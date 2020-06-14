import requests
import settings
import json


SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

# class YouTubeInfo:

#     def __init__(self, lookup_string):
#         self.lookup_string = lookup_string

def youtube_lookup_results(lookup_string):
    
    search_params = {
    'part' : 'snippet',
    'q' : lookup_string,
    'maxResults' : 10,
    'type' : 'video',
    'order' : 'relevance',
    'key' : settings.YOUTUBE_DATA_API_KEY
    }

    r = requests.get(SEARCH_URL, params = search_params)
    results = r.json()['items']
    video_id_list = []

    for result in results: 
        video_id_list.append(result['id']['videoId'])

    main_watch_url = "http://www.youtube.com/watch?v="

    video_links = []
    for id in video_id_list:
        video_links.append(main_watch_url +id)
 
    return video_links


def generate_video_link_file(top_videos):
    with open("video-links.txt", "w") as videos_links:
        for video in top_videos:
            videos_links.write(video +"\n")
    return 


look_up = input("What would you like to look up?")
top_ten_videos = youtube_lookup_results(look_up)
generate_video_link_file(top_ten_videos)


