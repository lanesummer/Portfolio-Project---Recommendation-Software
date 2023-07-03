from genres import *
from movie_data import *
from linkedlist import *





def add_movie():
    movie_list = LinkedList()
    for movie in movies:
        movie_list.insert_beginning(movie)
    return movie_list

def get_info(list, tar_key):
    index = 0
    while data_headings[index] != tar_key:
        index += 1
    # info = list.get_val(index)
    # print(info)
    return list.get_val(index)


test = add_movie()



print('----------------')

print(get_info(test, 'title'))
