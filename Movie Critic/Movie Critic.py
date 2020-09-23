import requests

API_KEY = "25725513"

def get_movie_details(movie):
    '''
    Description:
        Requests movie information from the IMDb database,
        and returns it in a JSON format.
    Output:
        If this function returns None, then handle_errors()
        prints an error message.
    '''
    url = "http://www.omdbapi.com/?t=" + movie + "&apikey=" + API_KEY
    try:
        # make the request and save the response
        response = requests.get(url)
        # extract data in json format
        data = response.json()
        return data
    except:
        return None


def writer_and_director(writer, director):
    '''
    Description:
        Decides wether the writer and director are the same
        and returns the appropriate statement.
    '''
    if director == writer:
        return 'Written and directed by ' + director
    return 'Directed by ' + director

def release_date(year):
    if year != 'N/A':
        print('Released in', year)


def critique(score):
    '''
    Description:
        Decides wether it should recommend the movie or not
        using the IMDb rating
    '''
    if score == 'N/A':
        return 'I don\'t have enough information to pass judgement'
    score = float(score)
    if score <= 4:
        return 'Stay away from this \'film\''
    elif score > 4 and score <= 5.5:
        return 'Probably not worth watching'
    elif score > 5.5 and score <= 6.5:
        return 'Watchable'
    elif score > 6.5 and score < 7:
        return 'Probably worth a watch'
    elif score >= 7 and score < 8.5:
        return 'Definitely worth a watch'
    elif score >= 8.5:
        return 'Must watch'


def print_movie_details(data):
    '''
    Decsription:
        Prints movie details including
        title, director, writer, and plot.
    Parameters:
        data - movie data in a JSON format
    '''
    print('\n' + data['Title'])
    print(writer_and_director(data['Writer'], data['Director']))
    release_date(data['Year'])
    print('\nPlot Synopsis:')
    print(data['Plot'], '\n')
    score = data['imdbRating']
    print('Rating:', score, '/ 10.0\n')
    print('Movie Critic says:', critique(score))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def handle_errors(data):
    '''
    Description:
        If get_movie_details() returns None or False response,
        this function prints the appropriate error message.
    Parameters:
        data - movie data in a JSON format
    Output:
        Is this function returns False, the program runs normally,
        if it returns True, the program restarts.
    '''
    error = True
    if data is None:
        # cannot connect to IMDb servers, likely an internet problem
        print('\nError: could not connected to IMDb servers, check your internet connection\n')
    elif data['Response'] == 'False' and data['Error'] == 'Movie not found!':
        # movie not found
        print('\nError: the movie was not found in the IMDb database\n')
    else:
        error = False
    return error


def main():
    print('\n~~~~~~~~~~~~~~~~~~ Movie Critic ~~~~~~~~~~~~~~~~~~\n')
    while True:
        movie = input('Enter a movie title (Q to quit): ')
        if movie.upper() == 'Q':
            break
        elif movie.upper() == '':
            print('')
            continue
        data = get_movie_details(movie)
        error = handle_errors(data)
        if error:
            continue
        print_movie_details(data)
    print('Thank you for using Movie Critic\n')


if __name__ == '__main__':
    main()