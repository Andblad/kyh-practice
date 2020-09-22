import params as params
from pprint import pprint
import requests
film = input("Välj en film:")

r = requests.get('http://www.omdbapi.com/',params={"t": film, "apikey": "9f6d550c"})
film_fil=r.json()
#pprint(URL.json())
print("*** Resultat från OMDB! ***")
print(f"Titel: {film_fil['Title']},({film_fil['Year']}) resigserads av {film_fil['Director']}")
print(f"Skådespelare: {film_fil['Actors']}")
print(f"Betyg: {film_fil['imdbRating']}")
print(f"Utmärkelser:{film_fil['Awards']}")
print(f"Längd: {film_fil['Runtime']}")
