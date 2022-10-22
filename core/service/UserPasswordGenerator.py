from random import choice, random
from string import ascii_lowercase


def newUsername():
    username = ''
    password = ''
    username = username.join(choice(ascii_lowercase) for i in range(8))
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    i = 0
    while i < 12:
        password += choice(chars)
        i = i + 1
    return username


def newPassword():
    password = ''
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    i = 0
    while i < 12:
        password += choice(chars)
        i = i + 1
    return password