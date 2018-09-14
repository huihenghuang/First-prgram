import requests

import json

# pip install jsonpath
import jsonpath

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

if __name__ == '__main__':
    # 线程，主线程，继承Thread
    response = requests.get(url=url,verify = False,headers = {'User-Agent':'123456abc'})
    response.encoding = 'utf-8'

    # str
    cities = response.text

    cities_json = json.loads(cities, encoding='utf-8')

    # print(cities)
    print(cities_json)
    ret = jsonpath.jsonpath(cities_json,'$..[name,code,id]')
    # print(ret)

    # ret = jsonpath.jsonpath(cities_json,'$[A]') False

    # .现行节点 /
    ret = jsonpath.jsonpath(cities_json,'$.content.data.allCitySearchLabels.A')
    print(ret)

    # 现行节点下没有data，这个返回值False
    ret = jsonpath.jsonpath(cities_json,'$.data')
    print(ret)

    # .or [] == ..
    ret = jsonpath.jsonpath(cities_json,'$.[name]')

    print(ret)
