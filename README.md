# mzitu
----
主要分为三个版本:
> 单页版、单图版、全图版

#### 运行环境
----
- Ubuntu 16.04
- Python 2.7.12
- Pycharm 2016.2

#### 使用方法
----
```
git clone https://github.com/leoyaojy/mzitu.git
```
```
cd mzitu 打开控制台
```
```
python page.py | single.py | full.py
```

#### 单页版
----
主要是针对妹子图每一页的图片进行下载，比如:**http://www.mzitu.com/page/1**此类链接的图片进行下载，我在代码中设置的是获取前四页的内容，即代码:`for i in range(1, 5)`,如果你想下载全站的图片，请修改`5`为对应的`最大页码 + 1`，测试效果如下图:
![](http://ww4.sinaimg.cn/large/0062vBsDgw1f7xip911swj30j90f40vp.jpg)
#### 单图版
----
主要是针对妹子图每个套图的**第一张**图片进行下载，比如:**http://www.mzitu.com/69627**此类链接的图片进行下载，我在代码中设置的是获取前四页套图的第一张图片，即代码:`for i in range(1, 5)`,如果你想下载全站的图片，请修改`5`为对应的`最大页码 + 1`，测试效果如下图:
![](http://ww3.sinaimg.cn/large/0062vBsDgw1f7xislib4wj30jj0f50vr.jpg)
#### 全图版
----
主要是针对妹子图每个套图的**全部**图片进行下载，由于套图数量过多，我只设置下载第一页的所有套图，即代码:`for i in range(1, 2)`,如果你想下载全站的图片，请修改`2`为对应的`最大页码 + 1`，测试效果如下图:
![](http://ww3.sinaimg.cn/large/0062vBsDgw1f7xitxap4nj30jf0f579z.jpg)
#### 作者
----
Leo Angel
