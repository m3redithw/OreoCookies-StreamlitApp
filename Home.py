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
    image = Image.open('img/title1.png')
    st.image(image,width=450)
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
                      font_size = 16, yaxis_range=[3.5,7.5], legend=dict(
            orientation="h", y=-0.8, font = dict(size = 12)))

    # CHOCO
    chocolate = Image.open('img/chocolate.jpg')
    fig.add_layout_image(
        dict(
            source=chocolate,
            xref="x",
            yref="y",
            x=-0.4,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # MINI
    mini = Image.open('img/mini.png')
    fig.add_layout_image(
        dict(
            source=mini,
            xref="x",
            yref="y",
            x=0.6,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # MINT
    mint = Image.open('img/mint.png')
    fig.add_layout_image(
        dict(
            source=mint,
            xref="x",
            yref="y",
            x=1.5,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # CAKESTERS
    cakesters = Image.open('img/cakesters.jpg')
    fig.add_layout_image(
        dict(
            source=cakesters,
            xref="x",
            yref="y",
            x=2.6,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # MEGA
    mega = Image.open('img/mega.jpg')
    fig.add_layout_image(
        dict(
            source=mega,
            xref="x",
            yref="y",
            x=3.6,
            y=7.5,
            sizex=1.8,
            sizey=1.8,
            opacity=0.9,
            layer = 'below'
        )
    )

    # GLUTENFREE
    gluten = Image.open('img/glutenfree.png')
    fig.add_layout_image(
        dict(
            source=gluten,
            xref="x",
            yref="y",
            x=4.55,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # GOLDEN
    golden = Image.open('img/golden.jpg')
    fig.add_layout_image(
        dict(
            source=golden,
            xref="x",
            yref="y",
            x=5.55,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # DOUBLE STUF
    double = Image.open('img/double.jpeg')
    fig.add_layout_image(
        dict(
            source=double,
            xref="x",
            yref="y",
            x=6.5,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # BIRTHDAY CAKE
    birthday = Image.open('img/bdcake.png')
    fig.add_layout_image(
        dict(
            source=birthday,
            xref="x",
            yref="y",
            x=7.5,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # HALLOWEEN
    halloween = Image.open('img/halloween.jpg')
    fig.add_layout_image(
        dict(
            source=halloween,
            xref="x",
            yref="y",
            x=8.525,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )

    # BROOKIE
    brookie = Image.open('img/brookie.png')
    fig.add_layout_image(
        dict(
            source=brookie,
            xref="x",
            yref="y",
            x=9.55,
            y=7.5,
            sizex=2,
            sizey=2,
            opacity=0.9,
            layer = 'below'
        )
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
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
                      font_size = 16, xaxis_range=[4,5], showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # TITLE
    image = Image.open('img/title2.png')
    st.image(image,width = 500)

    # IMAGE
    image = Image.open('img/pumpkin.jpg')
    st.image(image,use_column_width=True)

with columns[1]:
    image = Image.open('img/dash2.png')
    st.image(image,use_column_width=True)

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

    # TITLE
    image = Image.open('img/title3web.png')
    st.image(image,width=1050)

