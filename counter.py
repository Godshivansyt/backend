from collections import Counter 

cnt = Counter(["apple","Banana","orange","apple","banana","apple"])
print(cnt)

cnt = Counter("abracadabra")
print(cnt)


from collections import defaultdict

dd = defaultdict(list)
dd['fruits'].append("apple")
dd["fruits"].append("Banana")
print(dd)

from collections import namedtuple

point = namedtuple('Point',['x','y'])
p = point(10,20)
print(p.x,p.y)

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)