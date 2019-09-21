import requests
from bs4 import BeautifulSoup

def main():
    for i in range(12):      # Number of pages plus one
        url = "http://www.bruceleequotes.org/page/{}".format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        # Second argument is for 'append'. Running the script twice or more in succession will duplicate the quotes. 
        quotesFile = open('quotes.txt', 'a', encoding='utf-8')

        for l in soup.find_all('h2', class_='title'):
            quotesFile.write(l.text)
            quotesFile.write('\n')
            print(l.text)

        quotesFile.close()

if __name__ == "__main__":
    main()