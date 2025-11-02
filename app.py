import streamlit as st

def main():
    pg = st.navigation([
        st.Page('info.py', title="Home"),
        st.Page('generation.py', title="Generate"),
    ])
    pg.run()

if __name__ == "__main__":
    main()
