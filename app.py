import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Başlık ekleme
st.title("Basit Bir Grafik Örneği")

# Veri oluşturma
data = {
    'Günler': ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma'],
    'Değerler': [3, 6, 7, 8, 5]
}
df = pd.DataFrame(data)

# Tabloyu gösterme
st.write("Veriler:")
st.write(df)

# Grafik çizme
fig, ax = plt.subplots()
ax.plot(df['Günler'], df['Değerler'], marker='o')
ax.set_title("Haftalık Değerler Grafiği")
ax.set_xlabel("Günler")
ax.set_ylabel("Değerler")

# Grafik görselleştirme
st.pyplot(fig)