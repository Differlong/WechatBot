import requests
import itchat
from pancRecommend import duibai,movieRecommend
from tuningBot import joke
from google import news


def handle(text,toUser):
    assert(text[0] == "@")
    text = text.replace("@","")

    help = ""
    ziyuan = ""
    gouliang = "很好奇你为什么要吃这种东西，我家大黄都不够吃，不给你！"

    if text == "0" or text.lower() == "help" or text == "帮助":
        return help
    #发福利的时候会有问题！
    elif text == "1" or text == "福利" or text == "老司机":
        itchat.send("",toUserName=toUser)
        return ""
    elif text == "2" or text == "对白":
        return duibai()
    elif text == "3" or text == "电影" or text == "电影推荐" or text == "movie":
        return movieRecommend()
    elif text == "4" or text == "笑话"  or text == "joke":
        return joke()
    elif text == "5" or text == "资源":
        return ziyuan
    elif text == "6" or text == "狗粮":
        return gouliang
    elif text == "7" or text == "新闻" or text.lowe() == "news":
        return news()
    else:
        return help

