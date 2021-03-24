#imports
import streamlit as st
import pandas    as pd
import plotly.express as px

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


st.markdown( '<p class="big-font"> H2 - Houses with a construction date less than 1955 are 50% cheaper on average. </p>' , unsafe_allow_html = True)

df['year_1955'] = df.apply( (lambda x: 0 if x['yr_built'] < 1955 else 1 ), axis = 1 )

aux2 = df[['price','year_1955']].groupby( 'year_1955' ).mean().reset_index()


fig2 = px.bar(aux2, x ='year_1955', y ='price', template='plotly_dark',
              labels={'year_1955' : 'Year 1955 ',
                      'price': 'Price on average'},height = 600)

fig2.update_layout(

    xaxis = dict(
        tickmode = 'array',
        tickvals = [0, 1],
        ticktext = ['Under','Above']

    )
)

st.plotly_chart(fig2)

st.markdown('<p class="small-font" >  False, As we can see there is no significant difference </p>' , unsafe_allow_html = True )

st.markdown( '<p class="big-font"> H3 - The growth in the price of houses year over year is 10%. </p>' , unsafe_allow_html = True)

aux3 = df[['price','yr_built']].groupby( 'yr_built' ).mean().reset_index()

fig3 = px.line(aux3, x ='yr_built', y ='price', template='plotly_dark',
              labels={'yr_built' : 'Year that was built ',
                      'price': 'Price on average'},height = 600, width = 1200)

st.plotly_chart( fig3 )

st.markdown('<p class="small-font" >  False! </p>' , unsafe_allow_html = True )



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

st.markdown('<p class="small-font" >  IT IS TRUE ONLY BETWEEN 1 TO 8 </p>' , unsafe_allow_html = True )



st.markdown( '<p class="big-font"> H5- houses with 3 bathrooms have a MoM (Month over Month) growth of 15% </p>' , unsafe_allow_html = True)

aux51 = df[df['bathrooms'] == 3 ]
aux5 = aux51[['price','month']].groupby( 'month' ).mean().reset_index()

fig5 = px.line(aux5, x ='month', y ='price', template='seaborn',
              labels={'month' : 'Month of Year ',
                      'price': 'Price on average'},height = 600, width = 1200)


fig5.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        
    
    )
)

st.plotly_chart( fig5 )

st.markdown('<p class="small-font"; color: red;  >  False </p>' , unsafe_allow_html = True )



