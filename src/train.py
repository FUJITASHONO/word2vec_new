#テキストの集合を単語の集合にし、word2vecに学習させる
class Train:
	def train():
		from gensim.models import word2vec
		from preprocess import Preprocess,API_download
		lista=["医療","化学","経済","情報","心理","電気","土木","動物","法","歴史"]
		docs=[]
		for b in lista:
			for i in range(1,4):
				f = open("../data/日本語テキスト小/"+str(b)+str(i)+".txt")
				text=f.read()
				docs.append(text)

		tagger=API_download.mecab_download()
		word_lists=[]
		for doc in docs:
			text=Preprocess.cleaning_text(doc)
			word_class=Preprocess.mecab_list(text,tagger)
			word_list=[]
			for word in word_class:
				word_list.append(word[0])
			word_lists.append(word_list)
		model = word2vec.Word2Vec(word_lists, size=200,min_count=1,window=5,iter=100)
		return model