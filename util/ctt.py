#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time: 2020/11/8 3:37 下午
# Author: K

from eth_account import Account
from web3 import Web3, HTTPProvider

from config.cfg import httpPvi, FC, BEC, ABI


def getW3(uri=httpPvi):
    if uri:
        return Web3(HTTPProvider(uri))
    return None


def to0x(address):
    address = address[2:]
    return f'0x{address}'


def toLb(address):
    address = address[2:]
    return f'lb{address}'


def getAccount(prvKey):
    if not prvKey:
        return None
    if prvKey[:2] == '0x':
        prvKey = prvKey[2:]
    return Account.privateKeyToAccount(f'0x{prvKey}')


def getContract(addr=BEC):
    w3 = getW3()
    if addr and w3 and w3.isConnected():
        addr = w3.toChecksumAddress(addr)
        return w3.eth.contract(address=addr, abi=ABI)
    return None


def getTransaction(transaction_hash):
    w3 = getW3()
    result = w3.eth.getTransaction(transaction_hash)
    return result
