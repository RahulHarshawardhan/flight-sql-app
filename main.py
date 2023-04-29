import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from dbhelper import DB


db = DB()


st.sidebar.title('Flights Analytics')
user_option = st.sidebar.selectbox('Menu',['Select one', 'Check flights', 'Analytics'])

if user_option == 'Check flights':
    st.title("Check Flights")

    col1, col2 = st.columns(2)

    city = db.fetch_city_names()
    with col1:
       source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button("search"):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)

elif user_option == 'Analytics':
    ## Pie chart graph1
    st.title("Analytics")
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))
    st.header("Pie chart")
    st.plotly_chart(fig)
# Bar chart graph 2
    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1,
            )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# line chart graph3
    date, frequency2 = db.daily_frquency()
    fig = px.line(
        x=date,
        y=frequency2,
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title("Tell about the project")

