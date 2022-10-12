a = ["hello", "hi", "python"]

b ={}

for i in a:
    b[i]=len(i)
print(b)

c = {i:len(i) for i in a}
print(c)