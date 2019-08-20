class Preprocess:
    #文章中の無駄な記号などを削除
    def cleaning_text(text):
        import re
        pattern1=r"\[.+\]"
        text = re.sub(pattern1, '', text)   
        pattern2 = r"\d+"
        text = re.sub(pattern2, '', text)  
        pattern3 = r"\(.*\)"
        text = re.sub(pattern3, '', text)  
        pattern4 = r"\^"
        text = re.sub(pattern4, '', text)  
        pattern5 = r"％"
        text = re.sub(pattern5, '', text)  
        pattern6 = r"–"
        text = re.sub(pattern6, '', text)  
        pattern7 = r","
        text = re.sub(pattern7, '', text)  
        pattern8 = r"\."
        text = re.sub(pattern8, '', text)  
        pattern9 = r"/"
        text = re.sub(pattern9, '', text)  
        pattern10 = r"-"
        text = re.sub(pattern10, '', text)  
        pattern11 = r"\""
        text = re.sub(pattern11, '', text)  
        pattern12 = r":"
        text = re.sub(pattern12, '', text)
        pattern13=r"<"
        text=re.sub(pattern13,"",text)    
        pattern14=r";"
        text=re.sub(pattern14,"",text)
        pattern15=r"…"
        text=re.sub(pattern15,"",text)
        pattern16=r"，"
        text=re.sub(pattern16,"",text)
        pattern17=r"&"
        text=re.sub(pattern17,"",text)
        pattern18=r"\?"
        text=re.sub(pattern18,"",text)
        pattern19=r"!"
        text=re.sub(pattern19,"",text)
        pattern20=r">"
        text=re.sub(pattern20,"",text)
        pattern21=r"\+"
        text=re.sub(pattern21,"",text)    
        pattern23=r"—"
        text=re.sub(pattern23,"",text)    
        pattern24=r"•"
        text=re.sub(pattern24,"",text)    
        pattern25=r"="
        text=re.sub(pattern25,"",text)    
        pattern26=r"@"
        text=re.sub(pattern26,"",text)  
        pattern27=r"\("
        text=re.sub(pattern27,"",text)    
        pattern28=r"\)"
        text=re.sub(pattern28,"",text)    
        pattern29=r"\\.*"
        text=re.sub(pattern29,"",text)    
        pattern30=r"`"
        text=re.sub(pattern30,"",text)  
        pattern31=r"{"
        text=re.sub(pattern31,"",text)  
        pattern32=r"}"
        text=re.sub(pattern32,"",text)  
        pattern33=r"十"
        text=re.sub(pattern33,"",text)  
        pattern34=r"一"
        text=re.sub(pattern34,"",text)  
        return text
    #mecabで文章を形態素解析
    def mecab_list(text,tagger):
        import MeCab
        tagger.parse('')
        node = tagger.parseToNode(text)
        word_class = []
        while node:
            word = node.surface
            wclass = node.feature.split(',')
            if wclass[0] != u'BOS/EOS':
                if wclass[6] == None:
                    word_class.append((word,wclass[0],wclass[1],wclass[2],""))
                else:
                    word_class.append((word,wclass[0],wclass[1],wclass[2],wclass[6]))
            node = node.next
        return word_class

    #名詞だけを抜き出す
    def noun_extract(word_class):
        nounlist=[]
        for w in word_class:
            if w[1]=="名詞":
                nounlist.append(w[0])
        return nounlist
    #word2vecでベクトル化できないものを削除
    def noun_squeeze(nounlist,model):
        nounlist2=[]
        for w in nounlist:
            try:
                a=model[w]
                nounlist2.append(w)
            except KeyError as error:
                pass
        return nounlist2
    #アルファベット一文字の単語を削除
    def noun_squeeze2(nounlist):
        nounlist2=[]
        for w in nounlist:
            if not (w.isalpha()==True  and len(w)==1):
                nounlist2.append(w)
        return nounlist2
#mecabのダウンロード
class API_download:
    def mecab_download():
        import MeCab
        tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        return tagger