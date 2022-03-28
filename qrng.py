"""
Author: dinhanhx
"""
import requests

def construct_link(array_length: int = 1,
                   data_type: str = 'uint8',
                   block_size: int = 1):
    """Construct a link from

    https://qrng.anu.edu.au/contact/api-documentation/

    Args:
        array_length (int): The amount of numbers must be between 1-1024
        data_type (str): uint8, uint16, hex16
        block_size (int): only needed for hex16 data type.
            Sets the length of each block. Must be between 1-1024.
    """
    # Make sure array length in 1-1024
    if array_length < 1: array_length = 1
    if array_length > 1024: array_length = 1024
    # Make sure data type in available set
    if data_type in ('uint8', 'uint16', 'hex16'):
        if data_type == 'hex16':
            # Make sure block size in 1-1024
            if block_size < 1: block_size = 1
            if block_size > 1024: block_size = 1024
            return (f'https://qrng.anu.edu.au/API/jsonI.php?'
                    f'length={array_length}&type={data_type}&size={block_size}')
        else:
            return (f'https://qrng.anu.edu.au/API/jsonI.php?'
                    f'length={array_length}&type={data_type}')

    else:
        data_type = 'uint8'
        return (f'https://qrng.anu.edu.au/API/jsonI.php?'
                f'length={array_length}&type={data_type}')

def get_data(link: str):
    """Get data list from json response by requesting to link

    https://qrng.anu.edu.au/contact/api-documentation/

    Args:
        link (str): construct_link()

    Returns:
        list: a list of number
    """
    return requests.get(link).json()["data"]


def get_random_uint8(array_length: int=1):
    """Request X random numbers between 0-255

    https://qrng.anu.edu.au/contact/api-documentation/

    Args:
        array_length (int, optional): The amount of numbers
            must be between 1-1024.
            Defaults to 1.

    Returns:
        list: a list of number
    """
    link = construct_link(array_length, 'uint8')
    return get_data(link)


def get_random_uint16(array_length: int=1):
    """Request X random numbers between 0-65535

    https://qrng.anu.edu.au/contact/api-documentation/

    Args:
        array_length (int, optional): The amount of numbers
            must be between 1-1024.
            Defaults to 1.

    Returns:
        list: a list of number
    """
    link = construct_link(array_length, 'uint16')
    return get_data(link)


def get_random_hex16(array_length: int=1, block_size: int=1):
    """Request X blocks of random numbers in hexadecimal format.
    Each block is between 0000-ffff

    https://qrng.anu.edu.au/contact/api-documentation/

    Args:
        array_length (int, optional): The amount of numbers
            must be between 1-1024.
            Defaults to 1.

    Returns:
        list: a list of number
    """
    link = construct_link(array_length, 'hex16', block_size)
    return get_data(link)


if '__main__' == __name__:
    print(get_random_uint8(10))
    print(get_random_uint16(10))
    print(get_random_hex16(10, block_size=2))
    