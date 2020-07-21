import time
actors=[]
nameofmovie=""
releasenote=""
movietype=""
rating=0
year=0
moviedetails=[]
audience_rating=[]
movies={}

#actors details
def add_user(actor):
    n=len(actor)
    for i in range(n):
        print("name of the actors:",actor[i])

#movie details and type of the movie 
def add_movie(nameofmovie,releasenote,movietype):
    moviedetails.append(nameofmovie)
    moviedetails.append(releasenote)
    moviedetails.append(movietype)
    moviedetails.append(actors)
    # n=len(moviedetails)
    # for i in range(n):
    print("movie information:",moviedetails)

# movie review provided
def add_review(actors,nameofmovie,rating):
    audience_rating.append(actors)
    audience_rating.append(nameofmovie)
    audience_rating.append(rating)
    
    # n=len(audience_rating)
    # for i in range(n):
    print("movie rating given by audience:",audience_rating)

def get_top_rated_movie_for_year(year,rating):
    i=1
    movies={
        "id":i,
        "movie":moviedetails,
        "movierating":rating,
        "yearofthemovie":year
        

    }
    list_of_movies=[movies]
    i=i+1
    if(rating==9):

        print(movies)
    


# def get_top_rated_movie_for_genre("movietype"):

# def get_average_rating_for_year(year):

if __name__ == "__main__":
    actors=["Hrithik Roshan","Mrunal Thakur"]
    add_user(actors)
    add_movie("SUPER30","release in 2019","MESSAGE ORIENTED")
    add_review(actors,"SUPER30",9)
    get_top_rated_movie_for_year(2019,9)