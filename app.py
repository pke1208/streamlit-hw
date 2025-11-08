import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('movies.csv')
df = df.dropna(subset=['name']) 
st.title('Movie Details and Visualization App')

# Dropdown for movie selection
movie_names = sorted(df['name'].unique())
selected_movie = st.selectbox('Select a movie:', movie_names)

if selected_movie:
    # Get the movie data
    movie_data = df[df['name'] == selected_movie].iloc[0]
    
    # Display movie details
    st.subheader(f"Details for {selected_movie}")
    st.write(f"**Director:** {movie_data['director']}")
    st.write(f"**Rating:** {movie_data['rating']}")
    st.write(f"**Genre:** {movie_data['genre']}")
    st.write(f"**Year:** {movie_data['year']}")
    st.write(f"**Released:** {movie_data['released']}")
    st.write(f"**Score:** {movie_data['score']}")
    st.write(f"**Votes:** {movie_data['votes']}")
    st.write(f"**Writer:** {movie_data['writer']}")
    st.write(f"**Star:** {movie_data['star']}")
    st.write(f"**Country:** {movie_data['country']}")
    st.write(f"**Budget:** ${movie_data['budget']:,}")
    st.write(f"**Gross:** ${movie_data['gross']:,}")
    st.write(f"**Company:** {movie_data['company']}")
    st.write(f"**Runtime:** {movie_data['runtime']} minutes")
    
    # Simple visualization: Bar chart comparing movie's numerical stats to dataset averages
    st.subheader('Visualization: Movie Stats vs Dataset Averages')
    averages = df[['score', 'votes', 'budget', 'gross', 'runtime']].mean()
    movie_stats = movie_data[['score', 'votes', 'budget', 'gross', 'runtime']]
    
    comparison_df = pd.DataFrame({
        'Metric': ['Score', 'Votes', 'Budget', 'Gross', 'Runtime'],
        'Movie': movie_stats.values,
        'Average': averages.values
    })
    
    st.bar_chart(comparison_df.set_index('Metric'))
