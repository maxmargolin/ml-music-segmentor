__author__ = "Max Margolin, margolinmax@gmail.com"

"""
handle downloads
"""

import youtube_dl
from selenium import webdriver

VIDEO_ID = "kTHNpusq654"

def download_from_url(video_url, filename_of_download):
    """
    basically youtube2mp3
    :param video_url: url of video to download
    :param filename_of_download: <-
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': (filename_of_download + '.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def youtube_id_to_url(yt_video_id):
    """
    Add the video ID to the video url format
    :param yt_video_id: the video id
    :return:  full url that has the video
    """
    return 'https://www.youtube.com/watch?v=' + yt_video_id

def get_browser():
    """
    :return: a selenium driver
    """
    return  webdriver.Chrome(executable_path="chromedriver.exe")

def browser_url_to_title(driver):
    """
    get title from the currently open page in the browser
    :param driver: most likely open on a video
    :return: title of the page, probably the video title
    """
    return driver.title

def filter_name(og_title):
    """
    filter too long page title to something a user would search for
    :param og_title: name to filter
    :return: name that is searchable
    """

    # TODO: better cleanup

    song_name =  og_title.split("(")[0]
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789')
    symbolless_title = ''.join(filter(whitelist.__contains__, song_name))
    return symbolless_title

def get_current_song_name(driver):
    """
    Browser is open on a video,
    page title is video name ("katy perry - hot n cold (music video)..."),
    get the actual name of the song ("katy perry  hot n cold")
    :param driver: the already open browser
    :return: filtered name ready to search
    """
    full_title = browser_url_to_title(driver)
    filtered_name = filter_name(full_title)
    return filtered_name

def get_lyrics_url(non_lyrics_url,driver=None):
    """

    :param driver: not required
    :param non_lyrics_url: url of original video
    :return: the url of a video for the same song but with lyrics so it's just talking
    """
    if not driver:
        driver = get_browser()
    driver.get(non_lyrics_url)
    song_name = get_current_song_name(driver)
    search_url = "https://www.youtube.com/results?search_query=" + song_name + " lyrics"
    driver.get(search_url)
    driver.find_element_by_id("video-title").click()
    return driver.current_url


# get sound files of this and of the lyrical video

original_video_url = youtube_id_to_url(VIDEO_ID)
download_from_url(original_video_url,"og")
lyrics_video_url =  get_lyrics_url(original_video_url)
download_from_url(lyrics_video_url,"lyrical")


