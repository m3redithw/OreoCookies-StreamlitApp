import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image
# Config
st.set_page_config(page_title='Home',
                   page_icon='😀',
                   layout="wide")

df = pd.read_csv('data/oreo.csv')
# mapping & categorize cookie type
df['cookie'] = df.type.map({'golden oreo sandwich cookies': 'Golden', 'double stuf chocolate oreo sandwich cookies': 'Double Stuf',
                            'Brookie-O Brownie, Original & Cookie Dough Creme Chocolate Sandwich Cookies': 'Brownie',
                            'gluten free oreo sandwich cookies': 'Gluten Free',
                            'cakesters soft snack cake': 'Cakesters',
                            'Mint Flavored Creme Chocolate Sandwich Cookies': 'Mint',
                            'Mega Stuf Chocolate Sandwich Cookies': 'Mega Stuf',
                            'Orange Creme Chocolate Sandwich Cookies, Halloween Cookies': 'Halloween',
                            'Birthday Cake Chocolate Sandwich Cookies': 'Birthday Cake',
                            'Oreo Mini': 'Mini',
                            'Oreo Mini Pokemon': 'Mini',
                            'double stuf gluten free oreo sandwich cookies': 'Gluten Free',
                            'oreo chocolate sandwich cookies': 'Chocolate'})
columns = st.columns((1,1))
with columns[0]:
    price = pd.DataFrame(df.groupby('cookie').price.mean().reset_index())
    price = price.sort_values('price')
    fig = px.bar(price, x='cookie', y='price', color = 'cookie', color_discrete_map={'Chocolate': '#89afff', 'Mini': '#6294ff', 'Mint': '#4e87ff',
                                                                                                                           'Cakesters': '#276dff', 'Mega Stuf': '#0052ff', 'Gluten Free': '#0045d7',
                                                                                                                           'Golden': '#003fc4', 'Double Stuf': '#00329d', 'Birthday Cake': '#002c89',
                                                                                                                           'Halloween': '#002675', 'Brownie': '#00194e'}, labels = {'price': 'Price', 'cookie': 'Oreo Type'})
    fig.add_hline(y=4.66)
    fig.update_xaxes(categoryorder='array', categoryarray= ['Chocolate', 'Mini', 'Mint', 'Cakesters', 'Mega Stuf', 'Gluten Free', 'Golden', 'Double Stuf', 'Birthday Cake', 'Halloween', 'Brownie'])
    fig.update_layout(paper_bgcolor="#fff4e4", plot_bgcolor='#fff4e4', font_color='#180909',
                      font_size = 16, yaxis_range=[3.5,6], legend=dict(
            orientation="h", y=-0.5, font = dict(size = 10)))
    st.plotly_chart(fig, use_container_width=True)


image = Image.open('img/spooky_cropped.png')
st.image(image,width = 1600)
