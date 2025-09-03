import requests

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

country_code = ["fr", "cn"]
country = "cn"
app_id = "6473753684"


url = f"https://amp-api-edge.apps.apple.com/v1/catalog/{country}/apps/{app_id}"

for k in country_code:
    print(k)

response = requests.get(url, params=params, headers=headers)


data = response.json()
items = data.get("data", [])




def catch_error():
    error_data = f"""
    JSON : {data["errors"][0]}
    ID : {data["errors"][0]["id"]}
    Title : {data["errors"][0]["title"]}
    Details : {data["errors"][0]["detail"]}
    Status : {data["errors"][0]["status"]}
    Code : {data["errors"][0]["code"]}
    """
    print(error_data)


def in_app_purchase():
    top_in_apps_data = items[0]["relationships"]["top-in-apps"]["data"]

    for k in top_in_apps_data:
        attributes = k.get("attributes", {})
        name = attributes.get("name", {})
        price = attributes["offers"][0]["price"]
        pricestring = attributes["offers"][0]["priceString"]
        priceformatted = attributes["offers"][0]["priceFormatted"]
        currency = attributes["offers"][0]["currencyCode"]

        print(name)
        print(priceformatted)

try:
    in_app_purchase()
except (KeyError, IndexError):
    print("\n   Unavailable App in this Country.")
    catch_error()



