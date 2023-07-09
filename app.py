import streamlit as st
import requests
import numpy as np
import pandas as pd
from fast import predict

st.markdown("""# This is a header
## This is a sub header
This is text""")

Number_one = st.number_input('Number One')
Number_two = st.number_input('Number Two')
Number_three = st.number_input('Number three')


params ={
    'Number_one': f'{Number_one}',
    "Number_two": f'{Number_two}',
    'Number_three': f'{Number_three}',
}


url = f'http://127.0.0.1:8000/?Number_one={Number_one}&Number_two={Number_two}&Number_three={Number_three}'


if st.button('click me'):
    
    response = requests.get(url,params=params)
    
    price = response.json()['Estimate_price']
    #print(price)
    st.header(f'Estimate Price: ${round(price, 2)}')
    #st.header(f"Estimate price: ${round(price['Estimate_price'], 2)}")
        # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked 😞')
