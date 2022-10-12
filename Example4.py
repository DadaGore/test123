a = [2, 8, 5, 7, 3]
b=[]
for i in a:
    b.append (i*i)

print(b)
# list comprehension

d = [i**2 for i in a]
print(d)

e = [i**2 for i in range(11)]
print(e)

f = [i**2 for i in range (11) if i%2==0]
print(f)

m = [i for i in "Python"]
print(m)

# Python , learn

n = "Python"
o = "learn"
p = []
for i in n :
    for j in o:
        p.append(i+j)
        
print(p)
output = [i+j for i in "python" for j in "learn"]
print(output)
result = [i[1] for i in output]
print(result)
        