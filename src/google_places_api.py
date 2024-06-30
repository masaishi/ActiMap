import requests
import os
import json
from dotenv import load_dotenv
import time


class GooglePlacesAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://places.googleapis.com/v1/places:searchText"
        self.headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
            "X-Goog-FieldMask": "places.id,places.displayName,places.location,places.rating,places.userRatingCount,places.reviews,nextPageToken",
        }

    def find_places(self, search_word, lat, long, radius=5000, max_results=100):
        body = {
            "textQuery": search_word,
            "locationBias": {
                "circle": {
                    "center": {
                        "latitude": lat,
                        "longitude": long,
                    },
                    "radius": radius,
                }
            },
            "pageSize": min(max_results, 20),
            "languageCode": "ja",
        }

        places = []
        next_page_token = None

        while len(places) < max_results:
            response = requests.post(
                self.base_url, headers=self.headers, json=body
            ).json()
            print(response)
            if not response:
                break

            if "error" in response:
                print(f"Error: {response['error']}")
                break

            places.extend(response.get("places", []))

            next_page_token = response.get("nextPageToken")
            if not next_page_token or len(places) >= max_results:
                break

            body["pageToken"] = next_page_token
            time.sleep(2)

        return places

    @staticmethod
    def save_to_json(data, filename, save_path="data/inputs/"):
        # Save data to JSON file
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        output_file = os.path.join(save_path, filename)
        with open(output_file, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Data saved to {output_file}")


if __name__ == "__main__":
    # Load the .env file
    load_dotenv(".env")
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    ## Search parameters
    search_word = "Things to do"
    lat = 35.6895
    long = 139.6917

    # Create an instance of GooglePlacesAPI
    google_places = GooglePlacesAPI(api_key)

    # Find places
    places = google_places.find_places(
        search_word, lat, long, radius=10000, max_results=100
    )

    # Save as JSON
    google_places.save_to_json(places, "raw.json")
