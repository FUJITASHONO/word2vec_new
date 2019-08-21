class Comparison:
	def comparison(input_text,model,database,border):
		from preprocess import Preprocess,API_download
		from similarity import Most_similarity
		from gensim.models import Word2Vec

		#文章中の無駄な記号などを削除
		text=Preprocess.cleaning_text(input_text)
		#mecabのダウンロード
		tagger=API_download.mecab_download()
		#mecabで文章を形態素解析
		word_class=Preprocess.mecab_list(text,tagger)
		#名詞だけを抜き出す
		noun_list=Preprocess.noun_extract(word_class)
		#word2vecでベクトル化できないものを削除
		noun_list2=Preprocess.noun_squeeze(noun_list,model)
		#アルファベット一文字の単語を削除
		noun_list3=Preprocess.noun_squeeze2(noun_list2)
		#ストップワードの除去
		noun_list4=Preprocess.stop_word(noun_list3)
		#類似度が高い文章のインデックスを抜き出し
		most_sim_index=Most_similarity.most_similarity(noun_list4,database,model,border)

		return most_sim_index