
import streamlit as st 
import pandas as pd
import streamlit as st
import pandas as pd 
import altair as alt

# function to load data 
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)

    df.columns = df.columns.str.lower()

    event_list = []
    location_list = []

    for i in df['title'].astype(str):
        rows = [p.strip() for p in i.split(",")]

   
        if len(rows) > 1:
            event_list.append(rows[0])
            location_list.append(rows[-1])
        else:
            event_list.append(rows[0])
            location_list.append(None)


    df['incident']= event_list
    df['location'] = location_list

    return df

# function to display the data 
def display_data(df):
    st.title("Incidents Data Analysis")

    st.write("Shape of dataset:", df.shape)

    
    
