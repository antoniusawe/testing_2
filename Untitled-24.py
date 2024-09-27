#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import streamlit as st


# In[9]:

# Membaca file CSV dari tautan raw GitHub
url = 'https://github.com/antoniusawe/testing_2/blob/main/data%20karyawan%20aktif%20per%2026%20September%202024.csv'
df = pd.read_csv(url, encoding='ISO-8859-1', on_bad_lines='skip')

# Menampilkan judul di aplikasi Streamlit
st.title("Data Karyawan Aktif per 26 September 2024")

# Menampilkan data dalam tabel menggunakan Streamlit
st.write(df)

