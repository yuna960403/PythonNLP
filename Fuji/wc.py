count = 0
with open ('/Users/fujiwara/Git/PythonNLP/data/kusamakura.txt') as f:
    for line in f:
        count += 1
print(count)

ld = open('/Users/fujiwara/Git/PythonNLP/data/kusamakura.txt').read()
print len(ld)
