from urllib import request
import urllib

def yt_re(words):
    search_keyword = words.replace(' ', '+')
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + search_keyword)
    video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    watch_links = []
    for video_id in range(10):
        watch_link = 'https://www.youtube.com/watch?v=' + video_ids[video_id]
        print(watch_link)
        watch_links.append(watch_link)

    return watch_links


yt_re(input('type some search keywords: '))
