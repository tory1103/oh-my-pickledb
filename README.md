<p align="center">
  <a href="https://tory1103.github.io/oh-my-pickledb/" rel="noopener">
 <img src="docs/logo.png" alt="logo"></a>
</p>

<h3 align="center">OH-MY-PICKLEDB</h3>

<div align="center">

  ![GitHub status](https://img.shields.io/badge/status-active-brightgreen)
  ![GitHub issues](https://img.shields.io/github/issues/tory1103/oh-my-pickledb?color=yellow)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/tory1103/oh-my-pickledb)
  ![GitHub license](https://img.shields.io/github/license/tory1103/oh-my-pickledb?color=blue)
  ![GitHub last commit](https://img.shields.io/github/last-commit/tory1103/oh-my-pickledb?color=red)

</div>

---

<p align="center"> 
oh-my-pickleDB is a lightweight, fast, and intuitive data manager written in python
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](./TODO.md)
- [Contributing](./CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)
- [Useful Links](#links)

## 🧐 About <a name = "about"></a>
oh-my-pickleDB is an improved version of [PickleDB](https://github.com/patx/pickledb), with notable differences compared to the original. Most important differences are:
  - Cryptographic utils - Encrypt/Decrypt data content using [FERNET](https://cryptography.io/en/latest/fernet/) symmetric encryption
  - Code improvements - More readable documentation, improved code, etc...
  - Data conversions - Byte, json, or str conversions
  - More flexibility - Save/load data as bytes, json or str, you decide!
  - Utilities - Export data as XML

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites
```
python~=3.9
cryptography~=3.4.8
setuptools~=58.1.0
fire~=0.4.0
```

### Installing
```bash
# Using python pip
$ pip install oh-my-pickledb

# Using git
$ git clone https://github.com/tory1103/oh-my-pickledb.git
$ cd oh-my-pickledb
$ pip install -r requirements.txt
$ python setup.py install
```

## 🔧 Running the tests <a name = "tests"></a>
Tests are found on [tests](./tests) folder.
<br>
In future versions, tests will be added inside code documentation as multi-row comments.

### Break down into end to end tests
```bash
cd /tests
python3 <test_name>.py
```

## 🎈 Usage <a name="usage"></a>
```python
from my_pickledb import PickleDB

database = PickleDB("test.json")  # PickleDB object

database.set('key', 'value')  # Creates new key and value
database.get('key')  # Must return 'value'
database.save.as_json()  # Must save database to file on specified path
```

## 🚀 Deployment <a name = "deployment"></a>
oh-my-pickleDB is a python library, when installed, just import it to your project.
```python
import my_pickledb
from my_pickledb import *
```

## ⛏️ Built Using <a name = "built_using"></a>
- Python
- Json
- Data Structures

## ✍️ Authors <a name = "authors"></a>
- [@tory1103](https://github.com/tory1103) - Idea, Concept & Initial work

See also the list of [contributors](https://github.com/tory1103/LKD/contributors) who participated in this project.

<p align="center">
  <a href="https://github.com/tory1103/oh-my-pickledb/graphs/contributors">
    <img src="https://contributors-img.web.app/image?repo=tory1103/oh-my-pickledb"  alt=""/>
  </a>
</p>

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- [json](https://www.json.org/json-en.html) 
- [xml](https://en.wikipedia.org/wiki/Extensible_Markup_Language)
- [csv](https://en.wikipedia.org/wiki/Comma-separated_values)


## ✨ Useful links <a name = "links"></a>
- [Website](https://tory1103.github.io/oh-my-pickledb/)
- [Docs](https://tory1103.github.io/oh-my-pickledb/docs.html)
- [Pypi](https://pypi.org/project/oh-my-pickledb/)
