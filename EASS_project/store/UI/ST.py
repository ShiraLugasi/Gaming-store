import streamlit as st
import requests


def main():
    st.title("HELLO ,You are welcome to share with us an idea for a new/old game 🎮")
    st.write("Write the newest game you would like to buy:")
    new_game = st.text_input("New Game")
    platform = st.selectbox("Select the platform:", ("PC", "Mobile", "PlayStation"))
    main_actions = st.text_area("Main actions of the game")
    
    if st.button("Submit"):
        response = requests.post('http://backend:8000/games/', json={'name': new_game, 'platform': platform, 'main_actions': main_actions})
        if response.status_code == 200:
            st.success("New game submitted successfully! Maybe your game idea will be in stores soon... 🚀")
        else:
            st.error(f"An error occurred while submitting the game: {response.text}")

    st.write("Feel free to share any CRAZY idea")


if __name__ == "__main__":
    main()


