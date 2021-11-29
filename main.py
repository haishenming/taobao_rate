import requests
import re

url = "https://rate.taobao.com/feedRateList.htm"

# 头部需要带上ua和referer，不然请求不到参数
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'referer': 'https://item.taobao.com/item.htm?id=598886968545&ali_trackid=2:mm_12238993_19794510_110896800135:1638093374_232_1624932754&union_lens=lensId:OPT@1638091627@067007a5-1158-43e4-a35e-d900207083e0_598886968545@1;recoveryid:201_11.11.158.245_13422117_1638091626709;prepvid:201_11.11.158.245_13422117_1638091626709&spm=a231o.13503973.20618785.2&pvid=067007a5-1158-43e4-a35e-d900207083e0&scm=1007.16016.217477.0&bxsign=tbkbB4vqU+r5RQTy6hyxM4zHaDQA/pu7Li1q7uVIlVzo8ojqTxhg+ecs4040TGiZ+AuIOhsAauM5ydqMHStzognz5PLxCYmFEIZnQz8iKdNEcw='
}

# 之前复制的cookie
cookies = {
    "_samesite_flag_": "true",
    "cookie2": "1f8b3894e4cf452135978d40657c6a74",
    "t": "bf3844f151ea6793e6c09e7ee148ca8f",
    "_tb_token_": "315898307573e",
    "thw": "cn",
    "xlly_s": "1",
    "UM_distinctid": "17d65c9caa695f-0987249418573d-1f396452-1ea000-17d65c9caa7ab8",
    "sgcookie": "E1001lHyzSBBYLjyzXqnnenaUgnpMORtekV3nifC3cNHX3jav0H5W4MX0%2FBZgdwGN4VP6065H3PJkRPmPv5z1%2FYO2HplKDtJ0JWkoXYatJNwslg%3D",
    "_m_h5_tk": "cb5b749d78be0269e7711d4841a9d86f_1638100933539",
    "_m_h5_tk_enc": "49f66742a296ffd0736d389e4a7becbc",
    "lLtC1_": "1",
    "enc": "oTUYe%2BR6Pph11LD7Zuf2K6dB%2BOxC6lPSn0y2Nb9XGqPjjK8OTmvrmEQkhEx2QFJV3OrXmjpgL6ShJAu6vqGoyA%3D%3D",
    "hng": "CN%7Czh-CN%7CCNY%7C156",
    "mt": "ci=0_0",
    "tracknick": "",
    "cna": "dMgPGhFdUE8CAXdUnhXPcZOX",
    "tfstk": "cWRAB74e_4UA4N_J8KHk15U0ILdOaYzAVrsa64sb1SotyDVT1sXJtBE0Ix_OYi3R.",
    "l": "eBTtqlJlg-tOa4sUBOfZKurza779MIRfBuPzaNbMiOCP_0C65KLhW6IDlFTBCnhVH6z9R3leTTy0BzYeIP5J-D_BkYyA6q1q3dC..",
    "isg": "BC8v9AvtkgVfLJY5dzealh5tvkU51IP2bugCqkG8uh6hkE6SSaWbRhAGE4CuqVtu"
}

params = {
    # 这两个参数用于定位店铺
    'auctionNumId': '598886968545',
    'userNumId': '300463178',
    # 获取第几页评论
    'currentPageNum': 1,
    # 每页返回多少条评论
    'pageSize': '20',
}

if __name__ == '__main__':
    res = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(exec(res.text[3:-2]))
