import requests
import settings
import json

class YouTubeInfo:
    SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

    def __init__(self, lookup_string):
        self.lookup_string = lookup_string
        self.youtube_search(self.lookup_string)

    def new_lookup_string(lookup_string):
        """
        new_lookup_string methd to change the lookup string.

        Args:
            lookup_string (str): new search string in case the user wants to change their search
        """
        self.lookup_string = lookup_string
        self.youtube_search(self.lookup_string)

    def youtube_search(self, lookup_string):
        """
        youtube_search This uses the YouTube Data API to look for the top videos results
                       for a given string

        Args:
            lookup_string (str): What the user wants to search youtube for

        Returns:
            list : a list of the top videos for a given search. 
        """

        search_params = {
        'part' : 'snippet',
        'q' : lookup_string,
        'maxResults' : 10,
        'type' : 'video',
        'order' : 'relevance',
        'key' : settings.YOUTUBE_DATA_API_KEY
        }

        r = requests.get(self.SEARCH_URL, params = search_params)
        results = r.json()['items']
        video_id_list = []

        for result in results: 
            video_id_list.append(result['id']['videoId'])

        main_watch_url = "http://www.youtube.com/watch?v="

        video_links = []
        for id in video_id_list:
            video_links.append(main_watch_url +id)

        self.generate_video_link_file(video_links)

        return video_links

    def generate_video_link_file(self, top_videos):
        """
        generate_video_link_file This generates a file named video-links.txt Where we store
                                 the links for the latest YouTube search

        Args:
            top_videos (list): a list of the top YouTube search results for the given lookup string
        """ 
        with open("video-links.txt", "w") as videos_links:
            for video in top_videos:
                videos_links.write(video +"\n")
        return 






