import pprint
from textwrap import *
from movie_data import *
from linkedlist import *
from welcome import *

# add print statement for welcome here when created -----------------------
print(welcome)


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
        genre_sublist = LinkedList()
        for movie in movies:
            index = 0
            while index < len(movie[0]):
                if movie[0][index] == genre:
                    movie_this_genre = [genre] + movie
                    genre_sublist.insert_beginning(movie_this_genre)
                index += 1
        movie_data_list.insert_beginning(genre_sublist)
    return movie_data_list


my_genre_list = insert_genre_types()
my_movie_list = insert_movie_data()

selected_genre = ''


# create code for user interaction
while len(selected_genre) == 0:
    user_input = str(input(
        "\nWhat genre of movie would you like to watch?\nType the beginning of that genre and press enter to see if "
        "it's here.\n")).title()

    # Search for user_input (genre) in my_genre_list
    matching = []
    current_node = my_genre_list.get_head_node()
    while current_node is not None:
        if str(current_node.get_value()).startswith(user_input):
            matching.append(current_node.get_value())
        current_node = current_node.get_next_node()

    # print list of matching genres if more than one
    if len(matching) > 1:
        print('\nMore than one genre matches that search: ')
        for genre in matching:
            print(genre)



    # Check if only one genre was found, ask user if they would like to select this type
    if len(matching) == 1:
        select_movie_genre = str(input('\nThere is only one genre that matches your search: {0} \nDo you want to look at {0} movies? Enter y for yes and n for no.\n'.format(matching[0]))).lower()

        # After finding genre, retrieve movie data for selected genre
        if select_movie_genre == 'y':
            selected_genre = matching[0]
            print('\n==============================================================================')
            print('------------------------------------------------------------------------------')
            print('Selected genre: {0}'.format(matching[0]))
            print('------------------------------------------------------------------------------\n')
            my_movie_head = my_movie_list.get_head_node()
            while my_movie_head.get_next_node() is not None:
                sublist = my_movie_head.get_value().get_head_node()
                # if there aren't movies in the selected genre
                if not sublist.get_value():
                    print('There are no movies for that genre\n')
                    break
                # if there are movies in the genre
                elif sublist.get_value()[0] == selected_genre:
                    while sublist.get_next_node() is not None:
                        # create variables to make print statements more readable
                        title = sublist.get_value()[2]
                        pgenre = ', '.join(sublist.get_value()[1])
                        rated = sublist.get_value()[5]
                        tomato = sublist.get_value()[6]
                        audience = sublist.get_value()[7]
                        # check if tomato and audience are integers, if so add '%' to the end
                        if isinstance(tomato, int): tomato = str(tomato) + '%'
                        if isinstance(audience, int): audience = str(audience) + '%'
                        # make the overview (long text) wrap in the terminal
                        overview_text  = sublist.get_value()[3]
                        wrapper = TextWrapper(width = 70)
                        overview_wrapped = wrapper.fill(overview_text)
                        # print result for movie(s) of the genre selected
                        print(dedent('Title: {0}\n\nGenre(s): {1}\nRated: {2}\nTomatometer Score: {3}\nAudience Score: {4}\n\nOverview: {5}\n------------------------------------------------------------------------------\n'.format(title, pgenre, rated, tomato, audience, overview_wrapped)))
                        sublist = sublist.get_next_node()
                my_movie_head = my_movie_head.get_next_node()


        # Ask user if they would like to search for other genres of movies
