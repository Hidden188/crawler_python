# coding:utf8
'''
Created on 2018年5月21日
只使用了urllib2下载网页，是最简单的方法
@author: Ma.jian
'''
import urllib2
import sys   

class UrlDownloader(object):
    type = sys.getfilesystemencoding() 
    
    def __init__(self):
        pass
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        
        return response.read()


