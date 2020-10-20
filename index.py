import requests
import config as api


def shortenURL(url, unique_name, api=api):
    if len(unique_name) > 0:
        api_url = f"https://cutt.ly/api/api.php?key={api.api_key}&short={url}&name={unique_name}"
    else:
        api_url = f"https://cutt.ly/api/api.php?key={api.api_key}&short={url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        shortened_url = data["shortLink"]
        print("Shortened URL:", shortened_url)
    elif data["status"] == 3:
        print("The custom link is already in use")
        welcomebot()
    else:
        print("[!] Error Shortening URL:", data)

def welcomebot():
    unique_name=""
    print("*********************************************************************")
    url = input("Please enter the URL you would like to shorten: ")
    if len(url) < 0:
        print("Please input a valid URL")
    else:
        res = input("Would you like a custom name? \n [a]Yes \n [b]No \n >")
        if res == "a":
            unique_name = input("Please enter your custom name: ")
            
        shortenURL(url, unique_name)
            
welcomebot()  
    
    
     