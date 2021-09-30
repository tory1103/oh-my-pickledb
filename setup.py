"""
# What is PickleDB

[PickleDB](https://github.com/patx/pickledb) is a lightweight, fast, and simple database based on
[json](https://docs.python.org/3/library/json.html) module. It's BSD licensed!

## Oh-My-PickleDB

Oh-My-PickleDB is an improved version of [PickleDB](https://github.com/patx/pickledb) with more database concepts than original one. Most important concepts are:

* Cryptography module - Encrypt/Decrypt database content using [FERNET](https://cryptography.io/en/latest/fernet/) encoding
* Code improvements - More readable documentation, improved code, etc...
* Database Conversions - Works with bytes, json or str databases
* More flexibility - Save/load database as bytes, json or str, you decide!
* Statistics Tools - HopperDB works as a data analyzer
* Frameworks - Pre-defined databases like UsersDB, ProductsDB, etc...

## Oh-My-PickleDB is fun and easy to use

```python
from my_pickledb import PickleDB

database = PickleDB("test.db", load=True, auto_dump=True)  # PickleDB object

db.set('key', 'value')  # Creates new key and value
db.get('key')  # Must return 'value'
db.dump()  # Must save database to file on specified path
```

## Easy to Install

```shell
# Using python pip
$ pip install oh-my-pickledb
```

```shell
# Using git
$ git clone https://github.com/tory1103/oh-my-pickledb.git
$ cd oh-my-pickledb
$ pip install -r requirements.txt
```

## Contributing

You can propose a feature request opening an issue, or a pull request.

Here is a list of oh-my-pickledb contributors:

<a href="https://github.com/tory1103/oh-my-pickledb/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=tory1103/oh-my-pickledb" />
</a>

<h3 align="right">Useful Links</h3>
<p align="right">
<a href="https://tory1103.github.io/oh-my-pickledb/">
Website<br>
</a>
<a href="https://tory1103.github.io/oh-my-pickledb/docs.html">
Documentation<br>
</a>
<a href="https://pypi.org/project/oh-my-pickledb/">
PyPi<br>
</a>

</p>
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh: long_description = fh.read()

setuptools.setup(
    name="oh-my-pickledb",
    version="0.4",
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
    packages=["my_pickledb"],
    package_dir={"": "src"},
    install_requires=["cryptography~=3.4.8", "fire~=0.4.0"],
    python_requires=">=3.6",
    keywords='python, json, database, key-value, python3, datastore, fernet, encryption-decryption, fernet-encryption',
)
