import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                  "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }

    req = requests.get(url, headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")


get_data("https://www.nike.com/w/mens-shoes-nik1zy7ok")
