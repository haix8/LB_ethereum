#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time: 2020/11/8 3:37 下午
# Author: K

import requests

from util.ctt import getW3, to0x, getAccount, toLb


# 创建账户
def newAccount():
    w3 = getW3()
    acc = w3.eth.account.create()
    if acc is None:
        return None
    address = toLb(acc.address)
    return {
        'address': address,
        'privateKey': acc.key.hex()
    }


# LB余额
def lb_balance(address):
    w3 = getW3()
    address = w3.toChecksumAddress(to0x(address))
    ac_balance = w3.eth.getBalance(address)
    if ac_balance is None:
        return 0
    return ac_balance


# LB交易
def lb_tranfer(pvkey, toAddr, amount, gasLimit=None, gasPrice=None):
    acc = getAccount(pvkey)
    if acc:
        w3 = getW3()

        if gasLimit is None:
            gasLimit = 21000

        if gasPrice is None:
            gasPrice = w3.eth.gasPrice

        _from = acc.address
        _from_balance = w3.eth.getBalance(_from)
        # print('from余额', _from_balance)
        param = {
            'from': to0x(_from),
            'nonce': w3.eth.getTransactionCount(_from),
            'gasPrice': int(gasPrice),
            'gas': int(gasLimit),
            'to': w3.toChecksumAddress(to0x(toAddr)),
            'value': amount,
            # 'value': w3.toWei(amount, 'ether'),
            # data:b'',
        }
        print('交易参数 ', param)
        signed_txn = w3.eth.account.signTransaction(param, pvkey)
        hash_tx = w3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()

        print('交易哈希 ', hash_tx)
        return hash_tx
    return None


def getTransByHash(tx):
    w3 = getW3()
    tx = w3.eth.getTransactionReceipt(tx)
    return tx
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }
    r = requests.get('http://47.52.110.153:8080/api/contract_orderList_info?&str={}'.format(tx), headers=headers)
    if r.status_code != 200:
        return None
    data = r.json()
    if data['code'] == '-1':
        return None
    data['data']['from'] = toLb(data['data']['from'])
    data['data']['to'] = toLb(data['data']['to'])

    return data


# gas
def getLbGas():
    w3 = getW3()
    return w3.eth.gasPrice


def getLbNet():
    w3 = getW3()
    return w3.net
