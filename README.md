# cloudendure-python

Python wrapper and CLI for [CloudEndure](https://www.cloudendure.com/)

[![Build Status](https://travis-ci.com/mbeacom/cloudendure-python.svg?branch=master)](https://travis-ci.com/mbeacom/cloudendure-python)

[Documentation](https://mbeacom.github.io/cloudendure-python/)

Package version: `0.0.6`

## Requirements

[Python 3.6+](https://www.python.org/downloads/)

## Installation & Usage

### pipenv

```sh
brew install pipenv # if not installed
pipenv install cloudendure
```

Then import the package:

```python
import cloudendure
```

### pip

```sh
pip install cloudendure
```

Then import the package:

```python
import cloudendure
```

### Setuptools

Install via [Pipenv](https://docs.pipenv.org/en/latest/).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import cloudendure
```

## Getting Started

### Logging in via CLI using environment variables

Please note:  `cloudendure` and `ce` can be used interchangeably

```sh
export CLOUDENDURE_USERNAME=<your_ce_user>
export CLOUDENDURE_PASSWORD=<your_ce_password>

cloudendure api login
```

or

```sh
export CLOUDENDURE_TOKEN=<your_ce_api_token>

ce api login
```

### Logging in via CLI inline

Please note:  `cloudendure` and `ce` can be used interchangeably

```sh
cloudendure api login --user=<your_ce_user> --password=<your_ce_password>
```

or

```sh
ce api login --token=<your_ce_token>
```

Logging in for the first time will generate the `~/.cloudendure.yml` file.

## Coming Soon

This project is currently a work in progress and will actively change.  This client has not yet been finalized and is entirely subject to change.

## Changelog

Check out the [CHANGELOG](CHANGELOG.md)
