import requests, bs4
import sqlite3

conn = sqlite3.connect('databases/french_vocab.db')
c = conn.cursor()

def scrapeVocab(link, words):
    #download webpage
    res = requests.get(link)
    res.raise_for_status()

    #create beautiful soup object
    frenchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    #Get page title
    title = frenchSoup.select('h1')[0].getText()

    #get page words
    vocabWords = frenchSoup.select('span[class="txt--lang-foreign"]')

    #test
    #print(type(vocabWords))
    #print(len(vocabWords))

    #add all page words to dict
    for word in vocabWords:
        #Create dictionary
        #words[word.getText()] = title

        #insert into db: word, topic, level
        c.execute('''INSERT INTO frenchvocab VALUES(?,?,?)''', (words.getText(), title, 0))


def get_all_vocab_links():
    res = requests.get("https://french.kwiziq.com/learn/theme")
    res.raise_for_status()

    #create beautiful soup object
    frenchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    vocab_pages_html = frenchSoup.select('a[class="list-style__link"]')

    #testing with limited list
    #vocab_pages_html = vocab_pages_html[0:5]

    print("Number of pages: " + str(len(vocab_pages_html)))

    #extract links
    extracted_links = []
    for link in vocab_pages_html:
        full_link = "https://french.kwiziq.com" + link.attrs['href']
        extracted_links.append(full_link)

    #print(len(extracted_links))

    return extracted_links

def get_all_vocab(all_links):
    all_words = {}

    #iterate through links and add words to word dict
    for link in all_links:
        scrapeVocab(link, all_words)

    for k,v in all_words.items():
        print(k + v)

    #print(len(all_words))

    conn.commit()
    conn.close()




