# coding:utf8
'''
Created on 2018年5月21日

@author: Ma.jian
'''
from baike_py import htmlManager_py, htmlDownloader_py, htmlParser_py, htmlOutput_py

class SpiderMain(object):
    def __init__(self):
        self.urls = htmlManager_py.UrlManager()
        self.downloader = htmlDownloader_py.UrlDownloader()
        self.parser = htmlParser_py.UrlParser()
        self.outputer = htmlOutput_py.UrlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                if count == 10:
                    break
                count = count + 1
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
            except:
                print 'craw failed'
                
        self.outputer.output_html()
    

if __name__=="__main__":
    root_url = "http://www.runoob.com/java/java-tutorial.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
    