x = []
while True:
    i = input('enter a number: ')
    if i == 'done' : break
    v = float(i)
    x.append(v)

ave = (sum(x)/len(x))
print ('average:', ave)