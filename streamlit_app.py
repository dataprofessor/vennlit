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
        # Making the Venn diagram plot
        st.subheader('Output')
        fig, ax = plt.subplots()
        venn2([set(list1), set(list2)], (list1_name, list2_name))
        plt.figure(figsize=(5, 2))
        plt.show()
        st.pyplot(fig)

        # Compute list stats
        st.subheader('List info')
        # Common elements
        common_elements = set(list1).intersection(list2)
        common_elements = list(common_elements)
        common_size = len(common_elements)
        if st.button('Common elements'):
            st.write('Size: ', common_size)
            st.write('Elements: ', set(common_elements))

        # List differences
        list1 = set(list1)
        list2 = set(list2)
        list1_unique = list1.difference(list2)
        list2_unique = list2.difference(list1)
        list1_size = len(list1_unique)
        list2_size = len(list2_unique)
        if st.button('List 1'):
            st.write('List 1 unique: ', list1_size)
            st.write('List 1: ', list1_unique)
        if st.button('List 2'):
            st.write('List 2 unique: ', list2_size)
            st.write('List 2: ', list2_unique)

        # Download CSV
        st.subheader('Download data')
        def download_data(input_list, list_name):
            df = pd.DataFrame()
            list_name_2 = list_name.replace(' ', '_')
            df[list_name_2] = pd.Series(list(input_list))
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"{list_name} CSV",
                data=csv,
                file_name=f'{list_name_2}.csv',
                mime='text/csv',
            )

        download_data(list1, 'List 1')
        download_data(list2, 'List 2')
        download_data(common_elements, 'Common elements')

    else:
        st.info('☝️ Enter data to proceed!')

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
        # Making the Venn diagram plot
        st.subheader('Output')
        fig, ax = plt.subplots()
        venn3([set(list1), set(list2), set(list3)], (list1_name, list2_name, list3_name))
        plt.figure(figsize=(5, 2))
        plt.show()
        st.pyplot(fig)

        # Compute list stats
        st.subheader('List info')
        
        # Convert to sets for set operations
        set1 = set(list1)
        set2 = set(list2)
        set3 = set(list3)

        # Calculate all possible intersections
        common_all = set1.intersection(set2, set3)
        common_1_2 = set1.intersection(set2) - set3
        common_1_3 = set1.intersection(set3) - set2
        common_2_3 = set2.intersection(set3) - set1

        # Calculate unique elements
        unique_1 = set1 - set2 - set3
        unique_2 = set2 - set1 - set3
        unique_3 = set3 - set1 - set2

        # Display buttons for viewing different intersections
        if st.button('Common elements (all lists)'):
            st.write('Size: ', len(common_all))
            st.write('Elements: ', common_all)
        
        if st.button('Common elements (Lists 1 & 2)'):
            st.write('Size: ', len(common_1_2))
            st.write('Elements: ', common_1_2)
            
        if st.button('Common elements (Lists 1 & 3)'):
            st.write('Size: ', len(common_1_3))
            st.write('Elements: ', common_1_3)
            
        if st.button('Common elements (Lists 2 & 3)'):
            st.write('Size: ', len(common_2_3))
            st.write('Elements: ', common_2_3)

        # Display buttons for unique elements
        if st.button('List 1 unique'):
            st.write('Size: ', len(unique_1))
            st.write('Elements: ', unique_1)
            
        if st.button('List 2 unique'):
            st.write('Size: ', len(unique_2))
            st.write('Elements: ', unique_2)
            
        if st.button('List 3 unique'):
            st.write('Size: ', len(unique_3))
            st.write('Elements: ', unique_3)

        # Download function
        st.subheader('Download data')
        def download_data(input_list, list_name):
            df = pd.DataFrame()
            list_name_2 = list_name.replace(' ', '_')
            df[list_name_2] = pd.Series(list(input_list))
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"{list_name} CSV",
                data=csv,
                file_name=f'{list_name_2}.csv',
                mime='text/csv',
            )

        # Download buttons for all combinations
        download_data(unique_1, 'List 1 unique')
        download_data(unique_2, 'List 2 unique')
        download_data(unique_3, 'List 3 unique')
        download_data(common_all, 'Common all lists')
        download_data(common_1_2, 'Common lists 1 and 2')
        download_data(common_1_3, 'Common lists 1 and 3')
        download_data(common_2_3, 'Common lists 2 and 3')

    else:
        st.info('☝️ Enter data to proceed!')
