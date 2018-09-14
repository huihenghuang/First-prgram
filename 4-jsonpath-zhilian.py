import urllib
import urllib.request

import json
import jsonpath

url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

if __name__ == '__main__':
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    # str
    jobs = response.read().decode('utf-8')

    jobs_json = json.loads(jobs, encoding='utf-8')
    # print(jobs_json)

    ret = jsonpath.jsonpath(jobs_json,'$..[salary,jobName,display]')
    print(ret)

    ret = jsonpath.jsonpath(jobs_json, '$..company[name]')
    print(ret)

    # 工作地点
    ret = jsonpath.jsonpath(jobs_json, '$..city.items[0][name]')
    print(ret)