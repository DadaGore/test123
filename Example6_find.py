word = 'hjjhahfiooiqedorsaeopiodu'

req_char =  ['a','e','i']

a = {"a":word.count("a"), "e":word.count("e"), "i":word.count("i")}
print(a)
f = {}
for i in word :
    if i in req_char:
        f[i] = word.count(i)
print(f)
h = {i:word.count(i) for i in word if i in req_char}
print(h)