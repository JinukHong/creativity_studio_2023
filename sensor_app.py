
from collections import MutableSet


import streamlit as st
import pandas as pd
import numpy as np
import datetime

import collections


# Generate dummy data
def generate_data():
    time_range = pd.date_range(start="now", periods=60, freq="T")  # Every minute for an hour
    temperature = np.random.uniform(20, 30, 60)  # Random temperature values between 20 and 30
    pH = np.random.uniform(6.5, 7.5, 60)  # Random pH values between 6.5 and 7.5
    return pd.DataFrame({
        "Time": time_range,
        "Temperature": temperature,
        "pH": pH
    })

data = generate_data()

import streamlit as st
import pandas as pd
import numpy as np
import datetime



data = generate_data()

# Mock GPT-based API
def get_gpt_response(message, context):
    # In a real scenario, this function would call the GPT API and get a response.
    # For this example, if the message contains "temperature", we return the latest temperature.
    if "temperature" in message.lower():
        return f"The latest temperature reading is {context['Temperature']}°C."
    elif "ph" in message.lower():
        return f"The latest pH reading is {context['pH']}."
    else:
        return "I'm sorry, I don't understand that."

# Streamlit app
st.title('Arduino Sensor Data and Chatbot')
st.write('Displaying dummy data for temperature and pH levels.')

# Plot temperature
st.subheader('Temperature over Time')
st.line_chart(data.set_index('Time')['Temperature'])

# Plot pH
st.subheader('pH Level over Time')
st.line_chart(data.set_index('Time')['pH'])

# Chatbot interface
st.subheader('Ask the Secretary Bot')
user_message = st.text_input("Your message:")
if user_message:
    # Get the latest data as context
    context = {
        'Temperature': data['Temperature'].iloc[-1],
        'pH': data['pH'].iloc[-1]
    }
    bot_response = get_gpt_response(user_message, context)
    st.write(f"Secretary Bot: {bot_response}")
