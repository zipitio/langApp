import requests, bs4

def scrapeVocab():
    #download webpage
    res = requests.get("https://french.kwiziq.com/learn/theme/128")
    res.raise_for_status()

    #create beautiful soup object
    frenchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    print(type(frenchSoup))
    vocabWords = frenchSoup.select('span[class="txt--lang-foreign"]')
    print(type(vocabWords))
    print(len(vocabWords))

    for word in vocabWords:
        print(word.getText())

    return

def get_all_vocab_links():
    res = requests.get("https://french.kwiziq.com/learn/theme")
    res.raise_for_status()

    #create beautiful soup object
    frenchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    vocab_pages_html = frenchSoup.select('a[class="list-style__link"]')



    print(len(vocab_pages_html))

    extracted_links = []
    for link in vocab_pages_html:
        extracted_links.append(link.attrs['href'])

    print(len(extracted_links))




