import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import pandas as pd

# Define sample data
def load_sample_data():
    try:
        with open('data/list_a.txt', 'r') as f:
            list_a = f.read()
        with open('data/list_b.txt', 'r') as f:
            list_b = f.read()
        with open('data/list_c.txt', 'r') as f:
            list_c = f.read()
        return {
            'List A': list_a,
            'List B': list_b,
            'List C': list_c
        }
    except FileNotFoundError:
        st.error("Sample data files not found. Please ensure lista.txt, listb.txt, and listc.txt are in the same directory as the script.")
        return None

SAMPLE_DATA = load_sample_data()

# Function to clean text by removing quotes
def clean_text(text):
    # Remove both single and double quotes
    cleaned = text.replace('"', '').replace("'", '')
    return cleaned

# Function to process text area input
def process_text_area(text):
    # First clean the text to remove quotes
    cleaned_text = clean_text(text)
    # Split the text into a list
    return [item.strip() for item in cleaned_text.split() if item.strip()]

# Initialize session state for text areas
if 'list1_content' not in st.session_state:
    st.session_state.list1_content = ''
if 'list2_content' not in st.session_state:
    st.session_state.list2_content = ''
if 'list3_content' not in st.session_state:
    st.session_state.list3_content = ''

st.header('⭕ VennLit')

st.warning('''
    This app allows you to create Venn diagrams.
    Libraries used:
    - `streamlit`
    - `matplotlib`
    - `matplotlib_venn`
    - `pandas`
    ''')

# Navigation and Sample Data buttons
with st.sidebar:
    st.subheader('Type of Venn diagram')
    page = st.radio('Choose', ['2 Lists', '3 Lists'])
    
    st.divider()
    
    st.subheader('Sample Data')
    col1, col2 = st.columns(2)
    
    # Sample data button
    with col1:
        if st.button('Load Data', use_container_width=True):
            st.session_state.list1_content = SAMPLE_DATA['List A']
            st.session_state.list2_content = SAMPLE_DATA['List B']
            st.session_state.list3_content = SAMPLE_DATA['List C']
    
    # Clear data button
    with col2:
        if st.button('Clear Data', use_container_width=True):
            st.session_state.list1_content = ''
            st.session_state.list2_content = ''
            st.session_state.list3_content = ''

# Venn Diagram - 2 Lists
if page == '2 Lists':
    st.subheader('Input')
    col1, col2 = st.columns(2)
    with col1:
        list1 = process_text_area(st.text_area('List 1', value=st.session_state.list1_content))
        list1_name = st.text_input('List 1 name', value='List A')
    with col2:
        list2 = process_text_area(st.text_area('List 2', value=st.session_state.list2_content))
        list2_name = st.text_input('List 2 name', value='List B')

    if (list1 != []) and (list2 != []):
        # Rest of the 2 Lists code remains the same
        [Previous 2-list code section remains exactly the same]

# Venn Diagram - 3 Lists
if page == '3 Lists':
    st.subheader('Input')
    col1, col2, col3 = st.columns(3)
    with col1:
        list1 = process_text_area(st.text_area('List 1', value=st.session_state.list1_content))
        list1_name = st.text_input('List 1 name', value='List A')
    with col2:
        list2 = process_text_area(st.text_area('List 2', value=st.session_state.list2_content))
        list2_name = st.text_input('List 2 name', value='List B')
    with col3:
        list3 = process_text_area(st.text_area('List 3', value=st.session_state.list3_content))
        list3_name = st.text_input('List 3 name', value='List C')

    if (list1 != []) and (list2 != []) and (list3 != []):
        # Rest of the 3 Lists code remains the same
        [Previous 3-list code section remains exactly the same]
