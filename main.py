#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from random import randint
import time

default_link = 'https://prnt.sc/'
count = 100 # images count

# Creating link
def get_full_link():
    str = default_link
    for i in range(0, 6):
        tempI = randint(0, 1)
        if tempI == 0:
            str += chr(randint(48, 57))
        elif tempI == 1:
            str += chr(randint(97, 122))

    return str

# Getting html by link
def get_html(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    temp = requests.get(link, headers=headers)
    if (temp.status_code == 200):
        web_page = temp

        return web_page.text
    else:
        return "Error"

# Getting link to image from html source
def get_image_link(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    img_link = soup.find('img', class_='no-click screenshot-image')
    img_link = img_link['src']

    return img_link

link = get_full_link()

for i in range(1, count):
    try:
        link = get_full_link()
        html_text = get_html(link)

        if html_text == "Error":
            continue

        time.sleep(0.03)

        image = requests.get(get_image_link(html_text))


        image_file = open('images/img' + str(i) + '.png', 'wb')
        image_file.write(image.content)
        image_file.close()


        procent = i % count

        print (str(procent) + '%')
        time.sleep(0.1)

    except:
        continue

print ("Done.")