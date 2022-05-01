dict = {}
dict['one'] = "this is one"
dict[2] = "this is 2"
print(dict)

tinydict = {"one" : 1, "two" : 2, 3 : 4, 6 : "six", "7" : "seven"}
print(tinydict)
print(type({}))
a = set()
print(type(a))
# print(list(tinydict.values()))
for i in tinydict.items():
    print(i)