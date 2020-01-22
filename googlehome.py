#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pychromecast
import glob
import os


def select_file():
    list_of_files = glob.glob('/Users/akiho/wip/*.wav')
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file = os.path.basename(latest_file)
    return latest_file


if __name__ == "__main__":
    latest_file = select_file()
    print(latest_file)

    mp3url = 'https://web.sfc.keio.ac.jp/~s18779ay/googlehome/'+latest_file


    #googlehomeを探す
    chromecasts = pychromecast.get_chromecasts()

    if len(chromecasts) == 0:
        print("Google Homeが見つかりませんω")
        exit()

    #固定で1個目を使う
    googleHome = chromecasts[0]

    if not googleHome.is_idle:
        print("Killing current running app")
        googleHome.quit_app()
        time.sleep(5)

    #喋らせる
    googleHome.wait()
    googleHome.media_controller.play_media(mp3url, 'audio/mp3')
    googleHome.media_controller.block_until_active()
