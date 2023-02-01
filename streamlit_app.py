import streamlit
import pandas 

streamlit.title('My parents new Healthy Diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and blueberry omelettes')
streamlit.text('🥗 Kale, Spinach and Rcoket Smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
stream.multiselect('Pick some fruits',list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
