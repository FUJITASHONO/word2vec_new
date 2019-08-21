#テキストの集合から単語（名詞）のリストの集合を作成
class Database:
    def database(model):
        from preprocess import Preprocess,API_download
        import glob

        #docsにテキストの集合が、id2docにテキスト名が入る
        docs=[]
        id2doc=[]
        pathlist=glob.glob("../data/comparison_data/*")

        for path in pathlist:
            f = open(path)
            text=f.read()
            f.close()
            docs.append(text)
            id2doc.append(path)


        tagger=API_download.mecab_download()
        #テキストの下準備
        word_lists=[]
        for doc in docs:
            text=Preprocess.cleaning_text(doc)
            word_class=Preprocess.mecab_list(text,tagger)
            noun_list=Preprocess.noun_extract(word_class)
            noun_list2=Preprocess.noun_squeeze(noun_list,model)
            noun_list3=Preprocess.noun_squeeze2(noun_list2)
            noun_list4=Preprocess.stop_word(noun_list3)
            word_lists.append(noun_list4)
        return word_lists, id2doc