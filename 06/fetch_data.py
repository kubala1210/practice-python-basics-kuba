import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Dane pobrane poprawnie')
        return response.text
    else:
        print('Błąd pobierania danych')
        pass
   

weather_url = "https://wttr.in/?format=3"
json_placeholder = "https://jsonplaceholder.typicode.com/posts/1"

print(fetch_data(weather_url))
print(fetch_data(json_placeholder))
