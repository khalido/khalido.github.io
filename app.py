import streamlit as st 
import os
import utils

#posts, tags = utils.get_posts()
posts, ft = utils.get_files()



def main():

    st.title("khalido")
    key = st.selectbox("Choose post", list(posts.keys()))
    st.markdown(posts[key])

if __name__ == "__main__":
    main()