#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time: 2020/11/8 3:37 下午
# Author: K
import requests

from config.cfg import blockUrl
from util.ctt import getContract, getW3, to0x, getAccount


# 代币名称
def name(cttAddr):
    contract = getContract(to0x(cttAddr))
    return contract.functions.name().call()


# 代币符号
def symbol(cttAddr):
    contract = getContract(to0x(cttAddr))
    return contract.functions.symbol().call()


# 代币发行量
def totalSupply(cttAddr):
    contract = getContract(to0x(cttAddr))
    return contract.functions.totalSupply().call()


# 代币小数位
def decimals(cttAddr):
    contract = getContract(to0x(cttAddr))
    return contract.functions.decimals().call()


# Token余额
def token_balance(cttAddr, address):
    address = to0x(address)
    cttAddr = to0x(cttAddr)

    contract = getContract(cttAddr)
    w3 = getW3()
    address = w3.toChecksumAddress(address)
    balance = contract.functions.balanceOf(address).call()
    if balance is None:
        return 0
    return balance


# Token交易
def token_tranfer(cttAddr, pvkey, toAddr, tokenAmt, gasLimit=None, gasPrice=None, nonce=None):
    cttAddr = to0x(cttAddr)
    c = getContract(cttAddr)
    w3 = getW3()
    acc = getAccount(pvkey)

    if c is None:
        return None

    if nonce is None:
        nonce = w3.eth.getTransactionCount(acc.address),

    if gasLimit is None:
        gasLimit = 80000

    if gasPrice is None:
        gasPrice = w3.eth.gasPrice

    if acc and tokenAmt > 0:
        fromAddr = w3.toChecksumAddress(to0x(acc.address))
        toAddr = w3.toChecksumAddress(to0x(toAddr))
        param = {
            'from': fromAddr,
            'value': 0,
            'gas': int(gasLimit),
            'gasPrice': int(gasPrice),
            'nonce': int(nonce[0]),
            # 'chainId': 1,
        }

        # print('toAddr', toAddr)
        # print('tokenAmt', tokenAmt)
        # print('TOKEN 交易参数 ', param)

        unicorn_txn = c.functions.transfer(toAddr, tokenAmt).buildTransaction(param)
        signed_txn = w3.eth.account.signTransaction(unicorn_txn, private_key=acc.privateKey)
        hash_tx = w3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()
        # print('TOKEN 交易哈希 ', hash_tx)
        return hash_tx
    return None


# Token交易记录
def token_transList(cttAddr, num=10):

    url = '{}/api/contract_orderList?page=1&nums={}&str={}'.format(blockUrl, num, to0x(cttAddr))
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    return data['data'], data['nums']
