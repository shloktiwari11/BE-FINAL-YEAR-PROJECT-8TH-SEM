import os
import pickle
import streamlit as st
st.set_page_config(page_title='Fake Social Media Profile Detection',
                   layout='wide',
                   page_icon=":robot_face")
xgb=pickle.load(open(r"xgb2.sav",'rb'))


st.title("Fake Social Media Profile Detection using Machine Learning")
col1,col2=st.columns(2)
with col1:   
    pos=st.text_input("No. of posts")
    flg=st.text_input('No. of account followed')
    lin=st.text_input("URL in description(1 or 0)")
    hc=st.text_input("Average no. of hashtags used in the post")
with col2:
    flw=st.text_input('No. of followers')
    bl=st.text_input("No. of words in description")
    fo=st.text_input("Average no. of followers hunting keywords in hashtags (follow, like, followback)")
    pr=st.text_input("Average no. of promotional keywords in hashtags like (contest, repost, giveaway, mention, share,  quiz)")

result=''
if st.button("Predict"):
    user_input=[bl,lin,pos,flw,flg,pr,fo,hc]
    user_input=[float(x) for x in user_input]
    prediction=xgb.predict([user_input])
    if prediction==1:
        result="Profile is fake"
    else:
        result="Profile is not fake"
st.success(result)
