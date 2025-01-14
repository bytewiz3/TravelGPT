# Documentation

## 01. Users


### 1. Login

#### URL

- `POST` /api/v1/user/_login

Descriptions:

ContentType：`application/json`

#### Request Parameters

##### Body Parameter

| Name | Type | Required | Max Length | Description | Example Value |
| --- | --- | --- | --- | --- | --- |
| passwd | string | Y |  |  | admin |
| username | string | Y |  |  | admin |

#### Request Example

```
{
    "passwd": "admin",
    "username": "admin"
}
```

#### Response Parameters

None

#### Response Example

```
{
    "msg": "Login successful!",
    "code": 0,
    "data": {
        "user_id": "1777881255728259072",
        "username": "admin",
        "nickname": "admin",
        "roles": [
            "admin"
        ],
        "photo": "static/photo/head.jpg",
        "login_ip": "127.0.0.1",
        "last_login": "2024-04-17 11:35:25",
        "token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTMzMjQ5MjUsImV4cCI6MTcxMzkyOTcyNSwiaXNzIjoidHJhdmVsX2dwdCIsImRhdGEiOnsidXNlcl9pZCI6IjE3Nzc4ODEyNTU3MjgyNTkwNzIiLCJ1c2VybmFtZSI6ImFkbWluIiwibmlja25hbWUiOiJcdTdiYTFcdTc0MDZcdTU0NTgiLCJyb2xlcyI6WyJhZG1pbiJdLCJwaG90byI6InN0YXRpYy9waG90by9oZWFkLmpwZyIsImxvZ2luX2lwIjoiMTI3LjAuMC4xIiwibGFzdF9sb2dpbiI6IjIwMjQtMDQtMTcgMTE6MzU6MjUiLCJ0b2tlbiI6IiJ9LCJqdGkiOiI0ZjFnMjNhMTJhYSJ9.pJRcnuWtp3h_wFkeSC0pqW2apB3Ngw-S8oKpCxLu_8juyOAaOdCMWRHbJ5EC9rkiMrXnuihAm3FJPqhLPO7r5w"
    }
}
```

#### Error Code

None

### 2. User Registration

#### URL

- `POST` /api/v1/user/_register

Description:

ContentType：`application/json`

#### Request Parameters

##### Body Parameter

| Name | Type | Required | Max Length | Description | Example |
| --- | --- | --- | --- | --- | --- |
| passwd | string | Y | - |  | 2 |
| phone | string | N | - |  | 1111 |
| nickname | string | N | - |  | 2 |
| email | string | N | - |  | 2222 |
| username | string | Y | - |  | 5555 |

#### Request Example

```
{
    "passwd": "2",
    "phone": "1111",
    "nickname": "2",
    "email": "2222",
    "username": "5555"
}
```

#### Response Parameters

None

#### Response example

```
{
    "msg": "User registration successful!",
    "code": 0,
    "data": ""
}
---------------------------
{
    "code": 420,
    "msg": "The user already exists!"
}
```

#### Error Codes

None
## 02. Address


### 1. Gaode Address Navigation

#### URL

- `POST` /api/v1/address/address_list

Description:

ContentType：`application/json`

#### Request Parameters

##### Body Parameter

| Name | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| messages | array | 是 |  |  | ["杭州","杭州西湖"] |

#### 请求示例

```
{
    "messages": [
        "杭州",
        "杭州西湖"
    ]
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": [
        {
            "des_name": "西湖",
            "formatted_address": "浙江省杭州市西湖区",
            "country": "中国",
            "province": "浙江省",
            "city_code": "0571",
            "city": "杭州市",
            "ad_code": "330106",
            "street": [],
            "number": [],
            "location": "120.130396,30.259242",
            "annotate_url": "https://m.amap.com/navi/?dest=120.130396,30.259242&destName=杭州西湖&key=63b9df1479d58af21c4883226f1340b1"
        },
        {
            "des_name": "杭州",
            "formatted_address": "浙江省杭州市",
            "country": "中国",
            "province": "浙江省",
            "city_code": "0571",
            "city": "杭州市",
            "ad_code": "330100",
            "street": [],
            "number": [],
            "location": "120.210792,30.246026",
            "annotate_url": "https://m.amap.com/navi/?dest=120.210792,30.246026&destName=杭州杭州&key=63b9df1479d58af21c4883226f1340b1"
        }
    ],
    "code": 0,
    "data": ""
}
```

