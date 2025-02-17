import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime

old_webpage_addresses = [
    "https://t.me/s/v2ray_configs_pool",
    "https://t.me/s/XpnTeam",
    "https://t.me/v2rayNGcloud",
    "https://t.me/s/ZibaNabz",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/V_2rey",
    "https://t.me/s/V2ray_Alpha",
    "https://t.me/s/PROXY_MTM",
    "https://t.me/s/SiNABiGO",
    "https://t.me/s/v2rayng12023",
    "https://t.me/s/vlessconfig",
    "https://t.me/s/piazshekan",
    "https://t.me/s/Free_Internet_Iran",
    "https://t.me/s/ARv2ray",
    "https://t.me/s/VPNCUSTOMIZE",
    "https://t.me/s/UnlimitedDev",
    "https://t.me/s/MARAMBASHI",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/client_proo",
    "https://t.me/s/nufilter",
    "https://t.me/s/icv2ray",
    "https://t.me/s/Vpn_Mikey",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/kingspeedchanel",
    "https://t.me/s/VPN_Xpace",
    "https://t.me/s/SVNTEAM",
    "https://t.me/s/WPSNET",
    "https://t.me/s/v2rayng_fa2",
]

webpage_addresses = [
	        "https://t.me/sfreecfgalloperator",
]

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


html_pages = []

for url in old_webpage_addresses:
    response = requests.get(url)
    html_pages.append(response.text)

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if "vless://" in code_content or "ss://" in code_content or "vmess://" in code_content or "trojan://" in code_content:
            codes.append(code_content)

codes = list(set(codes))  # Remove duplicates

processed_codes = []

current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Jakarta'))

current_month = current_date_time.strftime("%b")

current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
#new_date_time = current_date_time + timedelta(hours=4)

updated_hour = current_date_time.strftime("%H")

updated_minute = current_date_time.strftime("%M")

final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_month}-{current_day}"
config_string = "#✅ " + str(final_string) + "-"

for code in codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            processed_codes.append(processed_part)

processed_codes = remove_duplicates(processed_codes)

new_processed_codes = []

for code in processed_codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            new_processed_codes.append(processed_part)

i = 0
with open("config.txt", "w", encoding="utf-8") as file:
    for code in new_processed_codes:
        if i == 0:
            config_string = "#🌐 Updated on" + final_string + " | Every 15 Minutes"
        else:
            config_string = "#🌐 Server" + str(i) + "| Sonzai X シ"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
