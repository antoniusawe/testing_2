#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import streamlit as st


# In[9]:


df = pd.read_csv(r"C:\Users\078220\Downloads\data karyawan aktif per 26 September 2024.csv", encoding='ISO-8859-1')


# In[10]:


# Menampilkan judul di aplikasi Streamlit
st.title("Data Karyawan Aktif per 26 September 2024")
st.write(df)

