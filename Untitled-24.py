#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import streamlit as st


# In[9]:

# Membaca file CSV dari tautan raw GitHub
url = 'https://raw.githubusercontent.com/antoniusawe/testing_2/main/data%20karyawan%20aktif%20per%2026%20September%202024.csv'
df = pd.read_csv(url, encoding='ISO-8859-1')

df['Nik'] = df['Nik'].astype(str).str.replace(',', '')
df['Nik'] = df['Nik'].str.zfill(6)

# Menampilkan judul di aplikasi Streamlit
st.title("Data Karyawan Aktif per 26 September 2024")

# Menambahkan filter berdasarkan kolom Position, Region, Area, dan Worklocation
position = st.selectbox('Filter by Position', options=['All'] + sorted(df['Position'].unique()))
region = st.selectbox('Filter by Region', options=['All'] + sorted(df['Region'].unique()))
area = st.selectbox('Filter by Area', options=['All'] + sorted(df['Area'].unique()))
worklocation = st.selectbox('Filter by Worklocation', options=['All'] + sorted(df['Worklocation'].unique()))

# Filter dataframe berdasarkan pilihan pengguna
if position != 'All':
    df = df[df['Position'] == position]

if region != 'All':
    df = df[df['Region'] == region]

if area != 'All':
    df = df[df['Area'] == area]

if worklocation != 'All':
    df = df[df['Worklocation'] == worklocation]

# Menampilkan data dalam tabel menggunakan Streamlit
st.write(df)

