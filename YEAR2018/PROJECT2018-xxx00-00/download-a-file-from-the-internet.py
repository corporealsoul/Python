# import urllib.request
from urllib import request

file_url = r"https://docs.python.org/3/library/urllib.request.html" # r means raw string

def download_file_information(url):
    # Open the url file
    fileOpen = request.urlopen(url)