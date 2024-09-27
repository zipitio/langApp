import requests, bs4

def scrapeVocab(link, words):
    #download webpage
    res = requests.get(link)
    res.raise_for_status()

    #create beautiful soup object
    frenchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    #Get page title
    title = frenchSoup.select('h1')

    #get page words
    vocabWords = frenchSoup.select('span[class="txt--lang-foreign"]')

    #test
    #print(type(vocabWords))
    #print(len(vocabWords))

    for word in vocabWords:
        #Create dictionary
        words[title] = word.getText()

def get_all_vocab_links():
    res = requests.get("https://french.kwiziq.com/learn/theme")
    res.raise_for_status()

    #create beautiful soup object
    frenchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    vocab_pages_html = frenchSoup.select('a[class="list-style__link"]')

    #print(len(vocab_pages_html))

    #extract links
    extracted_links = []
    for link in vocab_pages_html:
        extracted_links.append(link.attrs['href'])

    #print(len(extracted_links))

    return extracted_links

def get_all_vocab(all_links):
    all_words = {}
    links = get_all_vocab_links()

    #iterate through links and add words to word dict
    for link in links:
        scrapeVocab(link, all_words)

    print(all_words)





