# Janomeのインストール
# pip install janome | tail -n 1
# ターミナルで実行

# Janomeのロード
from janome.tokenizer import Tokenizer

path = "data/kusamakura.txt"
with open(path) as text :
    text = text.read()

# ファイル整形
import re

# 注釈の除去
if "※" in text :
    for i in range(text.count("※")) :
        s = int(text.find("※"))
        g = int(text.find(")"))
        text = text[:s] + text[g + 1:]

line = text.count("\n")

# 空行の削除
text = re.sub("\n", "", text)
text = re.sub("\r", "", text)
text = re.sub("\u3000", "", text)

word = len(text)

print(line, word)
# line = 1140
# word = 96340