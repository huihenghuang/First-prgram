import json
import jsonpath

# JSONObject
books = json.load(open('./books.txt', mode='r', encoding='utf-8'))

ret = jsonpath.jsonpath(books, '$.store.book[*]')
# print(ret)
# print(len(ret))


ret = jsonpath.jsonpath(books, '$..book[*]')
ret = jsonpath.jsonpath(books, '$..book[0]')
# print(ret)
# print(len(ret))

# 筛选条件，价格大于10
ret = jsonpath.jsonpath(books, '$..book[?(@.price > 10)]')

# print(ret)

# 筛选条件，选出来包含isbn属性的书

ret = jsonpath.jsonpath(books, '$..book[?(@.isbn)]')
print(ret)