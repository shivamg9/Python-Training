# a = {1: 'a', 2: 'b'}
# # c = map(lambda x : x.values() if x.keys()%2==0 else 'ab', a.keys())
# # for k,v in a.items():
# c = lambda x: x.values() if x.keys() == 2 else 'abc'
# print(c(a))
# print(type(a.keys()))
# a = [12,3,4]
# for i in range(len(a)):
#     print(i)

a = [x for x in range(10)]
print(a)
a = [i for i in a if i%2==0]
print(a)