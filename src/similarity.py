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
	if list2==[] :
		a1=0
		a2=0
	else:
		a1=max_cosine(list1,list2,model)
		a2=max_cosine(list2,list1,model)
	return (a1+a2)/2

#マックスアライメントがしきい値を超えた文章のインデックスを降順で返す
class Most_similarity:
	def most_similarity(nounlist,database,model,border):
		import numpy as np
		similarity=[]
		a=0
		for data in database:
			a+=1
			si=maximum_alignment(nounlist,data,model)
			similarity.append(si)
		similarity=np.asarray(similarity)
		rank=similarity.argsort()[::-1]
		ind=[]
		for r in rank:
			if similarity[int(r)]>border:
				ind.append(r)
		return ind