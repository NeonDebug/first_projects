from bs4 import BeautifulSoup as BS4
import shutil
import urllib.parse
import requests

def get_page(phrase, page):
    link = "https://www.istockphoto.com/ru" + phrase
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    params = {"page": page, "phrase": phrase, "sort": "mostpopular"}
    request = requests,get(link, headers = headers, params = params)
    return request.text
def is_404(html):
    page = BS4(html, "html.parser")
    if len(page.select("img.gallery-asset__thumb")) < 0:
        return True
    return False
def get_imgs_from_page(phrase, page):
    html = get_page(phrase, page)
    images =[]
    if is_404(html)==True:
        return False
    img_node = BS4(html, "html.parser")
    imgs = img_node.select("img.gallery-asset__thumb")
    for img in imgs:
        if img.has_attr("src"):
            print(f"Photo url: {img['src']}")
            images.append(img["src"])
    return images
def get_images(query, pages):
    num_of_page = i + 1
    img = get_imgs_from_page(query, num_of_page)