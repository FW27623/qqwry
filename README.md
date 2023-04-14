# qqwry.dat
**纯真IP数据库，使用 Github Action 定时更新最新版本，每天会扫描两次（17:55和23:55），如果不出意外的话应该能够正常更新。**

**最近花了不少时间在这上面。有帮助到的可以点点 [Star⭐](https://github.com/FW27623/qqwry/star)支持下。**

# 目录说明
 1、[app](https://github.com/FW27623/qqwry/tree/main/app) 目录下为最新数据，每次更新会覆盖其中的内容，如果想要历史数据可在 [Release](https://github.com/FW27623/qqwry/releases) 里查看。

 2、`qqwry.py` 文件用于获取最新微信公众号推文内发布的免费IP库的zip更新链接  

# 鸣谢
-  借鉴 [HMBSbige](https://github.com/HMBSbige)/[qqwry](https://github.com/HMBSbige/qqwry) 的 `workflow` 写法
-  使用 [dscharrer](https://github.com/dscharrer)/[innoextract](https://github.com/dscharrer/innoextract) 对获取到的 exe 文件进行解包操作

# 更新点

- 增加对仓库进行读写的操作权限
- `workflow` 中增加定时运行和手动运行操作
- 使用 `requests` 和 `bs4` 库以使用 `qqwry.py` 来自动获取微信公众号推文发布的免费IP库的zip更新链接
- 增加 `workflow` 对已有同名 [Release](https://github.com/FW27623/qqwry/releases) 的处理
- 增加对 `workflow` 中解包完成的 `qqwy.dat` 进行Git 操作，默认上传至 [app](https://github.com/FW27623/qqwry/tree/main/app) 目录下

# 如何使用

- 首先 Fork 本仓库，然后在 [Personal access tokens (classic)](https://github.com/settings/tokens) 里创建一个 Token ，给予 `Repo` 和 `Workflow` 权限。

  <p align=center><img src="https://pic.1016.site/file/77bfb30076803ef0487a4.png" style="zoom:50%;" /></p>

  <p align=center><img src="https://pic.1016.site/file/47e907c05535b078d36c6.png" style="zoom:50%;" /></p>

- 然后打开 Fork 的仓库，点击 `Settings` ，找到`Secrets and variables` ，点击 `Actions` ，增加一个名为 `qqwry` 的`Secrets` ，将刚刚生成的 `Token` 复制进去。

  <p align=center><img src="https://pic.1016.site/file/950cf56dd4cf8fe773721.png" style="zoom:50%;" /></p>

- 然后再新建两个变量 `GIT_USERNAME` 和 `GIT_EMAIL`  ，这两个填你自己的就好了，然后保存，运行 Action ，不出意外的话你应该很快就能看到最新的IP库了。

  <p align=center><img src="https://pic.1016.site/file/e4011db8b992a5da6a28b.png" style="zoom:50%;" /></p>
