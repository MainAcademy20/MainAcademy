"""
Задача: распарсить ссылки  из блока Новостей на сайте i.ua
(все ссылки в блоке <div class="news"> ... </div>)

Пример HTML кода ссылки
<a rel="nofollow" target="_blank"
onclick="trackNewsClick('Comments.ua')"
href="https://news.i.ua/click/6598357/331318064/2">

Верховная Рада переходит на электронный документооборот

</a>
"""

import requests
from html.parser import HTMLParser


class IUAParser(HTMLParser):
    enabled = False
    div_depth = 0
    link_list = []

    def handle_starttag(self, tag, attrs):
        attrdict = dict(attrs)
        if self.enabled and tag == 'a':
            self.link_list.append(attrdict['href'])
        if self.enabled and tag == 'div':
            self.div_depth += 1
        if tag == 'div' and attrdict.get('class') == 'news':
            self.enabled = True

    def handle_endtag(self, tag):
        if self.enabled and self.div_depth == 0 and tag == 'div':
            self.enabled = False
        if tag == 'div' and self.enabled:
            self.div_depth -= 1


if __name__ == '__main__':
    parser = IUAParser()
    iua = requests.get('https://i.ua')
    html = iua.text
    parser.feed(html)

    news = parser.link_list[:-3]
    news_unique = set(news)
    print(len(news_unique))
