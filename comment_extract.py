import json
import sys
from urllib import *
import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import  urlopen
import pandas as pd
import re

YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
key = "AIzaSyDk7_07DXXrZyqOocsw58DZO2Sn42TDl9U"

def load_comments(mat, data):

        for item in mat["items"]:
            comment = item["snippet"]["topLevelComment"]
            author = comment["snippet"]["authorDisplayName"]
            text = comment["snippet"]["textDisplay"]
            #print("Comment by {}: {}".format(author, text))
            data[author] = text

def openURL(url, parms):
        f = urlopen(url + '?' + urlencode(parms))
        data = f.read()
        f.close()
        matches = data.decode("utf-8")
        return matches

def get_video_comment(videourl, maxR):
            
        data = {}

        mxRes = 50
        vid = str()

        try:
            video_id = urlparse(str(videourl))
            q = parse_qs(video_id.query)
            vid = q["v"][0]

        except:
            print("Invalid YouTube URL")

        parms = {
                    'part': 'snippet,replies',
                    'maxResults': maxR,
                    'videoId': vid,
                    'textFormat': 'plainText',
                    'key': key
                }



        matches = openURL(YOUTUBE_COMMENT_URL, parms)
        i = 0
        mat = json.loads(matches)
        nextPageToken = mat.get("nextPageToken")
        #print("\nPage : 1")
        #print("------------------------------------------------------------------")
        load_comments(mat, data)

        while i < mxRes and nextPageToken:
            parms.update({'pageToken': nextPageToken})
            matches = openURL(YOUTUBE_COMMENT_URL, parms)
            mat = json.loads(matches)
            nextPageToken = mat.get("nextPageToken")
            #print("\nPage : ", i)
            #print("------------------------------------------------------------------")

            load_comments(mat, data)

            i += 1
            
        df = pd.DataFrame(list(data.items()))

        print(df.shape)

        df.to_csv('Comments.csv', index = False)

def remove_emoji(string):
	emoji_pattern = re.compile("["
	                   u"\U0001F600-\U0001F64F"  # emoticons
	                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
	                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
	                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
	                   u"\U00002702-\U000027B0"
	                   u"\U000024C2-\U0001F251"
	                   "]+", flags=re.UNICODE)
	return emoji_pattern.sub(r'', string)


def get_clean_data():
	data = pd.read_csv('Comments.csv')
	data= data.dropna()
	clean_texts = []

	for text in data['1']:
	    text = remove_emoji(text)
	    clean_texts.append(text)

	data['text'] = clean_texts
	data = data.drop(['0','1'], axis = 1)

	data.to_csv('Comments.csv', index = False)

def get_comments(url):

	maxR = 100
	get_video_comment(url, maxR)
	get_clean_data()
	    

