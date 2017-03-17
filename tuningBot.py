import requests


def joke():
    APIkey = "a8d98ff483b2498580e9e7b4d02aefe4"
    url = "http://www.tuling123.com/openapi/api"
    data = {
        "key" : APIkey,
        "info" : "讲个笑话"
    }
    try:
        resp = requests.post(url, data=data).json()
        assert(resp["code"] == 100000)
        return resp["text"]
    except Exception as e:
        print("Connect Tuning123 Error", e)
        return "哈哈哈……哈哈哈……好好笑呀……你怎么不笑？"

if __name__ == "__main__":
    print(joke())