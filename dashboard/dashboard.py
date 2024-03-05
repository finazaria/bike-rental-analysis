import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
@st.cache
def load_data():
    return pd.read_csv("day.csv")

df_day = load_data()

# Set page title and description
st.title('Bike Sharing Dataset Analysis')
st.write("""
## Menentukan Pertanyaan Bisnis
- Pertanyaan 1 : Di bulan apakah sepeda paling banyak dirental?
- Pertanyaan 2 : Di musim apakah sepeda paling banyak dirental?
- Pertanyaan 3 : Di hari apakah sepeda paling banyak dirental?
- Pertanyaan 4 : Apakah cuaca mempengaruhi jumlah sepeda yang dirental?
- Pertanyaan 5 : Bagaimana temperatur mempengaruhi jumlah sepeda yang dirental?
""")

# Data Wrangling

# Convert 'dteday' to datetime format
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Exploratory Data Analysis

# Pertanyaan 1
st.write('### Pertanyaan 1: Di bulan apakah sepeda paling banyak dirental?')
monthly_counts = df_day.groupby('mnth')['cnt'].sum()
st.line_chart(monthly_counts)

# Pertanyaan 2
st.write('### Pertanyaan 2: Di musim apakah sepeda paling banyak dirental?')
seasonal_counts = df_day.groupby('season')['cnt'].sum()
st.bar_chart(seasonal_counts)

# Pertanyaan 3
st.write('### Pertanyaan 3: Di hari apakah sepeda paling banyak dirental?')
daily_counts = df_day.groupby('weekday')['cnt'].sum()
st.bar_chart(daily_counts)

# Pertanyaan 4
st.write('### Pertanyaan 4: Apakah cuaca mempengaruhi jumlah sepeda yang dirental?')
weather_counts = df_day.groupby('weathersit')['cnt'].mean()
st.bar_chart(weather_counts)

# Pertanyaan 5
st.write('### Pertanyaan 5: Bagaimana temperatur mempengaruhi jumlah sepeda yang dirental?')
st.scatter_chart(df_day, x='temp', y='cnt')

# Conclusion
st.write('## Conclusion')
st.write("""
### Conclusion Pertanyaan 1: "Di bulan apakah sepeda paling banyak dirental?"
- Sepeda paling banyak dirental di bulan Agustus. Kemudian disusul oleh bulan Juni, lalu September.
- Secara keseluruhan, rata-rata sepeda banyak dirental di periode antara bulan Mei hingga Oktober

### Conclusion Pertanyaan 2: "Di musim apakah sepeda paling banyak dirental?"
- Sepeda paling banyak dirental di Musim Gugur. Kemudian disusul oleh Musim Panas, Salju, dan terakhir Musim Semi.

### Conclusion Pertanyaan 3: "Di hari apakah sepeda paling banyak dirental?"
- Sepeda paling banyak dirental di hari Sabtu. Kemudian disusul oleh hari Jumat, dan lalu hari Minggu.

### Conclusion Pertanyaan 4: "Apakah cuaca mempengaruhi jumlah sepeda yang dirental?"
- Iya, cuaca mempengaruhi jumlah sepeda yang dirental
- Sepeda paling banyak dirental pada saat cuaca Cerah. Dan kemudian diikuti oleh cuaca mendung, lalu saat cuaca hujan atau salju ringan
- Tidak terdapat record rental sepeda pada saat hujan atau salju lebat

### Conclusion Pertanyaan 5: "Bagaimana temperatur mempengaruhi jumlah sepeda yang dirental?"
- Berdasarkan scatterplot di atas, dapat dilihat bahwa rental sepeda cenderung lebih banyak saat keadaan temperatur yang lebih hangat atau panas. Dengan frekuensi rental sepeda paling tinggi pada saat temperatur ±24 celcius (41*0.6 celcius)
""")

# Optional: Display raw data
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df_day)
