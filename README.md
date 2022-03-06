# ANU Quantum Random Numbers for Python

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)

## Introduction

A simple (totally native) Python 3 API for [ANU QRNG API](https://qrng.anu.edu.au/contact/api-documentation/). 

Please use [new API from ANU QRNG](https://quantumnumbers.anu.edu.au/documentation) with API keys. [Python example](https://gist.github.com/cqtsma2/27af54ffddd6ababd114d9f642517611).

## Which functions **are** available?

For each function exists in [ANU QRNG API](https://qrng.anu.edu.au/contact/api-documentation/), there is a Python function.

## Which functions are **not** available?

They are [ANU QRNG]'s live numbers functions. In order to have Python functions, one might need to use [urllib3](https://urllib3.readthedocs.io/en/stable/) and [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). I will **not** implement those because I don't know ANU allows us to scrap. 

## Example

### Calling qrng.py functions
```python
from qrng import get_random_uint8, get_random_uint16, get_random_hex16

# Requesting 10 random numbers between 0–255
print(get_random_uint8(10))

# Requesting 5 random numbers between 0–65535
print(get_random_uint16(10))

# Requesting 10 blocks of random numbers in hexadecimal format. Each block is between 0000–ffff
print(get_random_hex16(10, block_size=2))
```

You can read the file. It's very simple.

## Note

- **Do not** use this code for cryptography implementation.
- **Do not** use this code to send many requests. Instead of doing that, use [the new API](https://quantumnumbers.anu.edu.au/documentation).



