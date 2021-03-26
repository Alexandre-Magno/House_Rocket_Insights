#imports
import streamlit as st
import pandas    as pd
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import fixed

st.set_page_config(layout="wide")
#font size
st.markdown("""
<style>
.big-font {
    font-size:26px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.title {
    font-size:45px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.small-font {
    font-size:22px !important;
}
</style>
""", unsafe_allow_html=True)

#read csv
df = pd.read_csv('data/kc_house_data.csv')

df['date'] = pd.to_datetime( df['date'], format='%Y/%m/%d' )
df['month'] = df['date'].dt.month

#side bar information
st.sidebar.markdown( '##')
st.sidebar.markdown( '##')
st.sidebar.markdown( '##')
st.sidebar.markdown('# About me :')
st.sidebar.markdown( '## Name: Alexandre Magno')
st.sidebar.markdown( '- Industrial mathematics student at Universidade Federal Goiás ')
st.sidebar.markdown( '- I will be a data scientist ')

st.sidebar.markdown( "## Contact : ")




st.sidebar.markdown ('[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)] \
     (https://www.linkedin.com/in/alexandre-magno-b-3bbb16139/) [![Gmail Badge](https://img.shields.io/badge/-alexmagno.contato@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:alexmagno.contato@gmail.com)](mailto:alexmagno.contato@gmail.com)')


st.sidebar.markdown(' [![GitHub Badge](https://img.shields.io/badge/Git-Hub-brightgreen)](https://github.com/Alexandre-Magno)')


st.markdown(" <h1 class = 'title'; style='text-align: center; color: black;'>House Rocket Insights </h1> </p>", unsafe_allow_html=True)
#st.title('House Rocket Insights')
st.markdown(" <h1 class = 'big-font'; style='text-align: center; color: black;'>Here are the insights that blow your mind! </h1> </p>", unsafe_allow_html=True)



## ########### H1
aux1 = df[['price','waterfront']].groupby( 'waterfront').mean().reset_index()

fig1 = px.bar(aux1, x ='waterfront', y ='price', template='plotly_dark',
              labels={'waterfront' : 'Has Water View? ',
                      'price': 'Price on average'},height = 600)

fig1.update_layout(

    xaxis = dict(
        tickmode = 'array',
        tickvals = [0, 1],
        ticktext = ['No','Yes']

    )
)

#st.bar_chart(aux1)
st.write(' ')

st.markdown( '<p class="big-font"> H1- Houses with water view are more expensive on average </p>' , unsafe_allow_html = True)

st.plotly_chart(fig1)
diff = float(aux1['price'][aux1['waterfront'] == 1] ) - float( aux1['price'][aux1['waterfront'] == 0] )


st.markdown('<p class="small-font" >  True, Water view houses are on average $1.130.312,42 more expensive  </p>' , unsafe_allow_html = True )
############# H2 ###########################33

st.markdown( '<p class="big-font"> H2- Houses with 3 floors are more expensive! </p>' , unsafe_allow_html = True)

aux2 = df[['price','floors']].groupby('floors').median().reset_index()

fig2 = px.bar(aux2, x ='floors', y ='price', template='plotly_dark',
              labels={'floors' : 'Number of Floors ',
                      'price': 'Price on average'},height = 600,color='floors',width= 1000)

st.plotly_chart(fig2)

st.markdown( " **False**")

st.markdown( "The **highest** is average price is 2.5 Floors")

############## H3 ############################

st.markdown( '<p class="big-font"> H3 Houses with condition 5 are more expensive on average </p>' , unsafe_allow_html = True)

aux3 = df[['price','condition']].groupby( 'condition').median().reset_index()

Fig3 = px.bar(aux3, x ='condition', y ='price', template='plotly_dark',
              labels={'condition' : 'Type of condition ',
                      'price': 'Price on average'},height = 600,color='condition',width= 1000)

st.plotly_chart(Fig3)

st.markdown('Diff between condition  2 and condition  1  is : 6.29 % ')
st.markdown ( 'Diff between condition  3 and condition  2  is : **61.29** % ' )
st.markdown ('Diff between condition  4 and condition  3  is : -2.22 % ' )
st.markdown ( 'Diff between condition  5 and condition  4  is : 19.55 %')

################################################## H4 ###########################33

