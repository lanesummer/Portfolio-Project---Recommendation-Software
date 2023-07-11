import string
from textwrap import TextWrapper, dedent
from movie_data import *
from linkedlist import *
from welcome import *
import time

# FUNCTIONS--------------------------------------------------------------------
# create function to determine if user wants to search by genre, rating, etc
def get_search_on():
    search_by = ''
    while len(search_by) == 0:
        user_input = str(input("\n\nHow would you like to search for movies? \nType g for genre, r for rating, a for alphabetical\n")).lower()
        if user_input != 'g' and user_input != 'r' and user_input != 'a':
            print('\nThat is not a valid response. Please try again.')
        else: search_by = 'genre' if user_input == 'g' else ('rating' if user_input == 'r' else 'letter')
    return search_by

# create code to insert genres into a data structure (LinkedList)
# for searching by genre
def insert_genre_types():
    genre_list = LinkedList()
    for genre in genres:
        genre_list.insert_beginning(genre)
    return genre_list

# for searching by rating
def insert_rating_types():
    rating_list = LinkedList()
    for rating in movie_ratings:
        rating_list.insert_beginning(rating)
    return rating_list

# for searching alphabetically
def insert_alphabet():
    alphabet_list = LinkedList()
    for letter in string.ascii_uppercase:
        alphabet_list.insert_beginning(letter, 0)
    return alphabet_list

# create code to insert movies into a data structure (LinkedList of LinkedLists)
# sorting by genre
def insert_movie_data_genre():
    movie_data_list = LinkedList()
    remove_list = []
    for genre in genres:
        genre_sublist = LinkedList()
        for movie in movies:
            index = 0
            while index < len(movie[0]):
                if movie[0][index] == genre:
                    movie_this_genre = [genre] + movie
                    genre_sublist.insert_beginning(movie_this_genre, 2)
                index += 1
        if genre_sublist.get_head_node().get_value() != None:
            movie_data_list.insert_beginning(genre_sublist)
        else:
            remove_list.append(genre)
    return movie_data_list, remove_list

# sorting by movie rating
def insert_movie_data_rating():
    movie_data_list = LinkedList()
    remove_list = []
    for rating in movie_ratings:
        rating_sublist = LinkedList()
        for movie in movies:
            if movie[4] == rating:
                movie_this_rating = [rating] + movie
                rating_sublist.insert_beginning(movie_this_rating, 2)
        if rating_sublist.get_head_node().get_value() != None:
            movie_data_list.insert_beginning(rating_sublist)
        else:
            remove_list.append(rating)
    return movie_data_list, remove_list

# sorting by letter
def insert_movie_data_letter():
    movie_data_list = LinkedList()
    remove_list = []
    for letter in string.ascii_uppercase:
        letter_sublist = LinkedList()
        for movie in movies:
            if movie[1][0] == letter:
                movie_this_letter = [letter] + movie
                letter_sublist.insert_beginning(movie_this_letter, 2)
        if letter_sublist.get_head_node().get_value() != None:
            movie_data_list.insert_beginning(letter_sublist)
        else:
            remove_list.append(letter)
    return movie_data_list, remove_list


# START PROGRAM HERE------------------------------------------------------------------------------
# add print statement for welcome import from welcome.py
print(welcome)

# create lists and variables needed to run program -----------------------
# get user input to determine how movies should be sorted/searched
search_by = get_search_on()

# create lists based on search parameters
my_type_list = insert_genre_types() if search_by == 'genre' else (insert_rating_types() if search_by == 'rating' else insert_alphabet())
my_movie_list, remove_list = insert_movie_data_genre() if search_by == 'genre' else  (insert_movie_data_rating() if search_by == 'rating' else insert_movie_data_letter())

selected_type = ''

# create code for user interaction
while len(selected_type) == 0:
    user_input = str(input(
        "\n\nWhat {0} of movie would you like to watch?\nType the beginning of that {0} and press enter to see if "
        "it's here.\n".format(search_by))).title()

    # Search for user_input (type) in my_type_list
    matching = []
    current_node = my_type_list.get_head_node()
    while current_node is not None:
        if str(current_node.get_value()).title().startswith(user_input) and not current_node.get_value() in remove_list and not current_node.get_value()[0] in remove_list:
            matching.append(current_node.get_value())
        current_node = current_node.get_next_node()

    # print list of matching types if more than one
    if len(matching) > 1:
        print('\n\nMore than one {0} matches that search: '.format(search_by))
        for match in matching:
            print(match)
        if user_input == 'PG':
            print("\nIf searching for PG add a space: 'PG ' \nIf searching for PG-13 add a hyphen: 'PG-'")

    if len(matching) == 0:
        print('\n\nSorry, there are no {0}s that match that search\n'.format(search_by))

    # Check if only one type was found, ask user if they would like to select this type
    if len(matching) == 1:
        if search_by == 'letter':
            select_movies = 'y'
        else:
            select_movies = str(input('\n\nThere is only one {1} that matches your search: {0} \n\n\nDo you want to look at {0} movies? Enter y for yes and n for no.\n'.format(matching[0], search_by))).lower()

        # After finding movie type, retrieve movie data for selected type
        if select_movies == 'y':
            selected_type = matching[0]
            print('\n==============================================================================')
            print('------------------------------------------------------------------------------')
            print('Selected {1}: {0}'.format(matching[0], search_by))
            print('------------------------------------------------------------------------------\n')
            my_movie_head = my_movie_list.get_head_node()
            while my_movie_head:
                sublist = my_movie_head.get_value().get_head_node()
                if sublist.get_value() is not None and sublist.get_value()[0] == selected_type:
                    while sublist is not None:
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
                        print(dedent('TITLE: {0}\n\nRated: {1}\nGenre(s): {2}\nTomatometer Score: {3}\nAudience Score: {4}\n\nOverview: {5}\n------------------------------------------------------------------------------\n'.format(title, rated, pgenre, tomato, audience, overview_wrapped)))
                        time.sleep(0.05)
                        sublist = sublist.get_next_node()
                my_movie_head = my_movie_head.get_next_node()

        # Ask user if they would like to search for other movies
        repeat = str(input('\n\nWould you like to look at movies in another {0}? Enter y for yes and n for no.\n'.format(search_by))).lower()
        selected_type = ''
        if repeat == 'n':
            search_again = str(input('\n\nWould you like to start another movie search? Enter y for yes and n for no.\n'))
            if search_again == 'y':
                selected_type = ''
                search_by = get_search_on()
                my_type_list = insert_genre_types() if search_by == 'genre' else (insert_rating_types() if search_by == 'rating' else insert_alphabet())
                my_movie_list, remove_list = insert_movie_data_genre() if search_by == 'genre' else  (insert_movie_data_rating() if search_by == 'rating' else insert_movie_data_letter())
            else:
                selected_type = 'end'
print('\n\nThank you for using Summer\'s Movie Picker!\n\n')
