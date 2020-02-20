import MeCab

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = open('/Users/fujiwara/Git/PythonNLP/data/kusamakura.txt').read()
mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
hinnsi = 0
meisi = 0
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    hinnsi += 1
    if node.feature.split(",")[0] == "名詞":
        meisi += 1
    #次の単語に進める
    node = node.next
print("名詞:"+str(meisi))
print("全単語:"+str(hinnsi))
print(str(meisi/hinnsi*100))