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
		"https://t.me/s/v2rayng_org",
		"https://t.me/s/V2rayNGvpni",
		"https://t.me/s/custom_14",
		"https://t.me/s/v2rayNG_VPNN",
		"https://t.me/s/v2ray_outlineir",
		"https://t.me/s/v2_vmess",
		"https://t.me/s/FreeVlessVpn",
		"https://t.me/s/freeland8",
		"https://t.me/s/vmess_vless_v2rayng",
		"https://t.me/s/PrivateVPNs",
		"https://t.me/s/vmessiran",
		"https://t.me/s/Outline_Vpn",
		"https://t.me/s/vmessq",
		"https://t.me/s/WeePeeN",
		"https://t.me/s/V2rayNG3",
		"https://t.me/s/ShadowsocksM",
		"https://t.me/s/shadowsocksshop",
		"https://t.me/s/v2rayan",
		"https://t.me/s/ShadowSocks_s",
		"https://t.me/s/VmessProtocol",
		"https://t.me/s/napsternetv_config",
		"https://t.me/s/Easy_Free_VPN",
		"https://t.me/s/V2Ray_FreedomIran",
		"https://t.me/s/V2RAY_VMESS_free",
		"https://t.me/s/v2ray_for_free",
		"https://t.me/s/V2rayN_Free",
		"https://t.me/s/free4allVPN",
		"https://t.me/s/vpn_ocean",
		"https://t.me/s/configV2rayForFree",
		"https://t.me/s/FreeV2rays",
		"https://t.me/s/DigiV2ray",
		"https://t.me/s/v2rayNG_VPN",
		"https://t.me/s/freev2rayssr",
		"https://t.me/s/v2rayn_server",
		"https://t.me/s/Shadowlinkserverr",
		"https://t.me/s/iranvpnet",
		"https://t.me/s/vmess_iran",
		"https://t.me/s/mahsaamoon1",
		"https://t.me/s/V2RAY_NEW",
		"https://t.me/s/v2RayChannel",
		"https://t.me/s/configV2rayNG",
		"https://t.me/s/config_v2ray",
		"https://t.me/s/vpn_proxy_custom",
		"https://t.me/s/vpnmasi",
		"https://t.me/s/v2ray_custom",
		"https://t.me/s/VPNCUSTOMIZE",
		"https://t.me/s/HTTPCustomLand",
		"https://t.me/s/vpn_proxy_custom",
		"https://t.me/s/ViPVpn_v2ray",
		"https://t.me/s/FreeNet1500",
		"https://t.me/s/v2ray_ar",
		"https://t.me/s/beta_v2ray",
		"https://t.me/s/vip_vpn_2022",
		"https://t.me/s/FOX_VPN66",
		"https://t.me/s/VorTexIRN",
		"https://t.me/s/YtTe3la",
		"https://t.me/s/V2RayOxygen",
		"https://t.me/s/Network_442",
		"https://t.me/s/VPN_443",
		"https://t.me/s/v2rayng_v",
		"https://t.me/s/ultrasurf_12",
		"https://t.me/s/iSeqaro",
		"https://t.me/s/frev2rayng",
		"https://t.me/s/frev2ray",
		"https://t.me/s/FreakConfig",
		"https://t.me/s/Awlix_ir",
		"https://t.me/s/v2rayngvpn",
		"https://t.me/s/God_CONFIG",
		"https://t.me/s/Configforvpn01",
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

# Get the current date and time
current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
# Print the current month in letters
current_month = current_date_time.strftime("%b")

# Get the current day as a string
current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
#new_date_time = current_date_time + timedelta(hours=4)

# Get the updated hour as a string
updated_hour = current_date_time.strftime("%H")

updated_minute = current_date_time.strftime("%M")

# Combine the strings to form the final result
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
            config_string = "#🌐 به روزرسانی شده در" + final_string + " | هر 15 دقیقه کانفیگ جدید داریم"
        else:
            config_string = "#🌐سرور " + str(i) + " | " + str(final_others_string) + "| MTSRVRS"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
