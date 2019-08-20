#判別モデルの作成
from train import Train
model=Train.train()

#比較する文章のデータベースの作成
from database import Database
database=Database.database(model)

#対象の文章の読み込み
f = open("../data/日本語テキスト小/薬.txt")
text=f.read()

#入力（対象の文章、判別モデル、文章のデータベース）から出力（似てる文章）を出す
from main import Main
ind=Main.main(text,model,database)
lista=["医療","化学","経済","情報","心理","電気","土木","動物","法","歴史"]
print(lista[ind])