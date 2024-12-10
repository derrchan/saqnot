import streamlit as st

# Hardcoded login credentials
LOGIN_CREDENTIALS = {
    "username": "admin",
    "password": "admin"
}

def authenticate(username, password):
    """Authenticate user credentials"""
    return username == LOGIN_CREDENTIALS["username"] and password == LOGIN_CREDENTIALS["password"]

def main_page():
    """Display main page"""
    st.title("Surgery SAQ")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            sidebar()
        else:
            st.error("Invalid username or password")

def sidebar():
    """Display sidebar with hyperlinks"""
    with st.sidebar:
        st.write("[M23Q1](https://huggingface.co/spaces/derrickchan223/saqtestdemo)")
        st.write("[M23Q2](https://www.yahoo.com)")
        st.write("[M23Q3](https://www.baidu.com)")

def main():
    main_page()

if __name__ == "__main__":
    main()
