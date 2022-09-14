# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:31:06 2022

@author: AllenKll
"""

""" 
Must create a local 'config.py' with your google API key in it:
api_key = "YOUR_API_KEY"
"""    

import requests
import config

def get_video_title(video_id):

    try:
        r = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={video_id}&key={config.api_key}",timeout=5)
    except:
        print("Encountered an error with youtube.")
        return "UNKNOWN - Youtube connection porblem"

    if r.status_code != 200:
        return f"UNKNOWN - Youtube Error {r.status_code}"
    
    items = r.json()["items"]
    for item in items:
        if item["id"]["kind"] != "youtube#video": continue
        if item["id"]["videoId"]== video_id:
            return(item["snippet"]["title"])
    
    return "UNKNOWN - Possibly Unlisted"

if __name__ == "__main__":
    print(get_video_title("dQw4w9WgXcQ"))