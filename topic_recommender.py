from bs4.dammit import html_meta
import pandas as pd
import streamlit as st
import re
import requests
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
from lxml import html

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

st.title("""Topic Recommender""")

with st.form(key='my_form'):
    keyword = st.text_input(label = 'Type any Topic (E.g. Marketing)')
    submit_button = st.form_submit_button(label = 'Recommend Topics')

# keyword = 'seo'
input_keyword = keyword.replace(" ", "+")
# st.write(input_keyword)

# url = 'https://www.bing.com/search?q=probability'
url = ('https://www.bing.com/search?q='+input_keyword+'&form=QBLH&sp=-1')
print(url)
# st.write(url)
# response = requests.get(url)
# print(response)

response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, 'lxml')

result_list = []

all_topics = []

for container in soup.select('.b_algo h2 a'):
    link = container['href']
    # print(f"{link}\n")
    # st.write(link)

    request = requests.get(link)
    Soup = BeautifulSoup(request.text, "lxml")
    heading_tags = ["h1","h2","h3","h4"]

    # all_topics = []

    for tags in Soup.find_all(heading_tags):
        topics = tags.text.strip()
        if keyword.lower().split(' ', 1)[0] in topics.lower():
            all_topics.append(topics.title())
            # st.write(topics)
            # print(all_topics)
            # print(topics) 
if all_topics:
    df = pd.DataFrame(all_topics)
    st.write(df[0].unique())
    st.success('Done!')
        
st.write("\n")
st.write("\n")
st.write("\n")

st.write("@author: abhishek.shukla")
st.write("Facing issues?")
href2 = f'<a href="https://www.linkedin.com/in/abhishekshukla01/">DM me on Linkedin</a>'
href3 = f'<a href="https://twitter.com/StanAbK">DM me on Twitter</a>'
st.markdown(href2, unsafe_allow_html=True)
st.markdown(href3, unsafe_allow_html=True)