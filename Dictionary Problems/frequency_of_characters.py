text = "hello world"
frq = {}
for i in text:
    frq[i] = frq.get(i,0)+1
print(frq)