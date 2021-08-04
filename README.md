# What is PickleDB
[PickleDB](https://github.com/patx/pickledb) is a lightweight, fast, and simple database based on
[json](https://docs.python.org/3/library/json.html) module. And it's BSD licensed!

## Oh-My-PickleDB
Oh-My-PickleDB is an improved version of [PickleDB](https://github.com/patx/pickledb) with more database concepts than original one. Most important concepts are:

* Cryptography module - Encrypt/Decrypt database content using [FERNET](https://cryptography.io/en/latest/fernet/) encoding
* Code improvements - More readable documentation, improved code...
* Database Conversions - Works with bytes, json or str databases
* More flexibility - Save/load database as bytes, json or str, you decide!
* Statistics Tools - HopperDB works as a data analyzer

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
$ pip install oh-my-pickledb
```

```python
# Using git
$ git clone https://github.com/tory1103/oh-my-pickledb.git
$ cd oh-my-pickledb
$ pip install -r requirements.txt
```

## Contributing

You can propose a feature request opening an issue or a pull request.

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
