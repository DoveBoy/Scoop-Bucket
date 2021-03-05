# Auto Update Scoop Bucket
#
# Author: Dragon1573

from subprocess import getoutput

if __name__ == "__main__":
    manifests = getoutput('ls bucket').splitlines()
    for manifest in manifests:
        app = manifest.rstrip('.json')
        response = getoutput(f'pwsh .\\bin\\checkver.ps1 -U {app}').splitlines()
        if (len(response) > 1 and response[1].endswith('autoupdate available') and
            response[-1].startswith('Writing updated') and
            response[-1].endswith('manifest')):
            version = response[1].split(' ')[1]
            getoutput('git add .')
            getoutput(f'git commit -m "{app}: Update to version {version}"')
