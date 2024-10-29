import requests
from bs4 import BeautifulSoup
import re
import base64
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
            response.raise_for_status()
            html_pages.append(response.text)
            print(f"Berhasil mengambil konten dari {url}")
        except requests.RequestException as e:
            print(f"Gagal mengakses {url}: {e}")
    return html_pages

# Ekstraksi kode dari setiap halaman HTML dengan regex
def extract_codes(pages):
    codes = []
    vless_pattern = r"vless://[^\s]+"
    vmess_pattern = r"vmess://[^\s]+"

    for page in pages:
        soup = BeautifulSoup(page, 'html.parser')
        page_text = soup.get_text()

        # Cari link vless
        vless_links = re.findall(vless_pattern, page_text)
        codes.extend(vless_links)

        # Cari link vmess
        vmess_links = re.findall(vmess_pattern, page_text)
        for link in vmess_links:
            # Decode VMESS link jika dienkripsi dalam base64
            if link.startswith("vmess://"):
                try:
                    base64_content = link[8:]
                    decoded_link = base64.b64decode(base64_content).decode('utf-8')
                    codes.append(decoded_link)
                except Exception as e:
                    print(f"Error decoding VMESS link: {e}")
                    continue

    return remove_duplicates(codes)

# Siapkan penanda waktu untuk config
def generate_timestamp():
    current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    formatted_date = current_date_time.strftime("%b-%d | %H:%M")
    return f"#✅ {formatted_date}-"

# Proses dan simpan kode dalam file
def save_codes(codes, filename="config.txt"):
    if not codes:
        print("Tidak ada kode yang ditemukan untuk disimpan.")
        return
    
    timestamp = generate_timestamp()
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for i, code in enumerate(codes):
                if i == 0:
                    config_string = "#Updated " + timestamp + " | New config every 1 hour"
                else:
                    config_string = f"#Akun_{i} @Sonzaix"
                config_final = f"{code} {config_string}"
                file.write(config_final + "\n")
        print(f"Berhasil menyimpan kode ke {filename}")
    except IOError as e:
        print(f"Gagal menyimpan file: {e}")

# Eksekusi seluruh proses
html_pages = fetch_html_content(webpage_addresses)
codes = extract_codes(html_pages)
save_codes(codes)
