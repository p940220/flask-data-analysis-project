import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_dynamic_site(url):
    driver = init_driver()
    try:
        driver.get(url)
        time.sleep(3) # 等待動態內容加載
        
        # 範例：獲取所有標題
        titles = driver.find_elements(By.TAG_NAME, "h2")
        results = []
        for title in titles:
            results.append({
                "title": title.text,
                "url": url,
                "crawl_date": time.strftime("%Y-%m-%d %H:%M:%S")
            })
        return results
    finally:
        driver.quit()

if __name__ == "__main__":
    target_url = "https://example.com" # 替換為實際目標
    data = scrape_dynamic_site(target_url)
    print(data)
