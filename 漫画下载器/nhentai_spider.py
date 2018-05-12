# coding:utf8
"""
--------------------------------------------------------------------------
    File:   nhentai_spider.py
    Auth:   zsdostar
    Date:   2018/1/13 22:23
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   嘛，就是一个漫画网站的下载器
            In:漫画id
            Out:漫画
            有的漫画id和每一页的id不是同一个的，会报错.
            打包为exe的方式：
            pip install PyInstaller
            pyinstaller -F nhentai_spider.py
--------------------------------------------------------------------------
"""
import re
import os
import threading
import time
import requests

OUTPUT_DIR_NAME = u'漫画'


# 下载图片存到本地
def download_img(img_url, i, page_name, img_nums, model_of_image):
    if not os.path.exists(os.path.join(OUTPUT_DIR_NAME, page_name, '%d.%s' % (i, model_of_image))):
        with open(os.path.join(OUTPUT_DIR_NAME, page_name, '%d.%s' % (i, model_of_image)), 'wb') as f:
            print('downloading:(%d/%d)' % (i, img_nums))
            img = requests.get(img_url)
            f.write(img.content)
            print('finished downloading:(%d/%d)' % (i, img_nums))


if __name__ == '__main__':
    while True:
        while True:  # 不至于输错就抛异常
            try:
                page_id = int(input('Please input id: '))
                page_url = 'https://nhentai.net/g/%d/' % page_id
                model_of_image = raw_input('jpg or png?:')
                if model_of_image not in ('jpg', 'png'):
                    continue
            except Exception as e:
                print(e)
            else:
                break

        # 创建存储目录
        if not os.path.exists('Catchs'): os.mkdir('Catchs')
        # 为这个页面缓存一下吧
        if not os.path.exists('Catchs\\nhentai.%s.html' % page_id):
            print('downloading page...')
            page = requests.get(page_url).text.encode('utf8')  # Unicode要转成utf8才能写入文件
            print('finished downloading page...')
            with open('Catchs\\nhentai.%s.html' % page_id, 'wb') as f:
                f.write(page)
        else:
            with open('Catchs\\nhentai.%s.html' % page_id, 'r') as f:
                page = f.read()

        page_name = '%s - ' % page_id + re.search(pattern='<h2>(.+)</h2>', string=page).group(1).decode(
            'utf8')  # 漫画名&漫画的目录名
        img_nums = len(re.findall(pattern='thumb-container', string=page))  # 这个漫画多少张图片
        img_id = re.search(pattern='galleries/(\d+)', string=page).group(1)  # 这个漫画所有图片唯一id标识
        img_url = 'https://i.nhentai.net/galleries/%s/' % img_id

        # 创建存储目录
        if not os.path.exists(OUTPUT_DIR_NAME): os.mkdir(OUTPUT_DIR_NAME)
        if not os.path.exists(os.path.join(OUTPUT_DIR_NAME, page_name)):
            os.mkdir(os.path.join(OUTPUT_DIR_NAME, page_name))

        # 把url存储在队列
        img_urls = []
        for i in range(1, img_nums + 1):
            img_urls.append(img_url + '%d.%s' % (i, model_of_image))

        downloadThreads = []  # 线程池
        for i in range(img_nums):  # 为每个图片都创建个线程
            time.sleep(0.2)  # 为了防止爬虫被网站ban
            downloadThread = threading.Thread(target=download_img, args=(img_urls[i], i + 1, page_name, img_nums, model_of_image))
            downloadThreads.append(downloadThread)
            downloadThread.start()

        # Wait for all threads to end

        for downloadThread in downloadThreads:
            downloadThread.join()
        print(page_name, "is Finished.")
        print('-' * 50)
