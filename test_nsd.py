from namespacedict import NameSpaceDict

print("Running tests")

print("# Empty initialisation")
# Create an empty NameSpaceDict
x = NameSpaceDict()
x['b.c'] = 5

print("# Assignment")
assert x['b.c'] == 5
assert x.b.c == 5
assert x.b == NameSpaceDict({'c': 5})


print("# Construction from dict/tuple")
# Or, build it from dict (or anything that `dict` supports):
x = NameSpaceDict({'b.c': 5})
x = NameSpaceDict((('b.c', 5),))

print("# Dict access")
# Access it as a dict:
x['b.d'] = 6
x['a.b'] = 3
x['a.c'] = 5

assert x['b'] == NameSpaceDict({'c': 5, 'd': 6})
assert x['a'] == NameSpaceDict({'b': 3, 'c': 5})
assert x['b.d'] == 6
assert x['a.b'] == 3

print("# Object access")
# Or, as an object:
assert x.b == NameSpaceDict({'c': 5, 'd': 6})
assert x.a == NameSpaceDict({'b': 3, 'c': 5})

print("# Sub-object access")
# All superficial child dicts are NameSpaceDicts:
assert x.b.c == 5
assert x.b['c'] == 5

print("# Mixed assignment")
x = NameSpaceDict()
x['b.c'] = {'d': {'e': 1}}
x['y.z'] = 'alpha'
assert x.b.c.d.e == 1

print("# Iterables and membership")
assert list(x) == ['b', 'y']
assert tuple(x) == ('b', 'y')
assert 'b' in x

print("# Keys/Values/Items")
assert list(x.keys()) == ['b', 'y']
assert list(x.values()) == [x['b'], x['y']]
assert NameSpaceDict(x.items()) == x

print("# Mixed keys")
x[6] = NameSpaceDict({'this': 'that'})
assert x[6].this == 'that'

print("All tests passed")
