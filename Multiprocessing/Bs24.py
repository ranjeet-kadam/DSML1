from bs4 import BeautifulSoup
import threading
import requests

urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/tutorials/',
    'https://python.langchain.com/docs/concepts/'
]

def fetch_cont(url):
    response = requests.get(url,verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_cont, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All the pages are fetched.")
