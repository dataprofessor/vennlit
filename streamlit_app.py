import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import pandas as pd

st.header('⭕ VennLit')

with st.expander('About this App'):
    st.write('''
    This app allows you to create Venn diagrams.

    Libraries used:
    - `streamlit`
    - `matplotlib`
    - `matplotlib_venn`
    - `pandas`
    ''')

# Navigation
with st.sidebar:
    page = st.radio('Choose', ['2 Lists', '3 Lists'])

# Venns Diagram - 2 Lists
if page == '2 Lists':

    st.subheader('Input')
    col1, col2 = st.columns(2)

    with col1:
        list1 = st.text_area('List 1').split()
        list1_name = st.text_input('List 1 name')
    with col2:
        list2 = st.text_area('List 2').split()
        list2_name = st.text_input('List 2 name')


    if (list1 != []) and (list2 != []):
        # Making the Venn diagram plot
        st.subheader('Output')

        fig, ax = plt.subplots()

        venn2([set(list1), set(list2)], (list1_name, list2_name) )

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
                file_name='list1.csv',
                mime='text/csv',
            )

        download_data(list1, 'List 1')
        download_data(list2, 'List 2')
        download_data(common_elements, 'Common elements')
        
    else:
        st.info('☝️ Enter data to proceed!')


# Venns Diagram - 3 Lists
if page == '3 Lists':
    st.subheader('Input')
    col1, col2, col3 = st.columns(3)

    with col1:
        list1 = st.text_area('List 1').split()
        list1_name = st.text_input('List 1 name')
    with col2:
        list2 = st.text_area('List 2').split()
        list2_name = st.text_input('List 2 name')
    with col3:
        list3 = st.text_area('List 3').split()
        list3_name = st.text_input('List 3 name')

    if (list1 != []) and (list2 != []) and (list3 != []):
        # Making the Venn diagram plot
        st.subheader('Output')

        fig, ax = plt.subplots()

        venn3([set(list1), set(list2), set(list3)], (list1_name, list2_name, list3_name))

        plt.figure(figsize=(5, 2))
        plt.show()
        st.pyplot(fig)

        # Compute list stats
        common_elements = set(list1).intersection(list2)
        common_elements = list(common_elements)

        common_size = len(common_elements)

        if st.button('Common elements'):
            st.write('Common elements: ', common_elements)
        st.write('Common size: ', common_size)
    else:
        st.info('☝️ Enter data to proceed!')