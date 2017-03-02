import media
import fresh_tomatoes

#create movies class
toy_story = media.Movie("Logan","In the near future, a weary Logan cares for an ailing Professor X in a hide out on the Mexican border. But Logan's attempts to hide from the world and his legacy are up-ended when a young mutant arrives, being pursued by dark forces."
                        ,"http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                        "https://www.youtube.com/watch?v=Div0iP65aZo",
                        media.Movie.VALID_RATINGS[1])
avator = media.Movie("Avator",
                     "A marine on an alien planet","http://cdn.movieweb.com/img.teasers.posters/FIsT9wwulpYIwu_369_c.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     media.Movie.VALID_RATINGS[0])
the_great_wall = media.Movie("The great wall",
                             "Matt Damon encounters the Great Wall of China and meets Chinese soldiers who defend against monsters.",
                             "https://s-media-cache-ak0.pinimg.com/736x/67/8a/74/678a740dd8cc6d9af045de6c66d473dc.jpg"
                             ,"https://www.youtube.com/watch?v=LVw9YdP1O-0",
                             media.Movie.VALID_RATINGS[2])

#add movies into array
movies = [toy_story,avator,the_great_wall]

#open movie page
fresh_tomatoes.open_movies_page(movies)


