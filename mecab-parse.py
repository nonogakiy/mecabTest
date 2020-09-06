import MeCab

tagger = MeCab.Tagger()
print(tagger.parse('test'))
