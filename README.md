# qqwry.dat
纯真IP数据库，定时更新最新版本，每天会扫描两次（17：55和23：55），如果不出意外的话应该能够正常更新。

昨晚折腾了不少时间在这上面。

# 目录说明
 1、[app](https://github.com/FW27623/qqwry/tree/main/app)目录下为最新数据，每次更新会覆盖其中的内容，如果想要历史数据可在[Release](https://github.com/FW27623/qqwry/releases)里查看。

 2、qqwry.py文件用于获取最新微信公众号推文免费IP库的zip更新链接  

# 鸣谢
-  借鉴[HMBSbige](https://github.com/HMBSbige)/**[qqwry](https://github.com/HMBSbige/qqwry)**的workflow写法
-  使用[dscharrer](https://github.com/dscharrer)/**[innoextract](https://github.com/dscharrer/innoextract)**对获取到的 exe 文件进行解包操作

# 更新点

- workflow 中增加定时运行和手动运行操作
- 增加对仓库进行读写的操作
- 使用 requests 和 bs4库以使用 qqwry.py 来自动获取微信公众号推文免费IP库的zip更新链接
- 增加 workflow 对已有同名 [Release](https://github.com/FW27623/qqwry/releases) 的处理
- 对 workflow 中生成的 qqwy.dat 进行Git 操作，上传至 [app](https://github.com/FW27623/qqwry/tree/main/app) 目录下

# 如何使用

- 首先 Fork 本仓库，然后在[Personal access tokens (classic)](https://github.com/settings/tokens)里创建一个 Token ，给予 Repo 和 Workflow 权限。
- 然后打开 Fork 的仓库，点击Settings ，找到Secrets and variables ，点击 Actions ，增加一个名为qqwry的Secrets ，将刚刚生成的 Token 复制进去。
- 然后再新建两个变量 GIT_USERNAME 和 GIT_EMAIL  ，这两个填你自己的就好了，然后保存，运行 Action ，不出意外的话你应该很快就能看到最新的IP库了
