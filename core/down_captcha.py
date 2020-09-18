# __author__ = "zok" 362416272@qq.com
# Date: 2020/4/29 Python:3.7
# -*- encoding: utf-8 -*-

import requests
import os
from tool.abuyun import proxies

class Cat:
    def __init__(self, url, proxy=False):
        self.target_url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        self.proxy = proxy

    @property
    def check_file(self):
        rootdir = 'images'
        list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
        return len(list)


    def get_img(self, name):
        if self.proxy:
            response = requests.get(self.target_url, headers = self.headers, proxies=proxies)
        else:
            response = requests.get(self.target_url, headers = self.headers)
        if not response.status_code == 200: return
        with open('images/' + str(name) + '.jpg', 'wb') as f:
            f.write(response.content)
            print('[写入成功]:', str(name) + '.jpg')

    def down(self, num):
        file_num = self.check_file
        for i in range(1, num+1):
            self.get_img(i+file_num)


if __name__ == '__main__':
    url = 'http://zxgk.court.gov.cn/zhixing/captcha.do'
    count = 5
    cat = Cat(url)  #  开启代理
    cat.down(count)
    print('完成')
