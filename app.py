
import streamlit as st 
import pandas as pd
import streamlit as st
import pandas as pd 
import altair as alt

#

st.write("HELLO")
st.write("TOCHUKWU")
st.write("DONALD")
st.write("JEMILAT")
st.write("ROTIMI")

# 3. Add an interactive element (a button)
if st.button("Click me!"):
    st.write("You clicked the button! Great job.")
# 4. (Optional) Since I see you have an 'incidents.csv' file, 
# here is how you can quickly display it:
st.subheader("Data Preview")
try:
    # Load the data
    df = pd.read_csv("incidents.csv")
    # Display it as an interactive dataframe
    st.dataframe(df.head())
except FileNotFoundError:
    st.write("No 'incidents.csv' file found in the current directory.")

