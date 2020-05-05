# 3-Minute Python - Python examples, explaining topics in 3 minutes

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic&color=brightgreen)](https://www.python.org/) [![Version 3.8.2](https://img.shields.io/badge/python-3.8.2-blue.svg?style=plastic&color=brightgreen)](https://www.python.org/downloads/release/python-382/)

## Table of contents
* [Installation](#Installation)
    * [OS X & Linux](#os-x-&-linux)
        *  [With Pipenv](#with-pipenv)
* [Build and run](#Build-and-run)
    * [Using Docker](#Using-Docker)
    * [Using shell script](#Using-shell-script)
* [Logs](#logs)
    * [Local system](#local-system)
    * [Docker](#docker)
* [Release History](#Release-History)
* [Issue List](#issue-list)
* [Contribute](#Contribute)

## Installation

### Setup virtual env

####OS X & Linux:

##### With Pipenv

```shell script
# Update Pip
pip install --upgrade pip --no-cache

# Install pipenv
pip install pipenv

# Install dependencies and Virtualenv based on Pipfile
pipenv install --deploy --ignore-pipfile
```

## Release History
//TODO
* 1.0.0
[[Unreleased]]

## Issue List
[Current Issues](https://github.com/saurabh-slacklife/3-minute-python/issues)

## Contribute

If you want to be a contributor please follow the below steps.

1. Fork it (<https://github.com/saurabh-slacklife/3-minute-python/fork>)
2. Create your feature branch (`git checkout -b feature/add-feature-xyz`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/add-feature-xyz`)
5. Create a new Pull Request