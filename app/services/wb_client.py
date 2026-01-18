from selenium.webdriver.common.by import By

from app.core.config import WB_PARSING_BASE_URL, MAX_PAGES
from app.services.parser import start_driver, scroll_page


def search_links(driver):
    cards = driver.find_elements(By.CSS_SELECTOR, "article.product-card a.product-card__link")
    links = []
    for card in cards:
        links.append(card.get_attribute("href"))
        if len(links) >= MAX_PAGES:
            break
    return links

def get_info_page(driver, link):
    driver.get(link)
    scroll_page(driver)
    info = {'url': link}

    article = driver.find_element(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[2]/div[3]/div/div/table/tbody/tr[1]/td/button/span')
    info['article'] = article.text

    name = driver.find_element(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/h3')
    info['name'] = name.text

    price = driver.find_element(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[3]/div/div/div[1]/div/div/div/div/div/span[1]/ins')
    info['price'] = price.text

    # description = driver.find_element(By.XPATH, '')
    # info['description'] = description.text

    info['images'] = []
    images = driver.find_elements(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div[2]/img')
    for image in images:
        info['images'].append(image.get_attribute("src"))

    # characteristic = driver.find_element(By.XPATH, '')
    # info['characteristic'] = characteristic.text

    seller_name = driver.find_element(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[3]/div/div/div[5]/section/div/div/div/a/div[2]/div/div/span[1]')
    info['seller_name'] = seller_name.text

    seller_link = driver.find_element(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[3]/div/div/div[5]/section/div/div/div/a')
    info['seller_link'] = WB_PARSING_BASE_URL + seller_link.get_attribute("href")

    info['sizes'] = []
    sizes = driver.find_elements(By.XPATH, '//*[@id="reactContainers"]/div[2]/div/div[3]/div[2]/div[2]/div[2]/ul/li[1]/button')
    for size in sizes:
        info['sizes'].append(size.text)

    # left_items = driver.find_element(By.XPATH, '')
    # info['left_items'] = left_items.text

    rating = driver.find_element(By.XPATH, '//*[@id="product-feedbacks"]/div[2]/div[1]/div[1]/div[1]/b')
    info['rating'] = rating.text

    reviews_amount = driver.find_element(By.XPATH, '//*[@id="product-feedbacks"]/div[2]/div[1]/div[1]/a')
    info['reviews_amount'] = reviews_amount.text

    return info

def get_search_results(search):
    driver = start_driver()
    driver.get(f"{WB_PARSING_BASE_URL}/catalog/0/search.aspx?search={search}")
    scroll_page(driver)
    links = search_links(driver)
    for link in links:
        print(get_info_page(driver, link))
    driver.quit()


