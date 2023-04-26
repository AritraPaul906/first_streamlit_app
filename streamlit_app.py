import streamlit

streamlit.title("My new healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 and blueberry oatmeal")
streamlit.text("🥗 Kale, spinach and rocket smoothie")
streamlit.text("🐔 Hard boiled free-range eggs")
streamlit.text("🥑🍞 Avocado toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
