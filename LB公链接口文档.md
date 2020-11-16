## LB公链接口文档

- 区块浏览器：http://47.52.110.153/#/

- 接口地址：http://101.133.165.158:53271/

- FC = '0xb6c1b8ea6ad63e6f23aecefbdb1576bfb73bd484'
- BEC = '0x8204b4286218ef8a72013a6b1621d49a49fc631c'

  

### 生成地址

#### Request
- Method: **GET**
- URL:  ```/api/generateAddress```
#### Response
- Body
```json
{
    "code": 200,
    "data": {
        "address": "lb41feF830Cb2e8B6607A1d385F65EEa2edC0f9944",
        "privateKey": "0x3ec26236101ba385a2a2fd72e6c37b207958ea17c776347b826ec8cb4f839f64"
    },
    "msg": "地址生成成功"
}
```



### LB余额查询

#### Request

- Method: **GET**
- URL:  ```api/balance/{address}```

#### Response

- Body

```json
{
    "code": 200,
    "data": {
        "balance": {
            "raw": 599238864000000000,
            "to_sun": 0.599238864
        }
    },
    "msg": "查询LB余额成功"
}
```





### 代币余额查询

#### Request

- Method: **GET**
- URL:  ```api/balanceOf/{cttAddr}/{address}```

#### Response

- Body

```json
{
    "code": 200,
    "data": {
        "balance": {
            "raw": 7000000000000000000,
            "to_sun": 7.0
        },
        "cttAddr": "0xF318e5Fd9a918fCde0663b7ba684898f67222926",
        "token": "NOA"
    },
    "msg": "查询成功"
}
```





### LB交易

#### Request

- Method: **POST**

- URL:  ```api/transfer```

- Body

  | Key         | Type   | Value                                                        |
  | ----------- | ------ | ------------------------------------------------------------ |
  | to_address  | String | lb9977300e448fF84F5Da663E571aC703eDFCf500a                   |
  | private_key | String | 0x372b55c2a34202fb47fd3670850fb3c8b1182066a0822dc15802afc3a0af45d1 |
  | amount      | float  | 0.2                                                          |

#### Response

- Body

```json
{
    "code": 200,
    "data": "0x45cc35f663b78b5cbebcc7275b44071a34fc56b77d7a5dd59255c201695094d8",
    "msg": "LB交易成功"
}
```





### 代币交易

#### Request

- Method: **POST**

- URL:  ```api/transferToken```

- Body

  | Key         | Type   | Value                                                        |
  | ----------- | ------ | ------------------------------------------------------------ |
  | to_address  | String | lb9977300e448fF84F5Da663E571aC703eDFCf500a                   |
  | private_key | String | 0x372b55c2a34202fb47fd3670850fb3c8b1182066a0822dc15802afc3a0af45d1 |
  | amount      | float  | 1                                                            |
  | cttAddr     | String | 代币的合约地址   
#### Response

- Body

```json
{
    "code": 200,
    "data": "0xbb059826258dd06d5c669f425f44b8961204b68152fabaaf214aba4a50ba83ed",
    "msg": "TOKEN交易成功"
}
```





### 查询GasPrice

#### Request

- Method: **GET**
- URL:  ```api/getGas```

#### Response

- Body

```json
{
    "code": 200,
    "data": 4000000000,
    "msg": "查询成功"
}
```






### 交易记录查询

#### Request

- Method: **GET**
- URL:  ```api/getTransList/{cttAddr}/{limit}```

#### Response

- Body

```json
{
    "code": 200,
    "data": {
        "decimals": 18,
        "list": [
            {
                "Id": "0",
                "address": "0xB6C1B8eA6aD63E6f23AecefbDB1576Bfb73Bd484",
                "block_number": "751195",
                "data": "0xa9059cbb000000000000000000000000c0ddbeaa042ad8dd8b0c85cdbbc22320dc2779cf000000000000000000000000000000000000000000084595161401484a000000",
                "from": "0x2A860b2Ac175C2905502eEAd1A0EAbDa3d5141Ef",
                "gas": "52546",
                "gas_price": "180000000",
                "hash": "0xea3db568c437ff5a6aed6c2820e30c330d4efa46375b12f3584170633a6c41fb",
                "nonce": "108",
                "time": "1604989233",
                "to": "0xc0ddbeaa042ad8dd8b0c85cdbbc22320dc2779cf",
                "value": "10000000000000000000000000"
            }
        ],
        "nums": 1
    },
    "msg": "交易记录查询成功"
}
```



