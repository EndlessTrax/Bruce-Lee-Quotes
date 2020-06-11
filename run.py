import requests
from bs4 import BeautifulSoup


def main():
    for i in range(12):  # Number of pages plus one
        url = "http://www.bruceleequotes.org/page/{}".format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        with open("quotes.txt", "a", encoding="utf8") as quotesFile:
            for l in soup.find_all("h2", class_="title"):
                quotesFile.write(f"{l.text}\n")
                print(f"Adding: {l.text}")


if __name__ == "__main__":
    main()
