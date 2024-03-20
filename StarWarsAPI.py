import requests

def get_film_info(film_id):
    film = requests.get_film(film_id)
    characters =\
        film.get_characters().order_by('name')
    vehicles = film.get_vehicles().order_by('name')
    starships = film.get_starships().order_by('name')
    species = film.get_species().order_by('name')

    print(f"Фільм: {film.title}")
    print("Персонажі:")
    for i, character in enumerate(characters.iter(), start=1):
        planet = character.get_homeworld().name if character.homeworld else "Невідома планета"
        print(f"  {i}. {character.name} з планети {planet}")

    print("Транспортні засоби:")
    for i, vehicle in enumerate(vehicles.iter(), start=1):
        print(f"  {i}. {vehicle.name}")

    print("Космічні кораблі:")
    for i, starship in enumerate(starships.iter(), start=1):
        print(f"  {i}. {starship.name}")

    print("Види істот:")
    for i, specie in enumerate(species.iter(), start=1):
        print(f"  {i}. {specie.name}")

film_id = input("Введіть ідентифікатор фільму: ")
get_film_info(film_id)
