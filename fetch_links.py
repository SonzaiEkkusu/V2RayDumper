import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Konfigurasi untuk headless Chrome di GitHub Action
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

URL = "https://t.me/s/freecfgalloperator"
OUTPUT_FILE = 'config.txt'

def fetch_links():
    # Inisialisasi WebDriver dengan opsi headless untuk GitHub Actions
    service = Service("/usr/local/bin/chromedriver")  # Lokasi default untuk GitHub Action
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(URL)
    time.sleep(5)  # Tunggu halaman termuat

    # Gulir beberapa kali untuk memuat lebih banyak pesan
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Tunggu agar halaman termuat setiap kali scroll

    # Ambil teks dari seluruh halaman
    page_source = driver.page_source
    driver.quit()

    # Ekstrak link dengan pola regex untuk vmess, vless, dan trojan
    pattern = r'(vmess://[^\s]+|vless://[^\s]+|trojan://[^\s]+)'
    links = re.findall(pattern, page_source)

    # Simpan link ke file config.txt
    with open(OUTPUT_FILE, 'w') as file:
        for link in links:
            file.write(link + '\n')
    print(f"Links disimpan di {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_links()
