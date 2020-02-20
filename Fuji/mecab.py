# -*- coding: utf-8 -*-



import MeCab
#辞書を指定
mecab = MeCab.Tagger("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
mecab.parse("東京スカイツリ-")

#'東京スカイツリー \n'