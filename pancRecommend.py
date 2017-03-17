import requests
import random


def duibai():
    initUrl = "http://www.panc.cc/js/getmovie.php?"
    num = random.randint(1000,9999)
    url = initUrl + str(num)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers).json()
        taici =  resp["yan"]["taici"]
        source = resp["yan"]["source"]
        return "《{}》: {}".format(source,taici)
    except Exception as e:
        print("Connect Panc Error: ",url)
        return "Something Error, Try it later! "


def movieRecommend():
    initUrl = "http://www.panc.cc/js/getmovie.php?"
    num = random.randint(1000,9999)
    url = initUrl + str(num)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers).json()
        movies = resp["movie"]
        return ", ".join(movies)
    except Exception as e:
        print("Connect Panc Error: ",url)
        return "Something Error, Try it later! "

if __name__ == "__main__":
    print(duibai())
    print(movieRecommend())