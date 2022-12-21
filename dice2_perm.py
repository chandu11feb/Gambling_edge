import itertools
import collections
dice=[1,1,2,2,3,3,4,4,5,5,6,6]
p=[]
su=[]
l=set(itertools.permutations(dice,2))
k=list(l)
p=p+k
#print(p)
p.sort()
print(*p,sep="\n")
for i in p:
    #print(sum(i))
    su.append(sum(i))
su.sort()
print(*su)
sum_stats=collections.Counter(su)
print(sum_stats)
print(len(p))