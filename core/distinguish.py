# -*- encoding: utf-8 -*-
# __author__ = 'Zok' 362416272@qq.com
# Date: 2020/09/18 11:17:02

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from tool.cjy import cjy
from concurrent.futures import ThreadPoolExecutor


def dist(path):
    if len(path) > 36: return
    with open(path, 'rb') as f:
            img = f.read()
    data = cjy.PostPic(img, 1902)
    if data.get('err_str') == 'OK':
        new_file = data.get('pic_str') + '_' + data.get('md5') + '.jpg'
        os.rename(path, 'images/' + new_file)
        print(data)
    else:
        print('[识别失败]:', path, data)

def start_dist(): 
    print('开始超级鹰识别')
    pool = ThreadPoolExecutor()
    list = os.listdir('images')  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join('images', list[i])
        pool.submit(dist, path) 
    pool.shutdown(wait=True)  
    print('主进程')    

if __name__ == "__main__":
    start_dist()
    print('主')