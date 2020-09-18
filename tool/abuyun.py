# -*- encoding: utf-8 -*-
# __author__ = 'Zok' 362416272@qq.com
# Date: 2020/09/18 11:09:02
import requests
from setting import proxyUser, proxyPass 
# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"


proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}

# resp = requests.get(targetUrl, proxies=proxies)