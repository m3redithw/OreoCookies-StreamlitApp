import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from PIL import Image
# Config
st.set_page_config(page_title='Home',
                   page_icon='🎃',
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
                            'oreo chocolate sandwich cookies': 'Chocolate'})
columns = st.columns((3,0.5))
with columns[0]:
    title = '<p style=" color:#231717; font-size: 35px;"><b>Oreo Prices vs. Cookie Type</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    price = pd.DataFrame(df.groupby('cookie').price.mean().reset_index())
    price = price.sort_values('price')
    fig = px.bar(price,
                 x='cookie', y='price', color = 'cookie', color_discrete_map={'Chocolate': '#E4F4FC', 'Mini': '#BFE6FA', 'Mint': '#A4DCF8',
                                                                                 'Cakesters': '#92D4F6', 'Mega Stuf': '#88D1F6', 'Gluten Free': '#7FCDF5',
                                                                                 'Golden': '#64C3f3', 'Double Stuf': '#49b8f1', 'Birthday Cake': '#36b1ef',
                                                                                 'Halloween': '#F29466', 'Brownie': '#0E84bf'}, labels = {'price': 'Price', 'cookie': 'Oreo Type'})
    fig.add_hline(y=4.66, line_dash="dash", line_color = '#ed5a14', annotation_text="Avg. Oreo Price in the U.S.",
                  annotation_position="bottom left", annotation_font_size=12,
                  annotation_font_color="#D2510F")
    fig.update_xaxes(categoryorder='array', categoryarray= ['Chocolate', 'Mini', 'Mint', 'Cakesters', 'Mega Stuf', 'Gluten Free', 'Golden', 'Double Stuf', 'Birthday Cake', 'Halloween', 'Brownie'])
    fig.update_layout(paper_bgcolor="#fff4e4", plot_bgcolor='#fff4e4', font_color='#231717',
                      font_size = 16, yaxis_range=[3.5,6], legend=dict(
            orientation="h", y=-0.8, font = dict(size = 12)))
    st.plotly_chart(fig, use_container_width=True)

with columns[1]:
    image = Image.open('img/spider.png')
    st.image(image,width = 200)

#============================================================================================================#
#============================================================================================================#
# MIDDLE IMAGE
image = Image.open('img/spooky_cropped.png')
st.image(image,width = 1600)

#============================================================================================================#
#============================================================================================================#
# BOTTOM
columns = st.columns((1,2))
with columns[0]:
    title = '<p style=" color:#231717; font-size: 35px;"><b>Oreo Cookies Rating ☆☆☆☆☆</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    rating = pd.DataFrame(df.groupby('cookie').rating.mean().reset_index())
    rating = rating.sort_values('rating')
    fig = px.bar(rating, x='rating', y='cookie', color = 'cookie', color_discrete_map={'Chocolate':'#E4F4FC','Brownie': '#BFE6FA',
                                                                                       'Cakesters': '#A4DCFA', 'Gluten Free': '#92D4F6',
                                                                                       'Birthday Cake': '#88D1F6', 'Mega Stuf': '#7FCDF5',
                                                                                       'Halloween': '#F29466', 'Mini': '#64C3f3', 'Mint': '#49b8f1',
                                                                                       'Golden': '#36b1ef', 'Double Stuf': '#0E84bf'},
                 labels = {'cookie': 'Oreo Type',
                           'rating': 'Average U.S. Rating'
                 })
    fig.add_vline(x=4.6, line_dash="dash", line_color = '#ed5a14', annotation_text="Avg. Oreo Rating in the U.S.",
                  annotation_position="top right", annotation_font_size=12,
                  annotation_font_color="#D2510F")
    fig.update_layout(paper_bgcolor="#fff4e4", plot_bgcolor='#fff4e4', font_color='#231717',
                      font_size = 16, xaxis_range=[4,5], legend=dict(
             orientation = 'h',y=-0.5, font = dict(size = 12)))
    st.plotly_chart(fig, use_container_width=True)
with columns[1]:
    fig = px.scatter(df, x='launch_year',y='cookie', color = 'cookie', color_discrete_map={'Chocolate': '#E4F4FC', 'Mini': '#88D1F6', 'Mint': '#88D1F6',
                                                                                            'Cakesters': '#64C3f3', 'Mega Stuf': '#49b8f1', 'Gluten Free': '#0E84bf',
                                                                                            'Golden': '#7FCDF5', 'Double Stuf': '#B6E3F9', 'Birthday Cake': '#49b8f1',
                                                                                            'Halloween': '#F29466', 'Brownie': '#36b1ef'}, labels = {'launch_year': 'Year of Initial Launch', 'cookie': 'Oreo Type'})
    fig.update_layout(paper_bgcolor="#fff4e4", plot_bgcolor='#fff4e4', font_color='#231717',
                       font_size = 16, legend=dict(
             orientation="h", y=-0.5, font = dict(size = 12)))
    fig.update_traces(marker=dict(size=12,
                                   line=dict(width=2)))
    st.plotly_chart(fig, use_container_width=True)