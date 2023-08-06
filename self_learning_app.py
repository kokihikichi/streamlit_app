import streamlit as st
import os

# Function to read markdown content
def read_markdown_file(markdown_file):
    with open(markdown_file, 'r') as file:
        content = file.read()
    return content

# List all markdown files in the current directory
markdown_files = [f for f in os.listdir() if f.endswith('.md')]

# Create the Streamlit app
st.title("Markdown Viewer")

# Dropdown menu for file selection
selected_file = st.selectbox("Choose a markdown file", markdown_files)

# Display the selected markdown file
content = read_markdown_file(selected_file)
st.markdown(content, unsafe_allow_html=True)
