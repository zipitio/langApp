import webscraper
import aiprompting

def main():
    # check_api_key()
    # prompt = aipromting.user_input()
    # aipromting.prompt_ai(prompt)
    # webscraper.scrapeVocab()

    all_links = webscraper.get_all_vocab_links()
    webscraper.get_all_vocab(all_links)



if __name__ == '__main__':
    main()

