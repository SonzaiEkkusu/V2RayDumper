import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import jdatetime

# List alamat web
webpage_addresses = [
    "https://t.me/s/freecfgalloperator"
]

# Fungsi untuk menghapus duplikasi dengan menggunakan set
def remove_duplicates(input_list):
    return list(set(input_list))

# Ambil halaman HTML dari setiap URL dan kumpulkan teks di dalam tag <code>
def fetch_html_content(urls):
    html_pages = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Tambah penanganan error
            html_pages.append(response.text)
        except requests.RequestException as e:
            print(f"Gagal mengakses {url}: {e}")
    return html_pages

# Ekstraksi kode dari setiap halaman HTML
def extract_codes(pages):
    codes = []
    for page in pages:
        soup = BeautifulSoup(page, 'html.parser')
        code_tags = soup.find_all('code')
        
        for code_tag in code_tags:
            code_content = code_tag.text.strip()
            if any(proto in code_content for proto in ["vless://", "vmess://", "trojan://"]):
                codes.append(code_content)
    return remove_duplicates(codes)

# Siapkan penanda waktu untuk config
def generate_timestamp():
    current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    formatted_date = current_date_time.strftime("%b-%d | %H:%M")
    return f"#✅ {formatted_date}-"

# Proses dan simpan kode dalam file
def save_codes(codes, filename="config.txt"):
    timestamp = generate_timestamp()
    with open(filename, "w", encoding="utf-8") as file:
        for i, code in enumerate(codes):
            if i == 0:
                config_string = "#Updated " + timestamp + " | New config every 1 hour"
            else:
                config_string = f"#Akun_{i} @Sonzaix"
            config_final = f"{code} {config_string}"
            file.write(config_final + "\n")

# Eksekusi seluruh proses
html_pages = fetch_html_content(webpage_addresses)
codes = extract_codes(html_pages)
save_codes(codes)
