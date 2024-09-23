import streamlit as st
import pickle
import pandas as pd
from PIL import Image

def recommend(music):
    music_index = musics[musics['song_name'] == music].index[0]
    distance = similarity[music_index]
    music_list = sorted(list(enumerate(distance)),reverse = True,key=lambda x:x[1])[1:6]
    
    recommended_musics = []
    for i in music_list:
        recommended_musics.append((musics.iloc[i[0]].song_name+' - '+musics.iloc[i[0]].spotify_link))
    return recommended_musics

music_dict = pickle.load(open('music.pkl','rb'))
musics = pd.DataFrame(music_dict)

similarity = pickle.load(open('similarity.pkl','rb')) 

st.title('Music Recommender System')

selected_music_name = st.selectbox(
'Search Music!!',
musics['song_name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_music_name)
    for i in recommendations:
        st.write(i)