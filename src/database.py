#テキストの集合から単語（名詞）のリストの集合を作成
class Database:
    def database(model):
        from preprocess import Preprocess,API_download
        lista=["医療","化学","経済","情報","心理","電気","土木","動物","法","歴史"]
        docs=[]
        for b in lista:
            for i in range(1,2):
                f = open("../data/日本語テキスト小/"+str(b)+str(i)+".txt")
                text=f.read()
                docs.append(text)

        tagger=API_download.mecab_download()
        word_lists=[]
        for doc in docs:
            text=Preprocess.cleaning_text(doc)
            word_class=Preprocess.mecab_list(text,tagger)
            noun_list=Preprocess.noun_extract(word_class)
            noun_list2=Preprocess.noun_squeeze(noun_list,model)
            noun_list3=Preprocess.noun_squeeze2(noun_list2)
            word_lists.append(noun_list3)
        return word_lists