import json


class TVShowsManager:

    def __init__(self):
        self.tv_shows = []

    def __str__(self):
        line = ''
        for i, show in enumerate(self.tv_shows):
            line += f'{i + 1}. '
            line += (f'Title: {show["title"]}, '
                     f'Genre: {show["genre"]}, '
                     f'Seasons: {show["seasons"]}, '
                     f'Rating: {show["rating"]}\n')
        return line

    def load_db(self, db_path: str) -> None:
        with open(db_path, "r", encoding="UTF-8") as f:
            self.tv_shows = json.load(f)["tv_shows"]

    def find_by_genre(self, genre: str):
        shows_by_genre = []
        for show in self.tv_shows:
            if show["genre"].lower() == genre.lower():
                shows_by_genre.append(show)
        return shows_by_genre

    def find_by_rating(self, rating: float):
        shows_by_genre = []
        for show in self.tv_shows:
            if show["rating"] == rating:
                shows_by_genre.append(show)
        return shows_by_genre

    def add_show(self, title: str, genre: str, seasons: int, rating: float) -> None:
        show = {
            "title": title,
            "genre": genre,
            "seasons": seasons,
            "rating": rating
        }
        self.tv_shows.append(show)

    def delete_show(self, title: str) -> bool:
        for i in range(len(self.tv_shows)):
            if self.tv_shows[i]["title"] == title:
                del self.tv_shows[i]
                return True
        return False

    def save_db(self, path: str):
        with open(path, "w", encoding="UTF-8") as f:
            tv_shows = {"tv_shows": self.tv_shows}
            json.dump(tv_shows, f)

    def get_info(self):
        return self.__str__()

    def manage(self) -> None:
        db_path = 'src/tv_shows_db.json'
        self.load_db(db_path)
        while True:
            print('-----------------------------')
            print("Choose number of operation:\n1. Search TV shows by genre\n2. Search TV shows by rating\n"
                  "3. Display information about all TV shows\n4. Add show\n5. Delete show\nQ. Finish work")

            choice = input("Number of operation: ").lower()
            if choice not in {"1", "2", "3", "4", "5", "q"}:
                print("There is no such operation.")
                continue
            if choice == "q":
                self.save_db(db_path)
                print("TV shows manager's work was stopped")
                break

            if choice == "1":
                genre = input('Enter the genre: ')
                matching_shows = self.find_by_genre(genre)
                if not matching_shows:
                    print(f'No TV shows with genre "{genre}" found')
                else:
                    for i, show in enumerate(matching_shows):
                        print(f"{i + 1}. {show['title']}")

            elif choice == "2":
                try:
                    rating = float(input('Enter the rating: '))
                except ValueError:
                    print("Rating was entered incorrectly")
                    continue
                matching_shows = self.find_by_rating(rating)
                if not matching_shows:
                    print(f'No TV shows with rating "{rating}" found')
                else:
                    for i, show in enumerate(matching_shows):
                        print(f"{i + 1}. {show['title']}")

            elif choice == "3":
                print(self)

            elif choice == "4":
                while True:
                    title = input('Enter the title: ')
                    genre = input('Enter the genre: ')
                    try:
                        seasons = int(input('Enter the number of seasons: '))
                        rating = float(input('Enter the rating: '))
                        print(f'"{title}" was added')
                    except ValueError:
                        print('The count of seasons and rating should be numbers')
                        continue

                    self.add_show(title, genre, seasons, rating)
                    break

            elif choice == "5":
                title = input('Enter the title: ')
                if self.delete_show(title):
                    print(f'The "{title}" series has been deleted')
                else:
                    print(f'No TV shows with genre "{title}" found')
