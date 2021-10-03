import setuptools

with open("README.md", "r", encoding="utf-8") as fh: long_description = fh.read()

setuptools.setup(
    name="oh-my-pickledb",
    version="0.4.1-dev",
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
