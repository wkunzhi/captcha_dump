# -*- encoding: utf-8 -*-
# __author__ = 'Zok' 362416272@qq.com
# Date: 2020/09/18 11:17:02

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from tool.cjy import cjy


if __name__ == "__main__":
    rootdir = 'images'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        # if os.path.isfile(path):
        # # 你想对文件的操作
        print(path)
#         with open('images/' + filename, 'rb') as f:
#             img = f.read()
#         data = cjy.PostPic(img, 1902)
#         print(data)
#         if data.get('err_str') == 'OK':
#             new_file = data.get('pic_str') + '_' + data.get('md5') + '.jpg'
#             os.rename('images/' + filename, 'images/' + new_file)
