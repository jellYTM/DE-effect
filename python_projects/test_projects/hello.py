def main():
    print("Hello from test-projects!")


if __name__ == "__main__":
    main()

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())