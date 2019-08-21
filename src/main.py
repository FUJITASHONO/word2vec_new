border=



#train.pyで学習したword2vecモデルのダウンロード
from train import Train
model=Train.train()

#フォルダ上のモデルをダウンロード
#from gensim.models import Word2Vec
#model=Word2Vec.load("name.model")


#wiki学習済みモデルをダウンロード
#from gensim.models import KeyedVectors
#model_dir = '../data/entity_vector.model.bin'
#model = KeyedVectors.load_word2vec_format(model_dir, binary=True)

#比較する文章のデータベースの作成
from database import Database
database,id2doc=Database.database(model)

#対象の文章の読み込み
import glob
path=glob.glob("../data/target_data/*")
path=path[0]
f = open(path)
text=f.read()
f.close()

#入力（対象の文章、判別モデル、文章のデータベース、類似度のしきい値）から出力（類似度がしきい値を超えた似てる文章を降順に）を出す
from comparison import Comparison
ind=Comparison.comparison(text,model,database,border)
for i in ind:
	print(id2doc[i])