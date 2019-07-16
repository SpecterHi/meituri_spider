import requests
from bs4 import BeautifulSoup
import get_one_album as goa
import os
from functools import partial

inputNew = partial(input,'请输入想要下载的起始页面url，按回车输入下一个url，输入666按回车进入下一步：\n')
sentinel = '666' # 遇到这个就结束
url_list = []
for line in iter(inputNew, sentinel):
    url_list.append(line)
    url = line

headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer': 'https://www.meituri.com/t/4074/'
}

os_path = input('请输入要保存相册的路径，按回车使用当前目录：\n')
if os_path is '':
    os_path = './'

print("相册将保存到：%s" %(os_path))

album_url_list = [] #各相册链接

def parse_url(url):
    html = requests.get(url,headers=headers).content
    bsObj = BeautifulSoup(html,'lxml')
    name = bsObj.find('h1').text
    return bsObj,name

def next_page(bsobj): #判断是否有多页，返回页面数量。相册多于40套时多页
    num = 1
    nextPage = bsobj.find('div', {'id': 'pages'})
    if nextPage:
        pagenum = nextPage.findAll('a')
        num = len(pagenum)-1
        print(pagenum)
        print('有{}页'.format(str(num)))
    else:
        print('只有1页'.format(str(num)))
    return num

def url_connect(num): #主页多个页面链接存入列表
    for i in range(1,num):
        new_url = url_list[0]+'index_{}.html'.format(i)
        print('new url:',new_url)
        url_list.append(new_url)


#获取单个页面中各相册链接，列表返回
def get_photoAlbum_url(bsobj):
    url_obj = bsobj.find('div',{'class':'hezi'}).ul.findAll('p',{'class':'biaoti'})

    for u in url_obj:

        album_url = u.a.attrs['href']
        album_url_list.append(album_url)

    return album_url_list


#创建人物文件夹，下载各相册
def down_album(album_list,path):
    if not os.path.exists(path):
        os.mkdir(path)
    for url_list in album_list:

        goa.main2(url_list,path,album_list.index(url_list)+1)
    return ' 全部抓取完成！'


def main():

    obj,name = parse_url(url)
    num = next_page(obj)  #主页页面数
    if num > 1:
        url_connect(num)
    for pageUrl in url_list:
        bsobj,name = parse_url(pageUrl)
        listAlbum = get_photoAlbum_url(bsobj)

    path = os_path+name+str(len(listAlbum))+'套' #D://爬虫/xxx+xx套
    string = '共{}套'.format(str(len(listAlbum)))
    print(name,string)
    mes = down_album(listAlbum,path)
    print(name,string,mes)

if __name__ == '__main__':
    main()

