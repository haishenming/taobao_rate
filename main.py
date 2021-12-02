import requests
import re
import json

cookie = "_samesite_flag_=true; cookie2=1f8b3894e4cf452135978d40657c6a74; t=bf3844f151ea6793e6c09e7ee148ca8f; _tb_token_=315898307573e; thw=cn; UM_distinctid=17d65c9caa695f-0987249418573d-1f396452-1ea000-17d65c9caa7ab8; sgcookie=E1001lHyzSBBYLjyzXqnnenaUgnpMORtekV3nifC3cNHX3jav0H5W4MX0%2FBZgdwGN4VP6065H3PJkRPmPv5z1%2FYO2HplKDtJ0JWkoXYatJNwslg%3D; enc=oTUYe%2BR6Pph11LD7Zuf2K6dB%2BOxC6lPSn0y2Nb9XGqPjjK8OTmvrmEQkhEx2QFJV3OrXmjpgL6ShJAu6vqGoyA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_0; tracknick=; cna=dMgPGhFdUE8CAXdUnhXPcZOX; _m_h5_tk=a05e80d65c1c3818428f9ed24a4548f3_1638199113604; _m_h5_tk_enc=4a7570bea8d402ccb59fa6c8e0ee524c; xlly_s=1; miid=4412439671428979900; lLtC1_=1; tfstk=cJSRB_MNY-H8NLpAQaUcAWnBqSwGw4HJGYOEv-OiEezySI1c6GjtZ24WpCR8H; l=eBTtqlJlg-tOaRXvKOfwourza77OSIRAguPzaNbMiOCPOHfp52b5W6I8fAT9C3GVhst6R3leTTy0BeYBcI0YB53Ee5DDwQHmn; isg=BCcnCNOrCpqIJI4Rrx8SPka1tl3xrPuOJkD6QvmUQ7bd6EeqAXyL3mXuCuj2ANMG"

url = "https://rate.taobao.com/feedRateList.htm"

# 头部需要带上ua和referer，不然请求不到参数
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'referer': 'https://item.taobao.com/item.htm?id=598886968545&ali_trackid=2:mm_12238993_19794510_110896800135:1638093374_232_1624932754&union_lens=lensId:OPT@1638091627@067007a5-1158-43e4-a35e-d900207083e0_598886968545@1;recoveryid:201_11.11.158.245_13422117_1638091626709;prepvid:201_11.11.158.245_13422117_1638091626709&spm=a231o.13503973.20618785.2&pvid=067007a5-1158-43e4-a35e-d900207083e0&scm=1007.16016.217477.0&bxsign=tbkbB4vqU+r5RQTy6hyxM4zHaDQA/pu7Li1q7uVIlVzo8ojqTxhg+ecs4040TGiZ+AuIOhsAauM5ydqMHStzognz5PLxCYmFEIZnQz8iKdNEcw=',
    'cookie': cookie,
}

params = {
    # 这两个参数用于定位店铺
    'auctionNumId': '555049996089',
    'userNumId': '704859967',
    # 获取第几页评论
    'currentPageNum': 2,
    # 每页返回多少条评论
    'pageSize': '20',
    'callback': 'json'
}

if __name__ == '__main__':
    res = requests.get(url, headers=headers, params=params)
    s = re.search("json\((.*)\)", res.text)
    rdata = json.loads(s.group(1))

    print(res.text)
