# Python3 program to print
# all primes less than N

#
def removee(s,r):
    #print(s)
    if len(s)<2:
        return s
    if s[0]!=s[1]:
        return s[0] + removee(s[1:],r)
    count = 2
    for i in range(1,r):
        if count == r:
            return removee(s[r:],r)
        if s[i] == s[i+1]:
            count+=1

s = input()
r = int(input())

s = removee(s,r)
print(removee(s,r))

