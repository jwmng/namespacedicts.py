from namespacedict import NameSpaceDict, _parse_namespaced_dict

print("# Empty initialisation")
# Create an empty NameSpaceDict
x = NameSpaceDict()
x['b.c'] = 5

print("Assignment")
assert(x['b.c'] == 5)
assert(x.b.c == 5)
assert(x.b == NameSpaceDict({'c': 5}))


print("# Construction from dict/tuple")
# Or, build it from dict (or anything that `dict` supports):
y = NameSpaceDict({'b.c': 5})
z = NameSpaceDict((('b.c', 5),))

print("# Dict access")
# Access it as a dict:
assert(y['b'] == NameSpaceDict({'c': 5}))
assert(z['b'] == NameSpaceDict({'c': 5}))

print("# Object access")
# Or, as an object:
assert(y.b == NameSpaceDict({'c': 5}))
assert(z.b == NameSpaceDict({'c': 5}))

print("# Sub-object access")
# All superficial child dicts are NameSpaceDicts:
assert(x.b.c == 5)
assert(x.b['c'] == 5)

print("# Mixed assignment")
z = NameSpaceDict()
z['b.c'] = {'d': {'e': 1}}
assert(z.b.c.d.e == 1)

print("All tests passed")