#### 错误码

无

### 2. 高德地址周边信息

#### URL

- `POST` /api/v1/address/circum_address_list

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| address_name | string | 是 |  |  | 杭州西湖 |

#### 请求示例

```
{
    "address_name": "杭州西湖"
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": {
        "suggestion": {
            "keywords": [],
            "cities": []
        },
        "count": "900",
        "infocode": "10000",
        "pois": [
            {
                "parent": [],
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.9",
                    "ticket_ordering": "0"
                },
                "recommend": "3",
                "type": "风景名胜;风景名胜;国家级景点",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/0fcf0bcc9827f4c28647f941472840fe"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/2fc7913f2429e2d443f4ac7ffd47afe0"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/9926946396f2b73c676dcc93f07634f9"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520206922",
                "typecode": "110202",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "西湖景区",
                "tel": "0571-89586930",
                "id": "B023B13L9M",
                "tag": "面面,特色小吃,龙井虾仁,东坡肉,西湖醋鱼,鸽子",
                "event": [],
                "entr_location": "120.153345,30.224729",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-17 10:17:54",
                "website": "www.hzwestlake.com",
                "address": "龙井路1号",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": [],
                "exit_location": [],
                "name": "杭州西湖风景名胜区",
                "location": "120.121282,30.222719",
                "shopid": [],
                "navi_poiid": "H51F022001_476398;4093",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.9",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;风景名胜",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/f19d171a36dfad3ba9aff4d943d15513"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/32b9cf5444f151c2335ca8b35850fa8a"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/624644d00b7e825a6293737c9ccb55da"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520217111",
                "typecode": "110200",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "苏堤",
                "tel": "0571-89586930",
                "id": "B023B0AC72",
                "tag": [],
                "event": [],
                "entr_location": "120.145021,30.228902",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-17 10:30:02",
                "website": [],
                "address": "杭州西湖风景名胜区内(东侧)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "601",
                "exit_location": [],
                "name": "杭州西湖风景名胜区苏堤",
                "location": "120.144497,30.228700",
                "shopid": [],
                "navi_poiid": "H51F022002_55970;94029",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B05MLT",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.8",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/b0997036a83403a275c888fe2b017738"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/1d2565bc3e4f117060e977b7b2511046"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/bc463a0f117bd88365bfd14a060a76af"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520311201",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": [],
                "tel": "0571-87179539",
                "id": "B023B13YJB",
                "tag": [],
                "event": [],
                "entr_location": "120.158138,30.258295",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-03-25 14:08:06",
                "website": [],
                "address": "杭州西湖风景名胜区内(东北角)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-六公园",
                "location": "120.157770,30.258607",
                "shopid": [],
                "navi_poiid": "H51F021002_135869",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.8",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;风景名胜",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/69e9b2188cacb3f4eb1eacde29b7787e"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "https://store.is.autonavi.com/showpic/1DF9AECDBE2546E4841CB4D79F00BA42"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://aos-cdn-image.amap.com/sns/ugccomment/ea66e6b2-5ee3-402e-bd0c-9f130628ba70.jpg"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310220",
                "typecode": "110200",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "断桥",
                "tel": "0571-87179539",
                "id": "B0FFFPPTEL",
                "tag": [],
                "event": [],
                "entr_location": "120.152289,30.259324",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-10 01:09:01",
                "website": [],
                "address": "北山街与白堤交叉口",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-断桥",
                "location": "120.151347,30.258151",
                "shopid": [],
                "navi_poiid": [],
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B05MLT",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.8",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "https://store.is.autonavi.com/showpic/04A76AB46308410FBDAF3C8577E67275"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "https://store.is.autonavi.com/showpic/A40FB050482C44919D4DBA0AAA180B12"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/66D5B9F1F5D741E08F9B82A107430AE9"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310202",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "上城区",
                "children": [],
                "alias": "湖滨一公园|西湖一公园",
                "tel": [],
                "id": "B023B06TYG",
                "tag": [],
                "event": [],
                "entr_location": "120.162786,30.250378",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-10 17:48:43",
                "website": [],
                "address": "湖滨路附近",
                "adcode": "330102",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-湖滨一公园",
                "location": "120.161535,30.250152",
                "shopid": [],
                "navi_poiid": "H51F021002_412923;10858",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "5.0",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;国家级景点",
                "photos": [
                    {
                        "provider": [],
                        "title": "春季",
                        "url": "http://store.is.autonavi.com/showpic/478ddbbf592df9e88466a3e10c5d6b70"
                    },
                    {
                        "provider": [],
                        "title": "春季",
                        "url": "http://store.is.autonavi.com/showpic/291127f3f2d2ceba0de575038ad6c885"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://aos-cdn-image.amap.com/sns/ugccomment/a1f6ed63-cdf2-4382-99a1-d8719297db86.jpg"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310220",
                "typecode": "110202",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "断桥残雪",
                "tel": "0571-87179539",
                "id": "B023B01EE6",
                "tag": "西湖醋鱼,小吃街,龙井虾仁,东坡肉,杭州小吃",
                "event": [],
                "entr_location": "120.152264,30.259343",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-17 10:34:19",
                "website": [],
                "address": "龙井路1号杭州西湖风景名胜区内(东北角)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-断桥残雪",
                "location": "120.151299,30.258106",
                "shopid": [],
                "navi_poiid": "H51F021002_382974;1499",
                "groupbuy_num": "0"
            },
            {
                "parent": "B0FFKQNUS4",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.7",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/7e1b5ce995e35a0ac685b2d994fc9790"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/4d1e298addccef3750660c11bc21adf9"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "https://store.is.autonavi.com/showpic/CC9C584DD4F0489595B37FFCD72427C9"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310101",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "中山公园",
                "tel": "0571-87996663",
                "id": "B023B02181",
                "tag": [],
                "event": [],
                "entr_location": "120.142423,30.250182",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-03-25 14:18:30",
                "website": [],
                "address": "孤山路1号杭州西湖风景名胜区内(东北角)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-中山公园",
                "location": "120.142482,30.250282",
                "shopid": [],
                "navi_poiid": "H51F021002_1461",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.9",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/b16eef9ee2b70e46b4aaf314ee111a47"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/c2e01bcb710be83244954c6a0f3b2bea"
                    },
                    {
                        "provider": [],
                        "title": "外景图",
                        "url": "http://store.is.autonavi.com/showpic/57a6949409878a743c3004d403b89928"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310221",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "上城区",
                "children": [],
                "alias": "湖滨公园",
                "tel": "0571-87179539",
                "id": "B023B05MLT",
                "tag": [],
                "event": [],
                "entr_location": "120.15838,30.258217",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-06 02:02:04",
                "website": [],
                "address": "杭州西湖风景名胜区内(东北角)",
                "adcode": "330102",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-湖滨公园",
                "location": "120.157851,30.257721",
                "shopid": [],
                "navi_poiid": "H51F021002_10708",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.8",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;风景名胜",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/f3fbc2aeaba1df9085cb07562e5cc8c0"
                    },
                    {
                        "provider": [],
                        "title": "秋季-autumn",
                        "url": "http://store.is.autonavi.com/showpic/11ba3e3c977ce53520e25bb64d2577c5"
                    },
                    {
                        "provider": [],
                        "title": "春季-spring",
                        "url": "http://store.is.autonavi.com/showpic/6ce974f26cfd42ec3ed8125af73a6089"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310122",
                "typecode": "110200",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "白堤|白沙堤",
                "tel": "0571-87967737",
                "id": "B0FFFTYEG4",
                "tag": [],
                "event": [],
                "entr_location": "120.152355,30.259285",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-17 10:32:21",
                "website": [],
                "address": "龙井路1号杭州西湖风景名胜区内(东北角)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-白堤",
                "location": "120.149189,30.255701",
                "shopid": [],
                "navi_poiid": "H51F021002_166557;92313",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": []
                },
                "recommend": "0",
                "type": "交通设施服务;停车场;公共停车场",
                "parking_type": "地面",
                "photos": [
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/681cbcfed71c6111f9e0cc46caa784df"
                    },
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/9cac8f46eb8bd8266db2fa89f51fc990"
                    },
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/e491ecdfa89e4feda0d8cee125e55556"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310121",
                "typecode": "150904",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": [],
                "tel": [],
                "id": "B0FFGB2AU5",
                "tag": [],
                "event": [],
                "entr_location": "120.144605,30.257055",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-01-28 19:08:21",
                "website": [],
                "address": "杭州西湖风景名胜区内(东北角)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": [],
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "北山",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "3",
                "exit_location": [],
                "name": "杭州西湖风景名胜区停车场",
                "location": "120.144664,30.256949",
                "shopid": [],
                "navi_poiid": "H51F021002_102879",
                "groupbuy_num": "0"
            },
            {
                "parent": [],
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": []
                },
                "recommend": "0",
                "type": "交通设施服务;停车场;公共停车场",
                "parking_type": "地面",
                "photos": [
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/c3806bbe1805039bfddcc5286ce774d9"
                    },
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/8ad12efc140ac9cadfafff6f7e57a6d7"
                    },
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/226ea0879fc37ea29baee194a793d38c"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520200712",
                "typecode": "150904",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": [],
                "tel": [],
                "id": "B023B15FMQ",
                "tag": [],
                "event": [],
                "entr_location": "120.097625,30.172204",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-01-22 00:17:57",
                "website": [],
                "address": "龙井路1号",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": [],
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": [],
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": [],
                "exit_location": [],
                "name": "杭州西湖风景名胜区停车场",
                "location": "120.097440,30.172151",
                "shopid": [],
                "navi_poiid": "H51F022001_14417",
                "groupbuy_num": "0"
            },
            {
                "parent": [],
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": []
                },
                "recommend": "0",
                "type": "交通设施服务;停车场;公共停车场",
                "parking_type": "地面",
                "photos": [
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/bcbb2ce730221abf4c7cf6a0c0c1c943"
                    },
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/ad4504cc81c614dad76af28e9a07f14d"
                    },
                    {
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/c86be313fbf11d93781c110ef3648e76"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520219212",
                "typecode": "150904",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "上城区",
                "children": [],
                "alias": [],
                "tel": [],
                "id": "B023B14SWA",
                "tag": [],
                "event": [],
                "entr_location": "120.159071,30.245097",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-02-17 16:16:18",
                "website": [],
                "address": "西湖风景名胜区内",
                "adcode": "330102",
                "pname": "浙江省",
                "biz_type": [],
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": [],
                "exit_location": [],
                "name": "杭州西湖风景名胜区停车场",
                "location": "120.159273,30.245310",
                "shopid": [],
                "navi_poiid": "H51F022002_67215",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.9",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;风景名胜",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/47f185b9daf7a9a1032c89412378e3f9"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/ABF77976722540059A6A79AEF1614EA3"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "https://store.is.autonavi.com/showpic/13DF29777E31455488C38153CB0406A2"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520217002",
                "typecode": "110200",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "浴鹄湾景区",
                "tel": "13777578768",
                "id": "B023B1D5U2",
                "tag": [],
                "event": [],
                "entr_location": "120.136252,30.225715",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-13 10:13:13",
                "website": [],
                "address": "三台山路赤山埠29号",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-浴鹄湾景区",
                "location": "120.136251,30.226033",
                "shopid": [],
                "navi_poiid": "H51F022002_73084",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B05MLT",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.6",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/602cd0cd24c0e5d5badbf8be1da66c5b"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/C5D408EBC4C243989F8DD69593151CED"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/d1fd7a2f06aed82a1557394a29ba5ca6"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310222",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "上城区",
                "children": [],
                "alias": "五公园",
                "tel": "0571-87179539",
                "id": "B023B1EQES",
                "tag": [],
                "event": [],
                "entr_location": "120.159738,30.256399",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-17 10:35:56",
                "website": [],
                "address": "杭州西湖风景名胜区内(龙翔桥地铁站B口步行430米)",
                "adcode": "330102",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-五公园",
                "location": "120.159631,30.256228",
                "shopid": [],
                "navi_poiid": "H51F021002_135870",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.8",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": "夏季-summer",
                        "url": "http://store.is.autonavi.com/showpic/74b51d5141a58ac662b09957c7db6713"
                    },
                    {
                        "provider": [],
                        "title": "秋季-autumn",
                        "url": "http://store.is.autonavi.com/showpic/d6349365855846ad6c37600ddf1f4083"
                    },
                    {
                        "provider": [],
                        "title": "冬季-winter",
                        "url": "http://store.is.autonavi.com/showpic/40b3d10b36daae77717c820479bd8d55"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520217221",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": [],
                "tel": "0571-87179539",
                "id": "B023B01EAA",
                "tag": [],
                "event": [],
                "entr_location": "120.155449,30.232853",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-04-09 01:27:01",
                "website": [],
                "address": "南山路",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-长桥公园",
                "location": "120.155057,30.232985",
                "shopid": [],
                "navi_poiid": "H51F022002_89",
                "groupbuy_num": "0"
            },
            {
                "parent": "B0FFKQNUS4",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.8",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;风景名胜",
                "photos": [
                    {
                        "provider": [],
                        "title": "春季-spring",
                        "url": "http://store.is.autonavi.com/showpic/7c59b9c01d797d7372df644ac99c3492"
                    },
                    {
                        "provider": [],
                        "title": "冬季-winter",
                        "url": "http://store.is.autonavi.com/showpic/1a551ff7b75a5b3948af0b8b3f9fb999"
                    },
                    {
                        "provider": [],
                        "title": "夏季-summer",
                        "url": "http://store.is.autonavi.com/showpic/322f5fc05cfd0eccc62a968012027a48"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520310100",
                "typecode": "110200",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "西泠桥",
                "tel": "0571-87996663",
                "id": "B023B0A6IY",
                "tag": "龙井虾仁,西湖醋鱼",
                "event": [],
                "entr_location": "120.138549,30.251884",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-03-13 02:00:58",
                "website": [],
                "address": "北山街与孤山路交叉口",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-西泠桥",
                "location": "120.138677,30.251775",
                "shopid": [],
                "navi_poiid": "H51F021002_330510",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.3",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;公园广场;公园",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://aos-cdn-image.amap.com/sns/ugccomment/4b945b81-26bc-4ca3-bf36-a07426819f8d.jpg"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://aos-cdn-image.amap.com/sns/ugccomment/0122356d-d71e-4106-9d29-e79945566bd3.jpg"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520214112",
                "typecode": "110101",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "上城区",
                "children": [],
                "alias": [],
                "tel": "0571-87179539",
                "id": "B0FFF33WR4",
                "tag": [],
                "event": [],
                "entr_location": "120.147903,30.203279",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2023-12-09 20:43:56",
                "website": [],
                "address": "龙井路1号杭州西湖风景名胜区(东南角)",
                "adcode": "330102",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": [],
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-海月水景公园",
                "location": "120.147567,30.203394",
                "shopid": [],
                "navi_poiid": "H51F022002_77519",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.3",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜相关;旅游景点",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "https://store.is.autonavi.com/showpic/9F1870252A7B497593E1E4F3144DEF5F"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/a9ee32c9798740d64c532aa4de17dc6d"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/11e1b2531996b0a9fda19e22ee1d5e0d"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520216120",
                "typecode": "110000",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "云谷",
                "tel": "13588832180",
                "id": "B0FFGS8T0N",
                "tag": [],
                "event": [],
                "entr_location": "120.138123,30.224556",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-02-17 13:17:37",
                "website": [],
                "address": "长河街道秋溢路500号乐通科技园2幢北3层",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-云谷",
                "location": "120.138125,30.224622",
                "shopid": [],
                "navi_poiid": "H51F022002_112364",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.5",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜;纪念馆",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/0f3a5498a87ed3e977ec0969edd37ed9"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/163ac4f30e5430ea738f5038e62745de"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/cbdc59070b59ce0dfa38c852d833e15d"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520213022",
                "typecode": "110204",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "杭州解放纪念碑",
                "tel": "0571-87179539",
                "id": "B023B05MNE",
                "tag": [],
                "event": [],
                "entr_location": "120.135912,30.197582",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-03-25 14:14:44",
                "website": [],
                "address": "之江路1号(钱塘江大桥西杭富路与之江路之间)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": [],
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-杭州解放纪念碑",
                "location": "120.135802,30.197418",
                "shopid": [],
                "navi_poiid": "H51F022002_166",
                "groupbuy_num": "0"
            },
            {
                "parent": "B023B13L9M",
                "distance": [],
                "pcode": "330000",
                "importance": [],
                "biz_ext": {
                    "cost": [],
                    "rating": "4.5",
                    "ticket_ordering": "0"
                },
                "recommend": "0",
                "type": "风景名胜;风景名胜相关;旅游景点",
                "photos": [
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://aos-cdn-image.amap.com/sns/ugccomment/e7cfb696-6576-47db-8743-7d3b65b43af9.jpg"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://aos-cdn-image.amap.com/sns/ugccomment/b67ef44d-1eec-4d70-af80-0820312925bf.jpg"
                    },
                    {
                        "provider": [],
                        "title": [],
                        "url": "http://store.is.autonavi.com/showpic/2d7c8fab52cc061cc451210ca7fca630"
                    }
                ],
                "discount_num": "0",
                "gridcode": "4520219012",
                "typecode": "110000",
                "shopinfo": "2",
                "poiweight": [],
                "citycode": "0571",
                "adname": "西湖区",
                "children": [],
                "alias": "里西湖",
                "tel": "0571-87179539",
                "id": "B0FFGNDMU8",
                "tag": [],
                "event": [],
                "entr_location": "120.135769,30.251408",
                "indoor_map": "0",
                "email": [],
                "timestamp": "2024-01-18 12:02:59",
                "website": [],
                "address": "龙井路1号杭州西湖风景名胜区(东北角)",
                "adcode": "330106",
                "pname": "浙江省",
                "biz_type": "tour",
                "cityname": "杭州市",
                "postcode": [],
                "match": "0",
                "business_area": "西湖",
                "indoor_data": {
                    "cmsid": [],
                    "truefloor": [],
                    "cpid": [],
                    "floor": []
                },
                "childtype": "301",
                "exit_location": [],
                "name": "杭州西湖风景名胜区-里西湖",
                "location": "120.136453,30.245651",
                "shopid": [],
                "navi_poiid": [],
                "groupbuy_num": "0"
            }
        ],
        "status": "1",
        "info": "OK"
    },
    "code": 0,
    "data": ""
}
```

