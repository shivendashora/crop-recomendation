import streamlit as st
import pickle
st.cache_data
st.title('Crop Recommender')
model = pickle.load(open('model.pkl','rb'))
N=st.number_input("Enter N")
P=st.number_input("Enter P")
K=st.number_input("Enter K")
temperature=st.number_input("Enter temperature")
humidity=st.number_input("Enter humidity")
ph=st.number_input("Enter ph")
rainfall=st.number_input("Enter rainfall")
button =st.button("click for predection")
if button:
       y_pred = model.predict([[N,P, K, temperature, humidity, ph, rainfall]])
       st.write("the predicted crop can be grown is ")
       st.write(y_pred[0])



