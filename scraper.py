import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_sbp_kibor_rate():
    url = "https://www.sbp.org.pk/ecodata/Kibor.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    kibor = None
    for td in soup.find_all("td"):
        if "%" in td.text:
            kibor = td.text.strip().replace("%", "")
            break

    sbp_base_rate = 20.5  # You can scrape this from SBP's policy page if needed
    return float(sbp_base_rate), float(kibor)

def get_meezan_murabaha_rate():
    url = "https://www.meezanbank.com/easy-home/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    murabaha_rate = None
    for strong in soup.find_all("strong"):
        if "%" in strong.text:
            murabaha_rate = strong.text.strip().replace("%", "")
            break

    return float(murabaha_rate) if murabaha_rate else 13.5

def save_rates():
    sbp_base_rate, kibor_rate = get_sbp_kibor_rate()
    murabaha_rate = get_meezan_murabaha_rate()

    data = {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "conventional_loans": {
            "sbp_base_rate": sbp_base_rate,
            "kibor_rate": kibor_rate
        },
        "islamic_loans": {
            "murabaha_rate": murabaha_rate
        }
    }

    with open("rates.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ rates.json updated successfully!")

if __name__ == "__main__":
    save_rates()
