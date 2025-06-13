import streamlit as st
import pickle



def recommend(movie):
  movie_index=movies_list[movies_list['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_sortedlist=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]
  for i in movies_sortedlist:
      recommended_movies.append(movies_list.iloc[i[0]].title)
  return recommended_movies




similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movies.pkl','rb'))
movie_title=movies_list['title'].values
st.header("Movie Recommender system")
selected_movie_name=st.selectbox(
    "How would you like to be contacted?",
    movie_title
)
if st.button("Recomment"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)