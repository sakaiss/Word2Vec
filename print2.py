from gensim.models import Word2Vec

model = Word2Vec.load('wiki.zh.text.model')



result=model.most_similar(u'足球')
for e in result:
    print (e[0],e[1])

print("\b")


result = model.most_similar(u'篮球')
for e in result:
    print(e[0], e[1])
print("\b")

result=model.most_similar(u'衣服')
for e in result:
    print (e[0],e[1])
print("\b")

result=model.most_similar(u'公安局')
for e in result:
    print (e[0],e[1])
print("\b")
result=model.most_similar(u'东南大学')
for e in result:
    print (e[0],e[1])
print("\b")

list_sim1 = model.n_similarity('计算机', '自动化')
print(list_sim1)

list_sim2 = model.n_similarity('女人', '男人')
print( list_sim2)

list_sim3 = model.n_similarity('老师', '教师')
print(list_sim3)

list_sim4 = model.n_similarity('教室', '自习室')
print(list_sim4)


list = [u'男孩', u'女孩', u'鞋子', u'大叔']
print(model.doesnt_match(list))
list = [u'数学书', u'语文书', u'物理书', u'电脑']
print( model.doesnt_match(list))

list = [u'父亲', u'母亲', u'爷爷', u'鞋子']
print( model.doesnt_match(list))


list = [u'鞋子', u'袜子', u'衣服', u'书本']
print( model.doesnt_match(list))



list1 = [u'我', u'身体', u'很', u'累']
list2 = [u'今天', u'外面', u'下雨']
list3 = [u'我', u'今天', u'去', u'健身']
list_sim1 = model.n_similarity(list1, list2)
print(list1, '与', list2, '的相似度为', list_sim1)
list_sim2 = model.n_similarity(list1, list3)
print(list1, '与', list3, '的相似度为', list_sim2)

list_sim3 = model.n_similarity(list2, list3)
print(list2, '与', list3, '的相似度为', list_sim3)


