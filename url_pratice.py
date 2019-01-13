#coding:utf-8
import urllib.request
import re
import sys
import sys
import codecs
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#all_urls = []
path = "E:/python/pic/"
def openurl():
    headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
                'HOST':'i.meizitu.net',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.mzitu.com/xinggan/',
                'DNT': '1',
                'Connection': 'keep-alive'
                }
                #req =urllib.request.Request(url= m,headers=headers)
    url = "https://i.meizitu.net/2019/01/07b01.jpg"
    #url = "https://rainlua.wordpress.com/blog/"
    req =urllib.request.Request(url= url,headers=headers)
    rsp = urllib.request.urlopen(req)
    html = rsp.read()
    #解码
    #html = html.decode()
    #以写的方式打开
    tempfile = path+"1.jpg"
    htmlfile = open(tempfile,"wb")#utf-8避免编码失败
    htmlfile.write(html)
    htmlfile.close()
   #print(html)
def run(url):
    # 头文件，header是字典类型 
    headers = {  
     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36" 
    }
    req =urllib.request.Request(url= url,headers=headers)
    rsp = urllib.request.urlopen(req)
    html = rsp.read()
    #解码
    html = html.decode()
    #以写的方式打开
    #htmlfile = open(path+"text.html","w",encoding="utf-8")#utf-8避免编码失败
    #htmlfile.write(html)
    #htmlfile.close()
    #print(html)
    return html
def findurl(html):
    title = re.findall('<span><a href="(.*?)" target="_blank">(.*?)</a></span>',html,re.S)
    print(title)
    for m in title:
        #print(m)
        print("\n")
        #print("url"+m[0])
        print("\n")
        #print("title"+m[1])
        print("\n")
        filepath = path+m[1]
        is_exsit = os.path.exists(filepath)
        if not is_exsit:
            os.makedirs(filepath)
            print(filepath+"创建成功\n")
        else:
            print(filepath+"已存在\n")
        url = m[0]
        #print(url)
        html = run(url)
        statement = url+"/(.*?)"+"\'><span>"
        max_num =re.findall(statement,html,re.S)
        max_index = max_num[4]
        max_index = int(max_index)
        index = 0
        print(max_index)
        print("\n")
        for page_index in range(max_index):
            print(filepath+"page_index:"+str(page_index))
            print("\n")
            temp_url = url
            temp_url  = temp_url+"/"+str(page_index)
            html = run(temp_url)
            all_pic_temp = re.findall('<img src="(.*?)" alt=',html,re.S)
            for pic_index in all_pic_temp:
                headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
                'HOST':'i.meizitu.net',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.mzitu.com/xinggan/',
                'DNT': '1',
                'Connection': 'keep-alive'
                }
                req =urllib.request.Request(url= pic_index,headers=headers)
                rspon = urllib.request.urlopen(req)
                tempfile = rspon.read()
                filename = filepath+"/"+str(index)+".jpg"
                index = index +1
                with open(filename,'wb') as f :
                    f.write(tempfile)
                    f.close()

    #all_pic_link = re.findall('<li><a href="(.*?)" target="_blank">',html,re.S)
    #print(all_pic_link)
    #print(all_pic_link)
    '''
    index =0
    for i in all_pic_link:
        #print (i)
        for j in range(40):
            url  = i+"/"+str(j)
            #print(url)
            #print("\n")
            html = run(url)
            all_pic_temp = re.findall('<img src="(.*?)" alt=',html,re.S)
            #print(all_pic_temp)
            for m in all_pic_temp:
                print(m)
                headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
                'HOST':'i.meizitu.net',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://www.mzitu.com/xinggan/',
                'DNT': '1',
                'Connection': 'keep-alive'
                }
                req =urllib.request.Request(url= m,headers=headers)
                rspon = urllib.request.urlopen(req)
                tempfile = rspon.read()
                filename = path+str(index)+".jpg"
                index = index +1
                with open(filename,'wb') as f :
                    f.write(tempfile)
                    f.close()
                    
    '''    
    #print(title)
#def download:

def main():

    #openurl()
    url = "https://www.mzitu.com/"
    for page_idx in range(10):
        page_idx = page_idx+2
        temp_url = url
        temp_url = temp_url+"page/" + str(page_idx)+"/"
        html = run(temp_url)
        findurl(html)
    '''
    html = run(url)
    findurl(html)
    '''

    pass

if __name__ == '__main__':
    main()
    

