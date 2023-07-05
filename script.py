from movie_data import *
from linkedlist import *

# add print statement for welcome here when created -----------------------


# create code to insert genres into a data structure (LinkedList)
def insert_genre_types():
    genre_list = LinkedList()
    for genre in genres:
        genre_list.insert_beginning(genre)
    return genre_list

# create code to insert movies into a data structure (LinkedList of LinkedLists)
def insert_movie_data():
    movie_data_list = LinkedList()
    for genre in genres:
        # print(genre) #-------can delete later
        # print('-------------------') #-------can delete later
        genre_sublist = LinkedList()
        for movie in movies:
            index = 0
            while index < len(movie[0]):
                if movie[0][index] == genre:
                    genre_sublist.insert_beginning(movie)
                index += 1
        # print(genre_sublist.stringify_list()) #-------can delete later
        movie_data_list.insert_beginning(genre_sublist)
    return movie_data_list


my_genre_list = insert_genre_types()
my_movie_list = insert_movie_data()

selected_genre = ''

# create code for user interaction



