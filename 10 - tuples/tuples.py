txt = 'but soft by yonder window breaks'
words = txt.split()

print (txt)

print (words)

t = list()
for word in words :
    t.append((len(word),word))

print(t)

t.sort(reverse=True)

print(t)

res = list()
for length, word in t :
    res.append(word)

print(res)