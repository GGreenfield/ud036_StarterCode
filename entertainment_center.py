import media
import fresh_tomatoes
import requests
import keys


def get_movie_info(user_movie):
    """Retrieves useful information for a movie from themoviedb.org

    Args:
        user_movie: a string representing the title of a movie

    Returns:
        A list containing all information required to create an instance
        of media.Movie

    Raise:
        IndexError: occurs when the movie the user entered cannot be
        found and thus the list contains no elements
    """
    search_url = "https://api.themoviedb.org/3/search/movie?api_key={0}&language=en-US&query={1}&page=1&include_adult=true"  # noqa
    vid_url = "https://api.themoviedb.org/3/movie/{0}/videos?api_key={1}&language=en-US"  # noqa
    poster_url = "http://image.tmdb.org/t/p/w185{0}"  # noqa
    yt_url = "https://www.youtube.com/watch?v={0}"  # noqa

    # make api call to search endpoint and then convert that response
    # to a json object
    response = requests.get(search_url.format(keys.API_KEY,
                                              user_movie.lower()))
    json = response.json()
    # parse the json data, populating a list of relevant information for
    # a movie
    info = [json['results'][0]['title'], json['results'][0]['overview'],
            json['results'][0]['release_date'][:4],
            poster_url.format(json['results'][0]['poster_path'])]

    # make api call to video endpoint and append the parsed json to the
    # information list
    response = requests.get(vid_url.format(json['results'][0]['id'],
                                           keys.API_KEY))
    json = response.json()
    info.append(yt_url.format(json['results'][0]['key']))
    return info


# main
# initialize an empty list to hold 5 of the user's favorite movies
# iteratively ask the user to search for a movie and attempt to
# create a movie object if that movie exists in TMDb, otherwise
# keep asking until a movie is found and then call
# fresh_tomatoes.open_movies_page() with the movie_list
movie_list = []
for i in range(5):
    movie = input("Please enter one of your favorite movies:\n")
    while True:
        try:
            movie = get_movie_info(movie)
            break
        except IndexError as e:
            movie = input("That movie cannot be found, try again:\n")

    movie_list.append(media.Movie(movie[0], movie[1], movie[2],
                                  movie[3], movie[4]))

fresh_tomatoes.open_movies_page(movie_list)
