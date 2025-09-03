import requests
import csv

from request import country_code

headers = {
    'accept': '*/*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlU4UlRZVjVaRFMifQ.eyJpc3MiOiI3TktaMlZQNDhaIiwiaWF0IjoxNzUzODA3MDIyLCJleHAiOjE3NjEwNjQ2MjIsInJvb3RfaHR0cHNfb3JpZ2luIjpbImFwcGxlLmNvbSJdfQ.J2kE8jfGDxL0E_FTh0Sm9Uuy-WLLoy59r_7k5XOJ3efOYMdW6sNSWIjcrtw7KHW2hk_VmE8SxgUO68CDphoirA',
    'dnt': '1',
    'origin': 'https://apps.apple.com',
    'priority': 'u=1, i',
    'referer': 'https://apps.apple.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

params = {
    'l': 'en-gb',
    'platform': 'web',
    'additionalPlatforms': 'appletv,ipad,iphone,mac,realityDevice',
    'extend': 'customPromotionalText,customScreenshotsByType,customVideoPreviewsByType,description,developerInfo,distributionKind,editorialVideo,fileSizeByDevice,messagesScreenshots,privacy,privacyPolicyUrl,requirementsByDeviceFamily,sellerInfo,supportURLForLanguage,versionHistory,websiteUrl,videoPreviewsByType',
    'include': 'app-events,genres,developer,reviews,merchandised-in-apps,customers-also-bought-apps,developer-other-apps,top-in-apps,related-editorial-items',
    'limit[merchandised-in-apps]': '20',
    'omit[resource]': 'autos',
    'meta': 'robots',
    'sparseLimit[apps:related-editorial-items]': '20',
    'sparseLimit[apps:customers-also-bought-apps]': '20',
    'sparseLimit[apps:developer-other-apps]': '20',
}
app_id = "6473753684"
country_codes = [
    "us", "tr", "de", "gb", "fr", "es", "fi", "ca", "it", "au",
    "at", "nl", "ch", "pt", "se", "no", "be", "ie", "jp", "dk",
    "nz", "ae", "in", "sa", "br", "mx", "cn", "hk", "pl", "id",
    "tw", "lu", "za", "cz", "gr", "ng"]

# Liste pour stocker toutes les lignes à écrire dans le CSV
csv_rows = []

def fetch_in_app_purchases(country):
    url = f"https://amp-api-edge.apps.apple.com/v1/catalog/{country}/apps/{app_id}"
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    items = data.get("data", [])

    def catch_error():
        if "errors" in data:
            error_data = f"""
            JSON : {data['errors'][0]}
            ID : {data['errors'][0].get("id")}
            Title : {data['errors'][0].get("title")}
            Details : {data['errors'][0].get("detail")}
            Status : {data['errors'][0].get("status")}
            Code : {data['errors'][0].get("code")}
            """
            print(error_data)

    try:
        if not items:
            raise IndexError("No data for this country")

        top_in_apps_data = items[0].get("relationships", {}).get("top-in-apps", {}).get("data", [])
        if not top_in_apps_data:
            raise KeyError("No in-app purchases found")

        for k in top_in_apps_data:
            attributes = k.get("attributes", {})
            name = attributes.get("name")
            offers = attributes.get("offers", [])
            if offers:
                price = offers[0].get("price")
                priceformatted = offers[0].get("priceFormatted")
                if priceformatted:
                    priceformatted = priceformatted.replace('\xa0', ' ')
                currency = offers[0].get("currencyCode")
            else:
                price = priceformatted = currency = None

            # Ajouter une ligne à la liste
            csv_rows.append({
                "country": country,
                "name": name,
                "price": price,
                "price_formatted": priceformatted,
                "currency": currency
            })

    except (KeyError, IndexError):
        print(f"\nUnavailable App in {country}.")
        catch_error()


# Boucle sur tous les pays
for country in country_codes:
    fetch_in_app_purchases(country)

# Écriture dans le CSV
with open("Claude Price/in_app_purchases.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["country", "name", "price", "price_formatted", "currency"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(csv_rows)

print("Export terminé : in_app_purchases.csv")
