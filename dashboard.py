import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


###################################################################
#DATA 
hour_df = pd.read_csv('Bike-sharing-dataset/hour.csv')
day_df = pd.read_csv('Bike-sharing-dataset/day.csv')

columns = ['season','yr', 'mnth', 'holiday', 'weekday', 'weathersit','workingday']
 
for column in columns:
    day_df[column] =  day_df[column].astype("category")
    hour_df[column] =  hour_df[column].astype("category")

hour_df.season.replace((1,2,3,4), ('Spring','Summer','Fall','Winter'), inplace=True)
day_df.season.replace((1,2,3,4), ('Spring','Summer','Fall','Winter'), inplace=True)

hour_df.mnth.replace((1,2,3,4,5,6,7,8,9,10,11,12), ('Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov','Des'), inplace=True)
day_df.mnth.replace((1,2,3,4,5,6,7,8,9,10,11,12), ('Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov','Des'), inplace=True)

hour_df.weathersit.replace((1,2,3,4), ('Clear', 'Misty_Cloudy', 'Light_RainSnow','Heavy_RainSnow'), inplace=True)
day_df.weathersit.replace((1,2,3,4), ('Clear', 'Misty_Cloudy', 'Light_RainSnow','Heavy_RainSnow'), inplace=True)

hour_df.yr.replace((0,1),('2011','2012'), inplace=True)
day_df.yr.replace((0,1), ('2011','2012'), inplace=True)

hour_df.holiday.replace((0,1), ('Holiday', 'Not_Holiday'), inplace=True)
day_df.holiday.replace((0,1), ('Holiday', 'Not_Holiday'), inplace=True)

hour_df.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)
day_df.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)

hour_df.workingday.replace((0,1), ('Workingday',"Not_workingday"), inplace=True)
day_df.workingday.replace((0,1), ('Workingday',"Not_workingday"), inplace=True)

###########################################################################################

#Title of Dashboard
st.markdown(
    """
    <style>
    .title {
        text-align: left;
        font-size: 65px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Visualisasi Bike-Share</h1>", unsafe_allow_html=True)


with st.sidebar:
    st.title('Insight')
    with st.expander('What is Bike-Share?'):
        st.write('Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, environmental and health issues.')
        st.image("https://i.pinimg.com/564x/34/c1/44/34c144684eb689c10fbce2d49e6a12f7.jpg")
        st.image("https://i.pinimg.com/564x/27/ca/3f/27ca3f46eaf8d3ffc4219fec35364162.jpg")



st.subheader("Dalam Visualisasi ini kita dapat melihat 4 visualisasi data Bike-Share")
st.subheader("So, please ENJOY!")

with st.expander('Open me for more info><'):
    st.write('Silahkan buka sidebar untuk melihat insight mengenai "Apa itu Bike-Share?"')

#Column
col1, col2 = st.columns([6, 6])
 
with col1:
    st.header("Jumlah Penyewaan Sepeda Tahun 2011 dan 2012")
    #Visualisasi pertanyaan 1
    sns.barplot(
        x='yr',
        y='cnt',
        data=day_df,
        palette='pastel')

    plt.title('Jumlah Penyewaan Sepeda Tahun 2011-2012')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot()

    with st.expander('Apa sih arti grafik ini?'):
        st.write('Grafik ini menjelaskan mengenai Jumlah Penyewaan Sepeda pada usaha Bike-Share pada tahun 2011 dan 2012. Bisa dilihat kalau grafik Tahun 2012 lebih tinggi ya dibanding 2011, hal ini berarti terjadi peningkatan penyewaan sepeda pada tahun 2012 dibanding tahun 2011.')


    st.header("Proporsi Pengguna Terdaftar dan Tidak")
    casual = sum(day_df['casual'])
    registered = sum(day_df['registered'])
    data = [casual, registered]
    labels = ['Casual', 'Registered']
    plt.pie(data, labels=labels, autopct='%1.1f%%', colors=['#92C6FF', '#97F0AA'])
    st.pyplot()

    with st.expander('Loh ini apalagi artinya?'):
        st.write('Nah kalau ini proporsi pengguna terdaftar dan tidak dari seluruh pengguna Bike-Share. Tau ngga sih? ternyata lebih dari 80% pengguna Bike-Share itu termasuk pengguna terdaftar lho! Sementara itu, masih ada 18,8% pengguna Bike-Share yang masih belum terdaftar menjadi pengguna.')

with col2:
    st.header('Jumlah Penyewaan Sepeda Berdasarkan Hari')
    sns.barplot(
        x='weekday',
        y='cnt',
        data=day_df,
        palette='pastel')

    plt.title('Jumlah Penyewaan Sepeda berdasarkan Hari')
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot()
    with st.expander('Wah kalau ini apa maksudnya ya?'):
        st.write('Kalian tau ga hari apa orang-orang paling banyak dan paling sedikit make Bike-Share? Nah jawabannya bisa dilihat dari grafik ini! Kalau kita lihat, hari Jumat tuh grafiknya paling tinggi kan? Artinya hari Jumat tuh hari dimana orang paling banyak make Bike-Share. Sedangkan kalau hari yang paling dikit, apa coba? Yup bener! Hari Minggu!')

    st.header('Jumlah Penyewaan Sepeda berdasarkan Musim')
    sns.barplot(
        x='season',
        y='cnt',
        data=day_df,
        palette='pastel')

    plt.title('Jumlah Penyewaan Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot()
    with st.expander('Apa nih bedanya sama yang di atas?'):
        st.write('Beda dong! Grafik ini memvisualisasikan jumlah penyewaan sepeda berdasarkan musim. Kalau dilihat dari grafik, keliatan kan kalo penyewaan sepeda paling banyak terjadi waktu musim gugur atau Fall, sedangkan penyewaan sepeda paling sedikit terjadi pada musim semi atau Spring.')




st.title('Terima Kasih Sudah Berkunjung!')



st.set_option('deprecation.showPyplotGlobalUse', False)



