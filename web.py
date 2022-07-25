import streamlit as st
import pandas as pd
import numpy as np
from st_on_hover_tabs import on_hover_tabs
st.set_page_config(layout="wide")

st.title("WhyNotCode.in")
st.subheader("About Sandipan Basu")


ss = """

Energetic and self-driven technologists worked on many successful greenfield projects. Have worked on a wide range of tech from Map-based information systems (GIS) to Network Management Systems (NMS), from Enterprise Application Integration (EAI) projects using TIBCO, Oracle AquaLogic suite etc to Recommendation Systems, systems using Stats NLP to build a conversation middleware platform supporting multi-AI/multi-channel cloud / on-prem, believer in intelligence-everywhere. Worked with small and big data, EDA techniques, insights, visualization frameworks and platforms, and machine learning pipelines.

Machine learning will/is change(ing) everything. I believe all the products we have been building in the past 2 decades will be changed from application logic+language to data+ML at the core. This shift will be so epic that this will spawn totally new sets of organizations and will need new sets of people with enough experience and openness to ride and guide. Those days are not too far where “hello world” programs will output only automated models and machine learning will be taught in junior classes along with their algebra courses.

Currently conducting Machine Learning and AI courses! In case you are interested to know more or you want to transform your non ML workforce into ML literates, buzz me - sandipan_at_whynotcode_dot_in

Specialties: Architecture, Polyglot, Search and Recommendation Systems, Conversation Artificial Intelligence, Machine Learning, Big Data, Chatbots, Voice Channels like Alexa / Google Assistance - Web Application Development, Startups, Engineering, Products, Teaching
"""

st.text(ss)
ls = 'https://www.crazygames.com/game/soccer-legends-2021'




url = ('https://in.linkedin.com/in/sandipanbasu')
st.write("His linkedin is [Sandipan's Linkedin, Click here](%s)" %url)
with st.sidebar:
    tabs = on_hover_tabs(tabName=['Sandipans Den', 'The 11 yr old museum', 'The Serious Stuff(Totally not)'], 
                         iconName=['house', 'museum', 'controller'], default_choice=0)
print(tabs)

if tabs =='Sandipans Den':
    st.title("This Is Sandipan's Den")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'The 11 yr old museum':
    st.title("The world famous 11 yr old museum !")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'The Serious Stuff(Totally not)':
    st.title("Games people like and play")
    st.subheader('Soccer Legends')
    st.write("""Soccer Legends is a fun game which,true to it's name, 
    is all about soccer.There are a number of different gamemodes 
    and teams to choose from. Have fun playing ! 
    [Click here to play]({})
    """.format (ls))
