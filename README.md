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
