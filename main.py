# -*- encoding: utf-8 -*-
# __author__ = 'Zok' 362416272@qq.com
# Date: 2020/09/18 11:37:55
from core.down_captcha import Cat
from core.distinguish import start_dist


def down_cat(url, count, proxy):
    Cat(url, proxy).down(count)  #  开启代理
    print('验证码下载完成')

def distinguish_cat():
    pass

if __name__ == '__main__':
    # ----- 下载 ------
    url = 'http://zxgk.court.gov.cn/zhixing/captcha.do'  # 验证码下载地址
    count = 1000  # 验证码获取个数
    proxy = True  # 开启阿布云代理（需在 setting 中配置）
    down_cat(url, count, proxy)
    # ----- 识别 ------
    start_dist()