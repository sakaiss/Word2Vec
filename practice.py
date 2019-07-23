from gensim.models.word2vec import LineSentence, Word2Vec

inp='lastread.txt'
outp1 = 'wiki.zh.text.model'
outp2 = 'wiki.zh.text.vector'
model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5, workers=4)
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)

