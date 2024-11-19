import requests

def search(category = "Any"):
    try:
        url = f"https://v2.jokeapi.dev/joke/{category}?lang=en"
        response = requests.get(url)
        response.raise_for_status()

        joke_data = response.json()
        if joke_data["type"] == "single":
            return joke_data["joke"]
        else:
            return f"{joke_data['setup']} - {joke_data['delivery']}"
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch a jokeerror: {e}"        