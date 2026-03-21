
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

    #ADD A FILTER
    filters = {"incident": df['incident'].unique(),
    "location": df['location'].unique()}

    #user selection
    selected_filters = {}

    #generate multi - select widgets dynamically 
    for key,options in filters.items():
        selected_filters[key] = st.sidebar.multiselect(key, options)

    #parse the filters content into a dataframe 
    df= df.copy()

    #apply filtered selection to the data
    for key, selected_values in selected_filters.items():
        if selected_values:
            df = df[df[key].isin(selected_values)]

    #add some streamlit columns to show metrics 
    no_of_incidents = df.shape[0]
    no_of_deaths = df['number of deaths'].sum()

    #columns 
    col1, col2,= st.columns(2)

    with col1:
        st.metric("No. of Incidents", no_of_incidents)

    with col2:
        st.metric("no. of death", no_of_deaths)
        #st.write(df.describe())  

    st.dataframe(df.head(5))

    if st.checkbox("Show summary statistics"):
        st.write(df.describe()) 


    for col, selected_options in selected_filters.items():
        if selected_options:
            df = df[df[col].isin(selected_options)]
    
    for col, options in filters.items():
        selected_filters[col] = st.multiselect(f"Select {col}", options)

    #add some streamlit columns to show metrics 
    no_of_incidents = df.shape[0]
    no_of_deaths = df['number of deaths'].sum()

    #columns 
    col1, col2,= st.columns(2)

    with col1:
        st.metric("No. of Incidents", no_of_incidents)

    with col2:
        st.metric("no. of death", no_of_deaths)
        #st.write(df.describe())  
        
    st.dataframe(df.head(5))

    if st.checkbox("Show summary statistics"):
        st.write(df.describe())


#create some charts 
# #bar chart (altair charts )

    temp1 = df['incident'].value_counts().reset_index()
    st.dataframe(temp1)
    temp1 = temp1.nlargest(10, 'count')

    chart1 = alt.Chart(temp1).mark_bar().encode(
        x =alt.X('count:Q', title='Incident count'),
        y =alt.Y('incident:N'),

        ).properties(height=600)

    #display the chart
    st.altair_chart(chart1)
    #temp1.columns = ['incident', 'count']
    temp2 = df.groupby('location')['number of deaths'].sum().reset_index()

    temp2 = (temp2.nlargest(10, 'number of deaths').sort_values('number of deaths', ascending=False))

    chart2 = alt.Chart(temp2).mark_bar().encode(
        x =alt.X('number of deaths:Q', title='Number of deaths'),
        y =alt.Y('location:N', sort='-x'),
        color=alt.Color('location:N', legend=None)

        ).properties(height=600)

    #display the chart
    st.altair_chart(chart2)


def main():
    df = load_data("incidents.csv")
    display_data(df)


if __name__ == "__main__":
    main()#CONTROL + L FOR TERMINAL TO OPEN
#python -m venv .env

#Control v for to termminal to stop

#.env\Scripts\activate
