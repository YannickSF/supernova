# supernova
NoSQL database plug to REST API

---

## Quick Start : 

    cd supernova

Install dependances :  

    pip3 install -r requirements.txt

Start api :

    python3 index.py

---

## API Endpoints : 

### GET : 
*request :*

    curl --location --request GET 'http://localhost:5000/index'

*response*

        {
            "table": [
                {
                    "key": "value",
                    "keyPrime": "valuePrime",
                    "primary": "keyId"
                }
            ]
        }

### GET : key

*request :*

    curl --location --request GET 'http://localhost:5000/index/keyId'

*response :*

    {
        "item": [
            {
                "key": "value",
                "keyPrime": "valuePrime",
                "primary": "keyId"
            }
        ]
    }

### PUT : 
*request :*

    curl --location --request PUT 'http://localhost:5000/index/keyId' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "key": "value",
        "keyPrime": "valuePrime"
    }'

*response :*

    {
        "index": [
            1
        ],
        "item": [
            {
                "key": "value",
                "keyPrime": "valuePrime",
                "primary": "keyId"
            }
        ]
    }

### DELETE : 
*request :*

    curl --location --request DELETE 'http://localhost:5000/index/keyId'

*response :*

    {
        "item": [
            1
        ]
    }

--- 

## Docker 

build docker image:  

    docker build -t supernova .

run container :

    docker run -d -p 5000:5000 supernova


### ***change port***  

- change `PORT` value in `index.py` 
- rebuild image 
- run by changing `-p <new_port>:<new_port>`
 

--- 
Powered By [Yannick S. F](https://linktr.ee/Yannick_SF)