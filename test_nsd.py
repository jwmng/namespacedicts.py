from namespacedict import NameSpaceDict, _parse_namespaced_dict

print("# Empty initialisation")
# Create an empty NameSpaceDict
x = NameSpaceDict()
x['b.c'] = 5

print("# Assignment")
assert(x['b.c'] == 5)
assert(x.b.c == 5)
assert(x.b == NameSpaceDict({'c': 5}))


print("# Construction from dict/tuple")
# Or, build it from dict (or anything that `dict` supports):
x = NameSpaceDict({'b.c': 5})
x = NameSpaceDict((('b.c', 5),))

print("# Dict access")
# Access it as a dict:
assert(x['b'] == NameSpaceDict({'c': 5}))
assert(x['b'] == NameSpaceDict({'c': 5}))

print("# Object access")
# Or, as an object:
assert(x.b == NameSpaceDict({'c': 5}))
assert(x.b == NameSpaceDict({'c': 5}))

print("# Sub-object access")
# All superficial child dicts are NameSpaceDicts:
assert(x.b.c == 5)
assert(x.b['c'] == 5)

print("# Mixed assignment")
x = NameSpaceDict()
x['b.c'] = {'d': {'e': 1}}
x['y.z'] = 'alpha'
assert(x.b.c.d.e == 1)

print("# Iterables and membership")
assert(list(x) == ['b', 'y'])
assert(tuple(x) == ('b', 'y'))
assert('b' in x)

print("# Keys/Values/Items")
assert(list(x.keys()) == ['b', 'y'])
assert(list(x.values()) == [x['b'], x['y']])
assert(NameSpaceDict(x.items()) == x)


print("All tests passed")
