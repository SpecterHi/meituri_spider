# meituri_spider

美图日https://www.meituri.com/ 批量下载 

## 缘起

- 代码主要来自[python爬虫抓取网站相册图片（request+BeautifulSoup）](https://blog.csdn.net/l_hyde/article/details/83543205)一文，经过测试确认可以使用的起始页面不但可以是原文提到的模特页面，也可以是机构页面。
- 将原程序的起始页面和保存路径改为交互式输入，并修改保存路径默认为当前程序所在目录。

## 使用

在python3.6.7下测试通过。

```
pip install bs4 requests lxml
python getalbums.py
```

- 然后按提示输入多个起始页面，实测至少支持两类：
  1. 模特页面，如https://www.meituri.com/t/2441/ ，通过网站首页“美女库”进入
  2. 机构页面，如https://www.meituri.com/x/37/ ，通过网站首页“写真机构”进入
- 再输入保存路径，默认为当前目录

## TODO

- 加入并发下载以及相应的代理调度、随机暂停等反爬机制
- 加入对输入内容的校验
- 加入每个相册自动打包（不压缩）为zip等格式的功能，方便使用看图软件
