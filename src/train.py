#テキストの集合(docs)があれば、学習できる
class Train:
	def train():
		from gensim.models import word2vec
		from preprocess import Preprocess,API_download
		import glob

		#train_dataから学習に用いるテキストを選択
		docs=[]
		pathlist=glob.glob("../data/train_data/*")
		for path in pathlist:
			f=open(path)
			text=f.read()
			f.close()
			docs.append(text)

		#テキストの前準備
		tagger=API_download.mecab_download()
		word_lists=[]
		for doc in docs:
			text=Preprocess.cleaning_text(doc)
			word_class=Preprocess.mecab_list(text,tagger)
			word_list=[]
			for word in word_class:
				word_list.append(word[0])
			word_lists.append(word_list)
		#学習をさせ、モデルを作る
		model = word2vec.Word2Vec(word_lists, size=200,min_count=1,window=5,iter=100)
		return model