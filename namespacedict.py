# -*- coding: utf-8 -*-
""" NameSpacedDicts: Name-spaced hierarchical dictionaries.

See the accompanying README or class documentation of `NameSpaceDict` for more
info.

"""


def _parse_namespaced_dict(to_parse, top=None):
    top = {} if top is None else top

    for key, val in to_parse.items():
        root, *children = key.split('.')

        if not children:
            top[root] = val
        else:
            top.setdefault(root, {})
            top[root] = _parse_namespaced_dict({'.'.join(children): val},
                                               top=top[root])

    return top


def _nsd_or_value(val):
    if isinstance(val, NameSpaceDict):
        return val

    if isinstance(val, dict):
        return NameSpaceDict(val)

    return val


class NameSpaceDict(object):
    """ Dict with namespaces

    Usage:

        Create an empty NameSpaceDict:
        >> a = NameSpaceDict()
        >> a['b.c'] = 5

        Or, build it from dict (or anything that `dict` supports):
        >> a = NameSpaceDict({'b.c': 5})
        >> a = NameSpaceDict((('b.c', 5),))

        Access it as a dict:
        >> a['b']
        << {'c': 5}

        Or, as an object:
        >> a.b
        << {'c': 5}

        Namespaces are NameSpaceDicts:
        >> a.b.c
        << 5
        >> a.b['c']
        << 5

        """
    def __init__(self, init=None):
        """ Create a new NameSpaceDict

        Args:
            init (iterable/dict): Initial dictionary to convert. Any type that
            supports `dict(x)` is allowed.
        """
        super(NameSpaceDict, self).__init__()

        init = {} if init is None else init
        self._dict = _parse_namespaced_dict(dict(init))

    def __getattr__(self, name):
        if not isinstance(name, str):
            return self._dict[name]

        spaces = name.split('.')

        cur_v = self._dict
        for space in spaces:
            try:
                cur_v = cur_v[space]
            except KeyError:
                raise AttributeError

        return _nsd_or_value(cur_v)

    def __setattr__(self, name, value):
        if name != '_dict':
            self._dict[name] = value
        else:
            super(NameSpaceDict, self).__setattr__(name, value)

    def __setitem__(self, name, value):
        if not isinstance(name, str):
            self._dict[name] = value
            return

        # Parse the name recursively
        spaces = name.split('.')

        if len(spaces) < 2:
            self._dict.update({name: value})
            return

        self._dict.setdefault(spaces[0], {})
        cur_v = self._dict[spaces[0]]

        for space in spaces[1:-1]:
            cur_v.setdefault(space, {})
            cur_v = cur_v[space]

        # cur_v[spaces[-1]].update({spaces[-1]: value})
        cur_v[spaces[-1]] = value

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __repr__(self):
        return '<NSDict %s>' % str(self._dict)

    def __eq__(self, other):
        if isinstance(other, NameSpaceDict):
            return (self._dict == other._dict)
        return self._dict == other

    def __iter__(self):
        return (key for key in self._dict.keys())

    def __ne__(self, other):
        return not self.__eq__(other)

    def values(self):
        """ Like `dict.values`, but a generator with NameSpaceDicts"""
        return (_nsd_or_value(val) for val in self._dict.values())

    def keys(self):
        """ Like `dict.keys`, but a generator """
        return (key for key in self._dict.keys())

    def items(self):
        """ Like `dict.items` but returns NameSpaceDicts where possible """
        return ((key, val) for key, val in zip(self.keys(), self.values()))
