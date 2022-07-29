import streamlit sl
import pandas pd

sl.title('My parents healthy diner')

sl.header('Breakfast menu')

sl.text('🥣 Omega 3 & bluberry oatmeal')
sl.text('🥗 kale, spinach & rocket smoothie')
sl.text('🐔 Hard boiled free range egg')
sl.text('🥑🍞 Avocado toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
sl.dataframe(my_fruit_list)
