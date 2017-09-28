import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",)

#print (avatar.storyline)

avengers2 = media.Movie("Avenger: Age of Ultron","Avenger's battle against Utron.",
                        "http://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                        "https://www.youtube.com/watch?v=iSAyI1HBD6s")

#print (avengers2.storyline)
#avengers2.show_trailor()

movies = [toy_story,avengers2]
fresh_tomatoes.open_movies_page(movies)
