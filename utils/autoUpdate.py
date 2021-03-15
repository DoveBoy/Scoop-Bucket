# Auto Update Scoop Bucket
#
# Author: Dragon1573

from subprocess import getoutput

if __name__ == "__main__":
    # 获取所有 App Manifests
    manifests = getoutput("ls bucket").splitlines()
    for manifest in manifests:
        # 提取 App Name
        app = manifest.rstrip(".json")
        # 检查更新
        print(f"Updating {app} ...")
        response = getoutput(f"pwsh .\\bin\\checkver.ps1 -U {app}")
        print(response)
        response = response.splitlines()
        if (
            len(response) > 1
            and response[0].endswith("autoupdate available")
            and response[-1].startswith("Writing updated")
            and response[-1].endswith("manifest")
        ):
            # 提取最新的版本号
            version = response[0].split(" ")[1]
            # 创建 Git 提交
            print(getoutput("git add ."))
            print(getoutput(f'git commit -m "{app}: Update to version {version}"'))
        else:
            print(f"{app} is currently the latest version!")
