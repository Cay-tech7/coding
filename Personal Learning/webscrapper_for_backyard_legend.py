import requests
import json
from time import sleep

# Replace with your actual SerpAPI key
API_KEY = "YOUR_SERPAPI_KEY"
BASE_URL = "https://serpapi.com/search"

# Contractor categories to search
contractor_categories = [
    "Concrete contractors",
    "Landscaping contractors",
    "Carpentry contractors",
    "Excavation contractors",
    "Fencing contractors",
    "Basketball court installers",
    "Putting green installers",
    "Fire pit builders",
    "Outdoor kitchen contractors",
    "Trampoline installers",
    "Lighting electricians",
    "Irrigation specialists",
    "Pool builders",
    "Outdoor audio visual installers",
    "Play structure builders",
    "Landscape designers",
    "3D render artists Utah",
    "Backyard project managers"
]


def search_contractors(query, location="Utah County, Utah"):
    params = {
        "engine": "google",
        "q": f"{query} near {location}",
        "api_key": API_KEY,
        "num": 10
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    results = []

    for result in data.get("organic_results", []):
        results.append({
            "title": result.get("title"),
            "link": result.get("link"),
            "snippet": result.get("snippet")
        })

    return results

def scrape_all_categories():
    all_results = {}
    for category in contractor_categories:
        print(f"🔍 Searching: {category}")
        results = search_contractors(category)
        all_results[category] = results
        sleep(2)  # Respectful delay to avoid rate limits
    return all_results

def get_int(prompt):  # helper to get a valid integer from the user
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")  # prompt again on bad input

def generate_series(start, end, step):  # generate list using a for loop
    nums = []  # store numbers here
    if step == 0:
        return None  # invalid step
    if (start <= end and step < 0) or (start >= end and step > 0):
        return None  # step sign doesn't progress from start to end
    stop = end + (1 if step > 0 else -1)  # make range inclusive
    for n in range(start, stop, step):  # loop to build sequence
        nums.append(n)
    return nums

def save_to_file(numbers, filename):  # write numbers one per line
    with open(filename, "w") as f:
        for n in numbers:
            f.write(f"{n}\n")

if __name__ == "__main__":
    contractor_data = scrape_all_categories()
    with open("utah_contractors.json", "w") as f:
        json.dump(contractor_data, f, indent=2)
    print("✅ Contractor data saved to utah_contractors.json")
    start = get_int("Enter start value: ")  # get start
    end = get_int("Enter end value: ")  # get end
    step = get_int("Enter step value (non-zero): ")  # get step
    series = generate_series(start, end, step)  # create the list
    if series is None or len(series) == 0:  # validate result
        print("Invalid range/step combination. Make sure step is non-zero and moves from start toward end.")
    else:
        save_to_file(series, "number_series.txt")  # write to file
        print(f"Wrote {len(series)} numbers to number_series.txt")  # final message