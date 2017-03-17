import itchat
from pancRecommend import duibai,movieRecommend
from tuningBot import joke
from googleNews import news


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg['Text']
    toUser = msg["FromUserName"]
    if text[0] != "@":
        return ""
    text = text.replace("@","")
    help = "发送给我的文字前面加“@”会有特殊效果哟。例如“@1”，“@老司机”，“@福利”，有福利图哟；“@2”，“@对白”会有电影电视剧动漫经典对白；“@3”，“@电影”，“@电影推荐”，“@movie”会有推荐电影；“@4”，“@笑话”,“@joke”会有给你讲个笑话；“@6”，“@狗粮”会给你推送狗粮，“@7”，“@新闻”，“@news”会有今日谷歌焦点新闻；“@0”，“@帮助”，“@help”会返回帮助。欢迎调戏，拒绝勾搭！"
    ziyuan = "待续"
    gouliang = "（大雾）很好奇你为什么要吃这种东西，我家大黄都不够吃，不给你！"

    if text == "0" or text.lower() == "help" or text == "帮助":
        return help
    if text == "1" or text == "福利" or text == "老司机":
        itchat.send("",toUserName=toUser)
    if text == "2" or text == "对白":
        return duibai()
    if text == "3" or text == "电影" or text == "电影推荐" or text == "movie":
        return movieRecommend()
    if text == "4" or text == "笑话"  or text == "joke":
        return joke()
    if text == "5" or text == "资源":
        return ziyuan
    if text == "6" or text == "狗粮" or text=="周晓丽":
        return gouliang
    if text == "7" or text == "新闻" or text.lower() == "news":
        return news()
    return help


itchat.auto_login()
itchat.run()