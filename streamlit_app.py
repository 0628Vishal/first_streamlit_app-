import snowflake.connector
import streamlit
import pandas
import requests
from urllib.error import URLError


streamlit.title('My parents new Healthy Diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and blueberry omelettes')
streamlit.text('🥗 Kale, Spinach and Rcoket Smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect('Pick some fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please enter a fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLerror as e:
  streamlit.error()
    
streamlit.write('The user entered ', fruit_choice)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


fruit_choice_one = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding', fruit_choice_one)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
