"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = [" Movie Recommender","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == " Movie Recommender":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.info('Introduction')
        st.write(
            'We live in a wonderful world where endless entertainments are available at the comfort of your home.\
            In recent years the entertainment streaming services became extremely competitive as numerous large\
            entertainment industries have deployed their own streaming platforms. It is not only the amount and\
            quality, but also the recommendation of contents that keeps the users subscribed to a platform.\
            During the last few decades, with the rise of YouTube, Amazon, Netflix and\
            many other such web services, recommender systems have taken more and more place in our lives.\
            Recommendation systems are socially and economically important system for the platforms,\
            as it offers the users appropriate contents based on their viewing history,\
            thus keeping them engaged to the service.\
            From e-commerce (suggest to buyers articles that could interest them)\
            to on-line advertisement (suggest to users the right contents, matching their preferences),\
            recommender systems are today unavoidable in our daily on-line journeys.'
            )

        st.info('What are recommender systems?')
        st.write(
            'In a very general way, recommender systems are algorithms aimed at suggesting\
            relevant items to users (items being movies to watch,\
            text to read, products to buy or anything else depending on industries).\
            With this context,\
            '
        )
        
        st.info('Our Objective')
        st.write(
           'we are aiming to build a recommendation algorithm based on content to collaborative filtering\
            that is capable of accurately predicting how a user will rate a movie they have not yet accessed\
            based on their historical preferences. Recommender systems are really critical in some industries\
            as they can generate a huge amount of income when they are efficient or also be a way to stand out\
            significantly from competitors.\
            Our algorithm may provide an accurate and robust solution to this economically significant challenge\
            for the entertainment streaming industries by encouraging user-platform affinity, thus ultimately\
            generating revenue.'
        )

   
        options=['Exploratory Data Analysis',"Recomender Models",'Resources','Raw Data']
        navigator=st.radio('Select and navigate to the relevant page for discriptions',options)

        if navigator=='Exploratory Data Analysis':
            st.title('Exploratory Data Analysis')
            st.markdown(
                'Exploratory Data Analysis refers to the critical process of performing\
                initial investigations on data so as to discover patterns,\
                to spot anomalies,to test hypotheses and to check assumptions with the help\
                of summary statistics and graphical representations. \
               '
            )
            st.info('Movie Production Trend')
            st.image('EDA_files\Productionyears.png')
            st.markdown(
                'The year 1995 has the highest number of movies released in the dataset'
                )

            st.info('Prominent Genres & Movie Types')
            st.image('EDA_files\Prominentgenres.png')
            st.image('EDA_files\Popgen.png')
            st.markdown(
                'Drama is the most popular genre in the dataset\
                 it would be expected to have a bigger weight on the outcome of\
                 the prediction we can be confident of pridictions that lie within the drama\
                 genre and others subsequent ones'
                )

            st.info('Rating Tendecies Across All Genres')
            st.image('EDA_files\Popularratings.png')
            st.image('EDA_files\Poprat.png')
            st.markdown(
                'We can see that the majority of movies ratings are between 3.0 to 5.\
                 with most ratings falling in 3.0,4.0,5.0\
                 there apears to be major rating categories\
                 the model we fit takes into account the weights of these ratings in\
                 recommandations highly rated movies will generally\
                 be most likley to be recommended  '
                )
            
            

            st.info('Popular Actors')
            st.image('recommenders\Resources\imgs\actors.png')
            st.markdown(
                'Samuel L. Jackson is the most featured actor in the database followed by Steve Buscemi\
                 as such we expect an affiliation with these top actors in the overall recommentation choices.\
                ')

            st.info('Popular Movie Directors')
            st.image('EDA_files\Popdir.png')
            st.markdown(
                '- The phrase "See full Summary" appears the most under featured Director\
                 - Both Woody Allen and Luc Besson are featured 26 times in the dataset\
                 such we expect an affiliation with these top actors in the overall recommentation choices.'
                )

            st.info('Popular Movie Plots')
            st.image('recommenders\Resources\imgs\directors.png')
            st.markdown( 
                '**rated F** and **female nudity** are the most popular movie plots in the dataset'                                                                                                                      
                )
        
        if navigator=='Raw Data':
            st.title('Raw data & Origins')
            st.info('Data Source')
            st.markdown(
                    'The data for the MovieLens dataset is maintained by the GroupLens\
                    research group in the Department of Computer Science and Engineering\
                    at the University of Minnesota. Additional movie content data was legally\
                    scraped from IMDB'
               )
            st.write(
                    "This dataset consists of several million 5-star ratings \
                    obtained from users of the online MovieLens movie recommendation service\
                    The MovieLens dataset has long been used by industry and\
                    academic researchers to improve the performance of explicitly-based\
                    recommender systems. For this  app, we \
                    used a special version of the MovieLens dataset which has enriched with\
                    additional data, and resampled for fair evaluation purposes."
                  )
                  
            st.info('Movies dataset')
            st.dataframe(pd.read_csv('resources\data\movies.csv'))
            st.info('Ratings dataset')
            st.dataframe(pd.read_csv('resources\data\Latings.csv'))
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
