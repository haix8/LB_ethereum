#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time: 2020/11/8 3:37 下午
# Author: K

from flask import (
    Flask, jsonify, abort, make_response, request
)

from src.lb import newAccount, lb_balance, lb_tranfer, getLbGas, getTransByHash
from src.token import token_balance, token_tranfer, symbol, decimals, token_transList
from util.ctt import getW3

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def hello_world():
    abort(404)
    return 'Hello World!'


@app.route('/api/generateAddress', methods=["GET"])
def generateAddress():
    account = newAccount()
    return jsonify({
        "data": account,
        "code": 200,
        "msg": "地址生成成功"
    })


@app.route('/api/balance/<string:address>', methods=["GET"])
def balance(address):
    try:
        _balance = lb_balance(address)
        balance_raw = _balance
        balance_sun = _balance / 1e18

    except Exception as e:
        return jsonify({
            "data": None,
            "code": 500,
            "msg": str(e)
        })

    return jsonify({
        "data": {
            # 'cttAddr': cttAddr,
            # 'token': symbol,
            'balance': {
                'to_sun': balance_sun,
                'raw': balance_raw
            }
        },
        "code": 200,
        "msg": "查询LB余额成功"
    })


@app.route('/api/balanceOf/<string:cttAddr>/<string:address>', methods=["GET"])
def balanceOf(address, cttAddr):
    try:
        tokenDecimals = decimals(cttAddr)
        balance_raw = token_balance(cttAddr, address)
        balance_sun = balance_raw / pow(10, tokenDecimals)

    except Exception as e:
        return jsonify({
            "data": None,
            "code": 500,
            "msg": str(e)
        })

    return jsonify({
        "data": {
            'cttAddr': cttAddr,
            'token': symbol(cttAddr),
            'balance': {
                'to_sun': balance_sun,
                'raw': balance_raw
            }
        },
        "code": 200,
        "msg": "查询成功"
    })


@app.route('/api/transferToken', methods=["POST"])
def transferToken():
    cttAddr = request.form.get('cttAddr')

    _privKey = request.form.get('private_key')
    _to = request.form.get('to_address')
    _amount = request.form.get('amount')
    _gasLimit = request.form.get('gas_limit')
    _gasPrice = request.form.get('gas_price')

    try:
        w3 = getW3()
        _amount = w3.toWei(_amount, 'ether')
        if _amount <= 0:
            raise Exception('转账金额需大于0')

        _txn = token_tranfer(cttAddr, _privKey, _to, _amount, _gasLimit, _gasPrice)
        print(_txn)
        return jsonify({
            "data": _txn,
            "code": 200,
            "msg": "TOKEN交易成功"
        })
    except Exception as e:
        return jsonify({
            "data": None,
            "code": 500,
            "msg": str(e)
        })


@app.route('/api/transfer', methods=["POST"])
def transfer():
    # _from = request.form.get('from_address')

    _privKey = request.form.get('private_key')
    _to = request.form.get('to_address')
    _amount = request.form.get('amount')
    _gasLimit = request.form.get('gas_limit')
    _gasPrice = request.form.get('gas_price')

    try:
        w3 = getW3()
        _amount = w3.toWei(_amount, 'ether')
        if _amount <= 0:
            raise Exception('转账金额需大于0')

        txn = lb_tranfer(_privKey, _to, _amount, _gasLimit, _gasPrice)

        return jsonify({
            "data": txn,
            "code": 200,
            "msg": "LB交易成功"
        })
    except Exception as e:
        return jsonify({
            "data": None,
            "code": 500,
            "msg": str(e)
        })


@app.route('/api/getGas', methods=["GET"])
def getGas():
    gas = getLbGas()
    return jsonify({
        "data": gas,
        "code": 200,
        "msg": "查询成功"
    })


@app.route('/api/getDecimals/<string:cttAddr>', methods=["GET"])
def getDecimals(cttAddr):
    tokenDecimals = decimals(cttAddr)
    return jsonify({
        "data": tokenDecimals,
        "code": 200,
        "msg": "查询成功"
    })


@app.route('/api/getTransaction/<string:txn_id>', methods=["GET"])
def getTransaction(txn_id):
    try:
        txn = getTransByHash(txn_id)

        return jsonify({
            "data": txn,
            "code": 200,
            "msg": "交易查询成功"
        })
    except Exception as e:
        return jsonify({
            "data": None,
            "code": 500,
            "msg": str(e)
        })


@app.route('/api/getTransList/<string:cttAddr>', methods=["GET"])
def getTransList(cttAddr):
    try:
        data, nums = token_transList(cttAddr)
        tokenDecimals = decimals(cttAddr)
        return jsonify({
            "data": {'list': data, 'nums': nums, 'decimals': tokenDecimals},
            "code": 200,
            "msg": "交易记录查询成功"
        })
    except Exception as e:
        return jsonify({
            "data": None,
            "code": 500,
            "msg": str(e)
        })


if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port=53271)