#### 错误码

无
## 03. 会话

## 01. 会话


### 1. 创建新的会话

#### URL

- `POST` /api/v1/chat/_new_chat_pri

描述：

ContentType：`application/json`

#### 请求参数

#### 请求示例

```
{}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "创建新会话成功",
    "code": 0,
    "data": {
        "session_id": "1780493677727195136"
    }
}
------------------------------------
{
    "code": 401,
    "msg": "Signature has expired"
}
```

#### 错误码

无

### 2. 保存会话历史

#### URL

- `POST` /api/v1/chat/_save

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| session_id | string | 是 |  |  | 1778085631688318976 |
| messages | array | 是 |  |  |  |
|   └ role | string | 是 |  |  | user |
|   └ content | string | 是 |  |  | 您好 |

#### 请求示例

```
{
    "session_id": "1778085631688318976",
    "messages": [
        {
            "role": "user",
            "content": "您好"
        }
    ]
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "保存会话成功",
    "code": 0,
    "data": {
        "session_id": "1778085631688318976"
    }
}
```

#### 错误码

无

### 3. 用户会话历史

#### URL

- `POST` /api/v1/chat/history/list

描述：

ContentType：`application/json`

#### 请求参数

#### 请求示例

```
{}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "获取成功",
    "code": 0,
    "data": [
        {
            "session_id": "1778349338083336192",
            "messages": [
                {
                    "id": 6,
                    "session_id": "1778349338083336192",
                    "message": {
                        "role": "system",
                        "content": "您现在是旅游专家，旅游时间规划大师"
                    }
                }
            ]
        },
        {
            "session_id": "1778349346140594176",
            "messages": [
                {
                    "id": 7,
                    "session_id": "1778349346140594176",
                    "message": {
                        "role": "system",
                        "content": "您现在是旅游专家，旅游时间规划大师"
                    }
                }
            ]
        },
        {
            "session_id": "1780493677727195136",
            "messages": [
                {
                    "id": 8,
                    "session_id": "1780493677727195136",
                    "message": {
                        "role": "system",
                        "content": "您现在是旅游专家，旅游时间规划大师"
                    }
                }
            ]
        }
    ]
}
```