st.markdown( '<p class="big-font"> H4- Houses with more rooms are more expensive on average. </p>' , unsafe_allow_html = True)

aux4 =df[['bedrooms','price']].groupby( 'bedrooms' ).mean().reset_index()

fig4 = px.bar(aux4, x ='bedrooms', y ='price', template='plotly_dark',
              labels={'bedrooms' : 'Number of Bedrooms ',
                      'price': 'Price on average'},height = 600, width = 1200, color = 'bedrooms')
fig4.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tickvals = [0, 1, 2, 3, 4, 5,6,7,8,9,10,11,33],
    
    )
)

st.plotly_chart( fig4 )

st.markdown('<p class="small-font" >  the price grows between 1 and 8 </p>' , unsafe_allow_html = True )
##### CEO Questions
st.markdown(" <h1 class = 'big-font'; style='text-align: center; color: black;'> Answering the CEO's questions </h1> </p>", unsafe_allow_html=True)
st.markdown(' - #### Which houses should the House Rocket CEO buy and at what purchase price?')
st.markdown('The suggestions for houses to be purchased are houses with good conditions (type 3 or greater) and that have their price below the average price of their type of condition.')

st.markdown('- ####  Once the house is owned by the company, what is the best time to sell it and what would be the price of the sale?')

st.markdown('The best time to sell is **Summer and Spring** and the suggested retail price is 30% more expensive than the purchase price.')

st.markdown('I calculated three scenarios: ')
st.markdown('1 - Expected profit: Average profit of 20% ')
st.markdown('2- Best scenario: Average profit of 30%  ')
st.markdown('3- Worst case scenario: Average profit of 15%')
from PIL import Image
image = Image.open('img/pe32.png')
st.image (image)

st.markdown("- #### Should House Rocket do a renovation to increase the sale price? What would be the suggestions for changes? What is the increase in the price given for each retirement option?")
st.markdown("In H3, we can see that the biggest increase is from condition 2 to 3 with an **increase of 61.29%** So, my suggestion is to buy houses with type 2 condition, renovate and sell at the average price of type 3 condition.")
st.markdown("I'm guessing that the renovation will cost 20% of the house price.My profit in this case will be the average price of the type 3 condition minus the new price after the reform.")
st.markdown("I calculated three scenarios:")
st.markdown("1- Expected profit: Sales price equal to 90% of the average price of condition 3, which generates an average **profit of 77.78%**")
st.markdown("2- Best scenario: Sales price equal to the average price of condition 3, which generates an average **profit of 97.53%** ")
st.markdown("3- Worst scenario: Sales price equal to 80% of the average price of condition 3, which generates an average **profit of 58.02%** ")

st.markdown( "#### Total expected profit:")

image2 = Image.open("img/profit.png")
st.image(image2 )

##################### ITERATIVE MAP ##################

st.markdown(" <h1 class = 'big-font'; style='text-align: center; color: black;'> Map of suggested houses to buy </h1> </p>", unsafe_allow_html=True)

df_buy = pd.read_csv('data/houses_buy.csv')
df_raw = pd.read_csv('data/houses_buy.csv')
df_raw = df_raw.reset_index()

df_buy['is_waterfront'] = df_buy['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')


style = { 'description_width' : 'initial'}



#iterative buttons
limit = st.slider(label='Price Limit',
    value= 450000,
    min_value= 75000,
    max_value = 525888,
    step = 1)

waterfront = st.selectbox(
    options = df_buy['is_waterfront'].unique().tolist(),
    label = 'Water view '
)



df_buy = df_buy[(df_buy['price'] <= limit) & (df_buy['is_waterfront'] == waterfront)][['id','lat','long','price','condition']]



fig6 = px.scatter_mapbox(df_buy,lat = 'lat',lon = 'long', hover_name='id',
                        hover_data=['price'],
                        color_discrete_sequence=['fuchsia'],
                        zoom=10,
                        color='condition',
                        height= 700,width= 1200,size = 'price' ,size_max=10)

fig6.update_layout( mapbox_style = 'open-street-map')
fig6.update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})

st.plotly_chart(fig6)
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

show = st.checkbox( label = 'show dataset with all houses')

if show:
    st.dataframe(df_raw)
else:
    st.markdown('')










