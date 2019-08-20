#コサインの計算
def cosine_similarity(vec1, vec2):
	import numpy as np
	inner_prod = np.dot(vec1,vec2)
	norm_a = (np.dot(vec1,vec1))**(1/2)
	norm_b = (np.dot(vec2,vec2))**(1/2)
	return inner_prod / (norm_a*norm_b)
#マックスアライメントを計算
def max_cosine(list1,list2,model):
	costotal=0
	for wa in list1:
		coslist=[]
		for wb in list2:
			coslist.append(cosine_similarity(model.wv[wa],model.wv[wb]))
		cosmax=max(coslist)
		costotal+=cosmax
	return costotal/len(list1)
#マックスアライメントの平均を計算		
def maximum_alignment(list1,list2,model):
	a1=max_cosine(list1,list2,model)
	a2=max_cosine(list2,list1,model)
	return (a1+a2)/2

#マックスアライメントが最も高い文章のインデックスを算出
class Most_similarity:
	def most_similarity(nounlist,database,model):
		import numpy as np
		lista=["医療","化学","経済","情報","心理","電気","土木","動物","法","歴史"]
		similarity=[]
		for i,data in enumerate(database):
			si=maximum_alignment(nounlist,data,model)
			similarity.append(si)
			print(lista[i])
			print(si)
		return np.argmax(similarity)