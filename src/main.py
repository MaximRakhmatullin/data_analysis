from matrix_analysis import MatrixAnalysis as Ma
from tv_shows_manager import TVShowsManager

matrix = [[1, 2], [3, 4], [5, 1], [5, 1], [5, 5], [-1, 1]]
matrix2 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
]

db_path = 'src/tv_shows_db.json'

manager = TVShowsManager()
manager.load_db(db_path)


# print(Ma.sum(matrix))
# print(Ma.max(matrix))
# print(Ma.min(matrix))
# print(Ma.mode(matrix))
#
# print(manager.tv_shows)
# print(manager.find_by_genre("Fantasy"))
# print(manager.find_by_rating(8))
# print(manager.get_shows_info())
# print(manager)
# manager.add_show('Fallout', 'Action', 1, 8.5)
# print(manager)
# manager.save_db(db_path)
# manager.delete_show("Fallout")
# manager.save_db(db_path)
# print(manager)
manager.manage()
