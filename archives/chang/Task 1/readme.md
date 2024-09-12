<h1 align="center">Usage of senti_c in China mainland</h1>

## 1 环境安装

创建一个空的环境，安装anaconda或miniconda，在开始菜单搜索conda，打开anaconda promot

![image-20240310134146033](https://raw.githubusercontent.com/fjwyz/images/main/pic/image-20240310134146033.png)

使用以下命令创建空环境并进入空环境（一行一行执行，执行过程中可能会让你键入y确认）。

```shell
conda create -n chang_senti_c python=3.8 pip

conda activate chang_senti_c
```

按以下命令安装依赖包，或使用项目中的requirements.txt

```shell
pip install senti_c —no-binary=wrapt,termcolor,sacremoses

pip install protobuf==3.20.0

pip install numpy==1.20.3

pip install opencc

pip install urllib3==1.25.11

pip install openpyxl 
```

若无法安装或速度极慢，按以下命令添加国内镜像源。

```shell
# 配置清华镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
# 配置中科大镜像(停止维护)
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple --trusted-host mirrors.ustc.edu.cn

# 配置阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# 配置腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
# 配置豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/

# 你只需配置其中一个即可
pip config set global.index-url http://pypi.douban.com/simple/  --trusted-host pypi.douban.com

pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

选第二行执行就行。

### 1.1 方法一

在成功运行一次后注释掉以下内容

> 注释model_structure.py第47行
>
> 注释sentence_sentiment_analysis.py第118行

### 1.2 方法二

下载`senti_c`的模型包，点[这里](http://www.im.ntu.edu.tw/~lu/data/senti_c/1DnSE7d_my_model.zip)去下载。

而后将安装包解压放在senti_c环境下的`pretrained_model\chinese_sentence_model\original`目录，以下是一个示例。

```
C:\Users\fjwyz\miniconda3\envs\env3\Lib\site-packages\senti_c\pretrained_model\chinese_sentence_model\original
```

而后下载另一个依赖文件，点[这里](https://docs.google.com/uc?export=download&id=1wVJUNhbHraehDyzo_2s5apWEoYmzRuUS)去下载。

放在senti_c环境下的`utils`目录，以下是一个示例。

```
C:\Users\fjwyz\miniconda3\envs\env3\Lib\site-packages\senti_c\utils
```

而后注释掉以下内容

> 注释model_structure.py第47行
>
> 注释sentence_sentiment_analysis.py第118行

