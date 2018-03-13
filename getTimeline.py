#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import config  # 標準のjsonモジュールとconfig.pyの読み込み
import time
import datetime
from requests_oauthlib import OAuth1Session  # OAuthのライブラリの読み込み


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理
upload_discord = []

list_url = "https://api.twitter.com/1.1/lists/statuses.json?list_id=972059926083203074&include_rts=False"
params = {'count': 10}  # 取得数
res = twitter.get(list_url, params=params)


def reserch_twitter():
    res = twitter.get(list_url, params=params)
    if res.status_code == 200:  # 正常通信出来た場合
        timelines = json.loads(res.text)#  レスポンスからタイムラインリストを所得
        for tweet in timelines:  # タイムラインリストをループ処理
            if tweet ['text'].find('参戦ID') >-1 and  tweet['text'].find( ':参加者募集！' ) -1:  
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                if tweet['created_at'] not in upload_discord :  
                  upload_discord.append(tweet['created_at'])
                  discode_up()
                    #  discodeにアップロード 
    else:  # 正常通信出来なかった場合
        print("Failed. : %d"% res.status_code)

def discode_up():
    print("実装して")

def main():
    start_time = time.perf_counter()
    last_gettime = time.perf_counter() - 8
    while True:
        print(start_time)
        if time.perf_counter() > last_gettime + 8 :
            last_gettime = time.perf_counter()
            reserch_twitter()
        else:
            time.sleep(1)


if __name__ == '__main__':
    main()
