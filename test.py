import requests
from bs4 import BeautifulSoup
import csv
import time
from concurrent.futures import ThreadPoolExecutor

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "X-Amzn-Trace-Id": "Root=1-65c58daf-3a2c6c3a7adb35726b652acb"
}

def get_product_links_amazon(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    a_tag = soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    
    product_link_list = []
    for tag in a_tag:
        href = tag.get('href', '')
        # Check if href is a complete URL or a relative path
        if href.startswith('http'):
            product_link_list.append(href)
        else:
            # Ensure it's a relative path and prepend the base URL
            product_link_list.append('https://www.amazon.com' + href)
            
    return product_link_list


def get_product_data_amazon(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id='productTitle').get_text().strip() if soup.find(id='productTitle') else 'N/A'
    price = soup.find('span', class_='a-offscreen').get_text().strip() if soup.find('span', class_='a-offscreen') else 'N/A'
    rating = soup.find('span', id='acrCustomerReviewText').get_text().strip() if soup.find('span', id='acrCustomerReviewText') else 'N/A'
    score = soup.find('span', class_='a-icon-alt').get_text().strip() if soup.find('span', class_='a-icon-alt') else 'N/A'
    review_summary = 'N/A'  # Amazon pages usually don't have an element with id='product-summary'

    return [url, title, price, rating, score, review_summary]

def main():
    start = time.time()
    link = 'https://www.amazon.com/s?k=razer+mouse'
    product_links = get_product_links_amazon(link)

    categories = ['URL', 'Title', 'Price', 'Ratings', 'Score', 'Review Summary']
    with open('scrape.csv', 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(categories)

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(get_product_data_amazon, product_links)
            for data in results:
                writer.writerow(data)
    end = time.time()
    print(end-start)
if __name__ == "__main__":
    main()
