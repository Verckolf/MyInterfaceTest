import json
from ApiManager.models import  TestReports
import re
import time

#获取请求中的参数
def get(request,key):
    text = json.loads(request.body.decode('utf-8'))[key]
    if not text:
        return None
    else:
        return text

#根据报告名查询报告ID
def getReportId(reortname):
    id = TestReports.objects.get(name=reortname).id
    return id

#通过正则匹配字符串
def getRe(string,pattern):
    return re.search(pattern,string).group(1)


def getTime(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp))