# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')

pattern = re.compile('<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
items = re.findall(pattern,content)
i = 1
print u'糗百段子第一页'
for item in items:
    print u'第%d条段子:'%(i)
    print  item
    i = i+1