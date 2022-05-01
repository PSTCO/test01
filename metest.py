'''

from konlpy.tag import Mecab 
mecab = Mecab(dicpath='E:/mecab/mecab-ko-dic')
#mecab = Mecab()

mecab.pos('아버지가방에들어가신다')

from konlpy.tag import Okt

tok = Okt()
print(tok.pos('안녕하세요'))
'''

import MeCab
mecab = MeCab.Tagger()
mecab.parse("안녕하세요. 홍길동입니다.")
