import media
import fresh_tomatoes
import requests
import keys


# get movie to search and perform request GET
# grab movie title, year, poster path, trailer link
# make movie instance
def get_movie_info(user_movie):
    """Retrieves useful information for a movie from themoviedb.org

    Args:
        user_movie: a string representing the title of a movie

    Returns:
        A list containing all information required to create an instance of media.Movie

    Raise:
        IndexError: occurs when the movie the user entered cannot be found and thus
        the list contains no elements
    """
    search_url = "https://api.themoviedb.org/3/search/movie?api_key={0}&language=en-US&" \
                 "query={1}&page=1&include_adult=true"
    vid_url = "https://api.themoviedb.org/3/movie/{0}/videos?api_key={1}&language=en-US"
    poster_url = "http://image.tmdb.org/t/p/w185{0}"
    yt_url = "https://www.youtube.com/watch?v={0}"
    response = requests.get(search_url.format(keys.API_KEY, user_movie.lower()))
    json = response.json()
    info = [json['results'][0]['title'], json['results'][0]['overview'], json['results'][0]['release_date'][:4],
           poster_url.format(json['results'][0]['poster_path'])]
    response = requests.get(vid_url.format(json['results'][0]['id'], keys.API_KEY))
    json = response.json()
    info.append(yt_url.format(json['results'][0]['key']))
    return info


# main
movie_list = []
for i in range(5):
    movie = input("Please enter one of your favorite movies:\n")
    try:
        movie = get_movie_info(movie)
    except IndexError as e:
        movie = ["", "", "", "", ""] # perhaps make default movie with dummy data
    movie_list.append(media.Movie(movie[0], movie[1], movie[2], movie[3], movie[4]))

fresh_tomatoes.open_movies_page(movie_list)

