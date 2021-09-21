import urllib.request, os, re
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('YT-API-KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
result_number = 0


def yt_api_search(words):
    results = 4
    request = youtube.search().list(
        part='snippet',
        q=words,
        maxResults=results,
    )

    response = request.execute()

    watch_links = []
    for item in response['items']:
        watch_link = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
        # print(watch_link)
        watch_links.append(watch_link)

    return watch_links


# request = youtube.search().list(
#     part='snippet',
#     q='placebo james',
#     maxResults=10,
# )
#
# response = request.execute()
#
# for item in response['items']:
#     print(item['id']['videoId'])
