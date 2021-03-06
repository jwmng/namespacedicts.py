# namespacedict.py

Namespace / dictionary crossover

Aims to mix python dictionaries and dot-separated namespaces.
Any key containing a dot (`.`) will be interpreted as a multi-level key:

```
a.b.c = 5
│ 
└── b
    └── c
        └── 5
```

This allows us to infer a data hierarchy from using simple data structures 
(key, value arrays).

## Usage

### Construction
Create an empty NameSpaceDict:
```
>>> from namespacedict import NameSpaceDict
>>> a = NameSpaceDict()
>>> print(a)
<<< <NSDict {}>
```

Or, build one from dict (or any object supported by `dict()`):
```
>>> a = NameSpaceDict({'b.c': 5})
>>> a = NameSpaceDict((('b.c', 5),))
```

### Assigning

Assign a value as if it were a dict:
```
>>> a['b.c'] = 5
>>> a
<<< <NSDict {'b': {'c': 5}}>
```

Or, as an object:
```
>>> a.d = 5
>>> a
<<< <NSDict {'b': {'c': 5}, 'd': 5}>
```

_Note_: The parent `NSDict` must be initialised: setting `a['b.e.d'] = 3` would 
first require setting `a[b.e] = {}`.

_Note_: Other hashable key types are allowed, but of access like `a.3.b` does
not make sense and is thus not allowed (`a[3].b` would be valid).

### Access
Access it as a dict:

```
>>> a['b']
<<< {'c': 5}
```

Or, as an object:
```
>> a.b
<< {'c': 5}
```

Superficial child-dictionaries (those not embedded in non-dict objects) are
automatically converted to NameSpaceDicts:

```
>> a = NameSpaceDict()
>> a['b'] = {'c': {'d': 5}}
>> a.b.c.d
<< 5
```
