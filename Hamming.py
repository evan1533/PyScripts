def ham(s,t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count+=1
    
    return count

words = []
digs = ["0","1"]

def buildWords(s, n):
    global digs
    global words
    
    if len(s) < n:
        temp = s
        temp+=digs[0]
        buildWords(temp, n)

        temp = s
        temp+=digs[1]
        buildWords(temp, n)
    else:
        words.append(s);



buildWords("", 3)
s1 = words.copy()
s2 = words.copy()
is_zero = []
for s in s1:
    for t in s2:
        res = ham(s, t)
        str_res = str("(%s, %s)" % (s, t))
        flip_res = str("(%s, %s)" % (t, s))
        if res == 3 and str_res not in is_zero and flip_res not in is_zero:
            is_zero.append(str_res)

for elem in is_zero:
    print(elem)
