from requests.exceptions import URLRequired
#from bs4 import BeautifulSoup
import bs4
import requests
import codecs

def get_url_list(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    url_list = []
    list = soup.select("#list > dl > dd > a")
    for i in list:
        i = i.get("href")
        i = 'http://www.biqugecom.com' + i
        url_list.append(i)
    url_list = url_list[9:-1]
    print(url_list)
    return url_list

def get_data(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    fo = codecs.open('output.txt', 'a+', 'utf-8')
    section_name = soup.select("#wrapper > div.content_read > div > div.bookname > h1")[0].text
    print(section_name)
    fo.write('\r\n' + section_name + '\r\n')
    section_text = soup.select("#contect")
    for x in section_text:
        a = x.text.replace('readx();', '').replace('www.biqugecom.com/75/75224', '')
        fo.write((a) + '\r\n')
    fo.close()

if '__main__' == __name__:
    url = 'https://www.biqugesc.com/75/75224/'
    url_list = get_url_list(url)
    for n in url_list:
        get_data(n)


