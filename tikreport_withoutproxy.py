import requests
import time

url = "https://www.tiktok.com/aweme/v2/aweme/feedback/?aid=1988&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/111.0.0.0%20Safari/537.36&channel=tiktok_web&cookie_enabled=true&current_region=DE&device_id=7213053496391550470&device_platform=web_pc&focus_state=true&from_page=user&history_len=2&is_fullscreen=false&is_page_visible=true&lang=de-DE&nickname=%D0%BD%D0%B8%D0%BA%D0%BE%D0%BB%D1%8C%F0%9F%AB%B6&object_id=6946178450474812422&os=windows&owner_id=6946178450474812422&priority_region=&reason=91014&referer=&region=DE&report_type=user&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAdT-n5_hDs39qy8PkAFDZ91SeLuCEHQ-c6ifZoRpLMpbG_qOxhlW_TKACYFGoqMj_&target=6946178450474812422&tz_name=Europe/Berlin&webcast_language=de-DE"

while True:
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    time.sleep(2)