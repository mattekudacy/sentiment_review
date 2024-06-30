import streamlit as st

def about():
    st.set_page_config(page_title='About', page_icon='📗')
    with open('README.md', 'r') as f:
        about_text = f.read()
    st.write(about_text)


if __name__ == '__main__':
    about()