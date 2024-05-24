import requests
from bs4 import BeautifulSoup

def check_google_business(business_name, location):
    query = f"{business_name} {location}"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check if any Google Business profiles appear in the results
    business_profile = soup.find_all('div', class_='BNeawe deIvCb AP7Wnd')
    for profile in business_profile:
        if "Google Business" in profile.text:
            return True
    return False

# Example usage
businesses = [
    ("Sunset Diner", "YourCity"),
    ("Harmony Salon", "YourCity"),
    ("Books & Brews", "YourCity"),
    ("Evergreen Hardware", "YourCity"),
    ("Greenleaf Florist", "YourCity"),
    ("Cozy Corner Café", "YourCity"),
    ("City Cycle Repair", "YourCity"),
    ("Traditional Tailors", "YourCity"),
    ("Vintage Vinyl", "YourCity"),
    ("Fit and Fab Gym", "YourCity")
]

for business in businesses:
    name, location = business
    if not check_google_business(name, location):
        print(f"{name} in {location} does not have a Google Business listing.")
    else:
        print(f"{name} in {location} has a Google Business listing.")
