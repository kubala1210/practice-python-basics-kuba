> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e02-python-basics` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#06` Python: Podstawy

## Pobierz dane z dowolnego adresu URL za pomocą `requests`  

Twoim zadaniem jest **uzupełnić funkcję**, która pobierze dane z podanego adresu URL i zwróci tekstową odpowiedź serwera.  

📌 **Instrukcja:**  
1. Otwórz plik `fetch_data.py`, który zawiera kod do uzupełnienia.  
2. Użyj biblioteki **`requests`**, aby pobrać zawartość strony z podanego **adresu URL**.  
3. Jeśli serwer zwróci kod odpowiedzi `200`, funkcja powinna zwrócić **zawartość strony jako tekst**.  
4. Jeśli serwer zwróci inny kod odpowiedzi, funkcja powinna zwrócić **"Błąd pobierania danych"**.  

📌 **Przykładowe adresy URL do testowania:**  
```python
weather_url = "https://wttr.in/?format=3"   # Skrócona aktualna pogoda
json_placeholder = "https://jsonplaceholder.typicode.com/posts/1"  # Przykładowe dane JSON

# Testowanie funkcji
print(fetch_data(weather_url))
print(fetch_data(json_placeholder))
```  

> **⭐ Podpowiedź:** 
- Możesz użyć `response.status_code`, aby sprawdzić kod odpowiedzi i `response.text`, aby pobrać zawartość strony.  
- Jeśli status kod jest różny od `200`, zwróć `"Błąd pobierania danych"`.  
- Link do przykładowego [opisu](https://pypi.org/project/requests/) biblioteki request

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-basics)*

> :arrow_left: [*poprzednie zadanie*](./../05) | ~~*następne zadanie*~~ :arrow_right:
