import  json


# load方法，将文件中数据转换成json
books = json.load(open('./books.txt', mode='r', encoding='utf-8'))


# print(books)
#
# # <class 'dict'>
# print(type(books))
#
# print(books['store']['book'][0])

with open('./books.txt',mode='r',encoding='utf-8') as fp:
    content = fp.read()

books = json.loads(content, encoding='utf-8')

# print(content)
# <class 'str'>,获取其中数据，很不方便，批量获取需要使用正则
# print(type(content))


# print(books)
# print(type(books))
#
# book_info = books['store']['book']
#
#
# for book in book_info:
#     print(book['author'],book['title'])


# jsonpath，最后一样种解析
# Xpath bs4  jsonpath
# print(books['author'])



json.dump(books,open('./书.json',mode='w',encoding='utf-8'),ensure_ascii=False)

dumps = json.dumps(books,ensure_ascii=False)

print(dumps)
# <class 'str'>
print(type(dumps))