#### 错误码

无

### 4. 删除会话历史

#### URL

- `POST` /api/v1/chat/_delete_history

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| session_id_list | array | 是 |  |  | ["1778340533417156608","1778340591604736000"] |

#### 请求示例

```
{
    "session_id_list": [
        "1778340533417156608",
        "1778340591604736000"
    ]
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "删除会话成功",
    "code": 0,
    "data": ""
}
```

#### 错误码

无
## 02. 会话模板管理


### 1. 会话模板列表

#### URL

- `POST` /api/v1/chat/prompt/list

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| category | string | 是 |  |  | 1 |

#### 请求示例

```
{
    "category": "1"
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "获取成功",
    "code": 0,
    "data": [
        {
            "prompt_id": "1778669658526851072",
            "act": "11111111111111111",
            "prompt": "22222222222222"
        }
    ]
}
```

#### 错误码

无

### 2. 新增会话模板

#### URL

- `POST` /api/v1/chat/prompt/_add

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| act | string | 是 |  |  | ddd |
| category | string | 是 |  |  | 1 |
| prompt | string | 是 |  |  | ddd |

#### 请求示例

```
{
    "act": "ddd",
    "category": "1",
    "prompt": "ddd"
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "成功",
    "code": 0,
    "data": ""
}
```

#### 错误码

