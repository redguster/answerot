# 直播答题小能手

**声明**

<font color="red"><b>本项目是作者业余开发，仅为娱乐和研究的目的，如有任何人凭此做何非法事情，均于作者无关。</b></font>

**交流反馈群**：**554355216**

**新增安装部署演示视频：** 链接: [https://pan.baidu.com/s/1smGXgIT](https://pan.baidu.com/s/1smGXgIT) 密码: `6kqu`

[项目介绍和安装部署](#INSTALL)

# 功能更新

## 更新 2018.2.10

1. **目前已经支持18个平台**。冲顶大会、今日。百万英雄、百度。好看视频、优酷。疯狂夺金、知乎。头脑王者、UC。 疯狂夺金、蘑菇街.大富翁、掌阅.百万文豪、映客.芝士超人、斗鱼.百万勇者、UC.红包赛、必要.抢钱冲顶(不稳定)、波波视频、京东直播、百万给你花、腾讯视频(需屏蔽弹幕)、微博.黄金 10 秒、千帆.知识英雄。

2. **两种 OCR 识别，百度和 tesseract**。百度有每天500条限制，而且是网络请求，可能影响速度，另外增加tesseract本地识别，还在测试中，需要训练数据。

3. **多种扩展搜索模式，更加有效的答题**。增加`自动去否定`针对题目待否定词，如`不`、`没`等，`自动加问搜`针对如问题是`下列是....`。

4. **页面重构美化**。使用bootstrap美化界面，操作更加方便。

![img](http://wx3.sinaimg.cn/large/006mu4nKly1foap1113v9j31fx0m145t.jpg)

5. **发布[v0.1.8](https://github.com/anhkgg/answerot/releases/tag/v0.1.8)版本**。

## 更新 2018.01.28

1. **增加4个答题平台支持**。分别是UC-疯狂夺金、蘑菇街-大富翁、掌阅-百万文豪、映客-芝士超人，感谢@[AUGUSTRUSH8](https://github.com/AUGUSTRUSH8)提供的题目图片。

![img](https://wx4.sinaimg.cn/mw1024/006mu4nKly1fnwsb04cklj30op069aac.jpg)

2. **开放[www.answerot.com](http://www.answerot.com)试用**。目前服务器配置较低，可能会影响速度，仅给有兴趣的朋友试用。如果后续有需求，再考虑升级服务器。**后续功能同步更新本项目、AnswerotX、服务器**。

## 更新 2018.01.26

1. **增加本地支持**。将题目检索和题目拉取功能分离，服务端只负责题目的识别和搜索以及展示结果，而本地功能负责拉取手机中的题目信息，这样可以部署一次服务端，再任意电脑开启本地功能即可使用。**本地功能需要AnserotX的支持，详情见[AnserotX](https://github.com/anhkgg/answerotx)介绍**。如果不想自己部署服务端，可以偷懒使用我提供的服务端 [http://answerot.com](http://answerot.com) (暂时还未部署)，然后只需下载本地功能模块[AnserotX](https://github.com/anhkgg/answerotx)即可。

2. **增加扩展搜索功能**。有些时候题目没有明显关键信息，如**下列那个是正确说法？**，这种题目是无法拿到结果的，此时其实可以通过答案来搜索确认答案，但是10秒时间肯定时不允许你来完成手工搜索的，那么扩展搜索来帮你完成，点击答案旁边的**搜**或者**加问搜**(问题和当前答案合并搜索)即可完成快速搜索，然后确认答案。

![img](https://wx3.sinaimg.cn/mw1024/006mu4nKly1fntxece40zj30m205yjrn.jpg)

## 发布v0.1.0

查看详情和下载 [v0.1.0](https://github.com/anhkgg/answerot/releases/tag/v0.1.0)

<h1 id='INSTALL'>项目介绍和安装部署</h1>

**支持：**
1. 冲顶大会
2. 百万英雄（西瓜视频）
3. 极速挑战（好看视频）
4. 疯狂夺金（优酷）
5. 头脑王者 (微信小程序)

**特性：**
1. 多平台自由切换选择
2. 多种搜索引擎选择（百度搜索，手机百度搜索，搜狗搜索，360搜索，必应搜索，谷歌搜索）
3. 答案匹配统计显示
4. 搜索结果页显示，匹配到的答案字体突出显示
5. 设备参数可配置，可视化获取设备信息
6. 一键获取答案

# 安装环境

所需资源包地址：[https://pan.baidu.com/s/1smGXgIT](https://pan.baidu.com/s/1smGXgIT) 密码:`6kqu`

1. 安装python2.7.14（安装中勾选环境变量配置，如果勾选了pip则省略第二步，否则需要自己配置环境变量）

```
https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi
```

2. 安装[setuptools](https://pypi.python.org/packages/6c/54/f7e9cea6897636a04e74c3954f0d8335cc38f7d01e27eec98026b049a300/setuptools-38.5.1.zip#md5=1705ae74b04d1637f604c336bb565720)和pip(`https://pypi.python.org/pypi/pip`)。下载之后，先安装setuptools，解压进入setuptools目录，按住shift，点击鼠标右键，弹出菜单后选择`在此处打开命令行`，在命令行窗口中输入命令`python setup.py install`安装。成功之后继续安装pip-9.0.1.tar，解压进入目录，按住shift，点击鼠标右键，弹出菜单后选择`在此处打开命令行`，在命令行窗口中输入命令`python setup.py install`安装。在安装python时勾选了pip忽略本步骤。

```
//这两个路径可以忽略，直接再网盘下载就行了
https://pypi.python.org/pypi/setuptools
https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz#md5=35f01da33009719497f01a4ba69d63c9
```
3. 使用pip安装django、PIL、simplejson，打开命令行窗口，分别输入下面的命令。

```
pip install django==1.11
pip install simplejson
```
下载安装PIL（提供的百度网盘中已经提供PIL）
```
http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe
```

4. 使用百度文字识别API识别图片文字，申请百度开发者账号，创建文字识别应用，拿到`API Key`和`Secret Key`

注册地址：
```
https://cloud.baidu.com/product/imagerecognition
```

登陆后，进入后台，点击左侧，产品服务->文字识别，创建应用即可。

```
https://login.bce.baidu.com/
```

然后管理应用中，找到`API Key`和`Secret Key`填入配置页的对象位置即可，`AppID`是不需要的。


需要研究API的看这里
```
https://cloud.baidu.com/doc/IMAGERECOGNITION/ImageClassify-API.html#.E7.AE.80.E4.BB.8B
```

5. 手机通过USB连接到电脑，开启手机调试模式（某些手机需要手工确认允许），运行adb devices，拿到手机设备号，也可在系统配置页提取到，本系统已经在配置页中自动获取。

# 怎么答题

1. 下载最新源码。可直接保存[压缩包](https://github.com/anhkgg/answerot/archive/master.zip)，也可通过`git clone git@github.com:anhkgg/answerot.git`下载（针对开发者）。压缩包解压。

2. 进入源码根目录，按住shift，点击鼠标右键，弹出菜单后选择`在此处打开命令行`，在命令行窗口中输入`python manage.py runserver 0.0.0.0:8000`即可启动服务。

```
c:\answerot\>python manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 23, 2018 - 00:21:22
Django version 1.11, using settings 'answerot.settings'
Starting development server at http://0.0.0.0:8008/
Quit the server with CTRL-BREAK.
```

如果出现`unable to open database file`错误，请先输入如下命令，再重新启动服务。

```
python manage.py migrate //初始化数据库
python manage.py runserver 0.0.0.0:8000 //启动服务
```

3. 打开浏览器访问 localhost:8000

4. 第一次使用，先点击初始配置进入配置页，配置必要的参数，如图。左下角黑色区域为自动获取到的设备信息，手机设备一般对应xxxxx device，拿到xxxx填入对应配置项即可。虚拟机一般是emilator-xxxx，填入这串值即可。

![img](screencap/config.png)

5. 配置完成后，返回答题页，打开答题app，等待题目出现，同时浏览器页面中答题按钮，大约2秒左右出现答案

6. 确认答案。某些时候搜索引擎的答案肯定不是很准的，所需需要自己浏览结果页，寻找答案，由于选项相关文字都突出显示，可以快速查找答案。

```
答案1：数量1
答案2：数量2
答案3：数量3
```

有以下几种情况：
1. 答案数量只有某一个有值，其他都是0，则很大可能这个就是正确答案
2. 每个答案都有数量，需要自己浏览结果页找到正确答案
3. 某些题目是否定意义，也就是问’不‘，’没有‘等，则取数量是0的答案
4. 由于受图片质量以及百度识图能力的影响，某些时候可能影响识图结果，需要注意

**注意**

1. 保持手机屏幕常量，否则截图失败
2. error: device offline, 重新插拔手机
3. 如果adb devices没有设备，确认手机打开usb调试模式，并且允许电脑调试

# 效果截图

![img](screencap/ans1.png)

![img](screencap/ans2.png)

![img](screencap/ans3.png)

![img](screencap/ans4.png)

# 捐助

如果觉得本项目对你有帮助，可以给作者发点小红包表示鼓励。

![img](wechatpay.png)