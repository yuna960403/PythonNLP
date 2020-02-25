#行数を数える
line_count = 0
with open('/Users/sakura/git/PythonNLP/Yuna/kusamakura.txt') as f:
    for line in f:
        line_count += 1

print('line_count:',line_count)

#文字数を数える
with open('/Users/sakura/git/PythonNLP/Yuna/kusamakura.txt') as f:
    text = f.read()

print('word_count:',len(text))