无

### 3. 删除会话模板

#### URL

- `POST` /api/v1/chat/prompt/_delete

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| id_list | array | 是 |  |  | [1,2] |

#### 请求示例

```
{
    "id_list": [
        1,
        2
    ]
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "删除Prompt成功",
    "code": 0,
    "data": ""
}
```

#### 错误码

无

### 4. 更新会话模板

#### URL

- `POST` /api/v1/chat/prompt/_update

描述：

ContentType：`application/json`

#### 请求参数

##### Body Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| act | string | 是 |  |  | 11111111111111111 |
| id | string | 是 |  |  | 3 |
| category | string | 是 |  |  | 1 |
| prompt | string | 是 |  |  | 22222222222222 |

#### 请求示例

```
{
    "act": "11111111111111111",
    "id": "3",
    "category": "1",
    "prompt": "22222222222222"
}
```

#### 响应参数

无

#### 响应示例

```
{
    "msg": "更新Prompt成功",
    "code": 0,
    "data": ""
}
```

#### 错误码

无

## 04. 匿名会话


### 1. 创建新的会话

#### URL

- `POST` /api/v1/chat/_new_chat_pri

描述：

ContentType：``

#### 请求参数

#### 响应参数

无

#### 响应示例

```
{}
```

#### 错误码

无

### 2. 进行会话

#### URL

- `POST` /api/v1/chat/_chat

描述：

ContentType：``

#### 请求参数
```
{
    "messages": [
        {
            "session_id": "N1780504179484270592",
            "role": "user",
            "content": "您好"
        }
    ]
}
```
#### 响应参数

无

#### 响应示例

```
{}
```

#### 错误码

无
