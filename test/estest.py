from elasticsearch7 import Elasticsearch

es = Elasticsearch("http://10.10.10.1:9200")
# print(es.info())
index_name = 'my_index'

data = {
    'title': '美国留给伊拉克的是个烂摊子吗',
    'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
    'data': '2011-12-16'
}
# 删除索引
#result1 =es.indices.delete(index='test-index')
#print(result1)
# 创建索引
#es.indices.create(index='news', ignore=400)
#result=es.index(index='news',doc_type='politics', id=1, body=data)
# print(result)

# 查看索引
#result = es.indices.get('*')
#print(result)

# 插入数据

#更新数据
result = es.update(index='news', doc_type='politics', body=data, id=1)
print(result)


# todo
# 删除数据

# todo
# 查询数据
# 1.term和terms查询
# 2.match
# match_all
# 布尔match
# multi_match

# 2.id和ids查询

# prefix查询   通过一个Field的前缀，从而查询到指定的文档

# fuzzy 查询   真正的模糊查询，输入字符的大概，ES就可以去根据输入的内容大概去匹配一个结果

# wildcard 查询   通配符查询，和Mysql中的like类似，在字符串中指定通配符*和占位符?

# regexp 正则查询，可以通过编写正则表达式查询。
# PS.  prefix,fuzzy,wildcard和regexp查询效率相对比较低，要求效率比较高时，避免使用。
