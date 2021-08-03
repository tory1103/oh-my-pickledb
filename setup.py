"""
# What is PickleDB
PickleDB is a lightweight, fast, and simple database based on
[json](https://docs.python.org/3/library/json.html) module. And it's BSD licensed!

## Oh-My-PickleDB
Oh-My-PickleDB is an improved version of [PickleDB](https://github.com/patx/pickledb) with more database concepts than original one. Most important concepts are:

* Cryptography module - Encrypt/Decrypt database content using [FERNET](https://cryptography.io/en/latest/fernet/) encoding
* Code improvements - More readable documentation, improved code

## Oh-My-PickleDB is fun and easy to use
```python
>> > from my_pickledb import PickleDB

>> > database = PickleDB("test.db", load=True, auto_dump=True)

>> > db.set('key', 'value')

>> > db.get('key')
>> > 'value'

>> > db.dump()
>> > True
```

## Easy to Install
```python
# Using python pip
$ pip install my_pickledb
```

```python
# Using git
$ git clone https://github.com/tory1103/oh-my-pickledb.git
```

<h3 align="right">Useful Links</h3>
<p align="right">
<a href="https://tory1103.github.io/oh-my-pickledb/">
Website<br>
</a>
<a href="https://tory1103.github.io/oh-my-pickledb/docs.html">
Documentation<br>
</a>

</p>
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oh-my-pickledb",
    version="0.1.1",
    author="Adrián Toral",
    author_email="adriantoral@sertor.es",
    description="Oh-My-PickleDB is an open source key-value store using Python's json module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://tory1103.github.io/oh-my-pickledb/",
    project_urls={
        "Website": "https://github.com/tory1103/oh-my-pickledb",
        "Documentation": "https://tory1103.github.io/oh-my-pickledb/docs.html",
        "Issues": "https://github.com/tory1103/oh-my-pickledb/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Database",
    ],
    py_modules=["my_pickledb"],
    install_requires=["cryptography==3.1.1"],
    python_requires=">=3.6",
    keywords='python, json,database, key-value, python3, datastore, fernet, encryption-decryption, fernet-encryption',
)
