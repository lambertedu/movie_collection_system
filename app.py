MENU_PROMPT = "Eenter 'a' to add a movie, 'l' to list movies, 'f' to find a movie, 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter movie title: ")
    director = input("Enter movie director: ")
    year = input("Enter movie relaese year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })
    print("Movies added successfully!\n")


def list_movie():
    if not movies:
        print("No movies in the list.\n")
    else:
        for movie in movies:
            print_movie(movie)


def find_movie():
    search_movie = input("Enter movie title to search: ")

    for movie in movies:
        if search_movie.lower() == movie['title'].lower():
            print("movie found!")
            print_movie(movie)
            return
    print("Movie not found")


def print_movie(movie):
    print(
        f"Title: {movie['title']}\nDirector: {movie['director']}\nYear: {movie['year']}\n")

user_option = {
    "a" : add_movie,
    "l" : list_movie,
    "f" : find_movie
}

def menu():
    selection = input(MENU_PROMPT)

    while selection != 'q':
        
        if  selection in user_option:
            selection_functon = user_option[selection]
            selection_functon()
        else:
            print("Invalid selection. Try again\n")
        selection = input(MENU_PROMPT)


menu()
