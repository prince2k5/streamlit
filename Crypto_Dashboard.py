import streamlit as st
import pandas as pd
import requests
import datetime

st.set_page_config(page_icon="📈", page_title="Crypto Dashboard")
st.button("Refresh")

st.sidebar.image(
    "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/z3ahdkytzwi1jxlpazje",
    width=50,
)

c1, c2 = st.columns([1, 8])

with c1:
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/chart-increasing_1f4c8.png",
        width=90,
    )

st.markdown(
    """# **Crypto Dashboard**
A simple cryptocurrency price app pulling price data from the [Binance API](https://www.binance.com/en/support/faq/360002502072), from [Data Professor](https://twitter.com/thedataprof).
"""
)

st.header("**Selected Price**")

# Load market data from Binance API
df = pd.read_json("https://api.binance.com/api/v3/ticker/24hr")
df_usdt=df[df['symbol'].str.endswith('USDT')]

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a


crpytoList = {
    "Price 1": "BTCUSDT",
    "Price 2": "ETHUSDT",
    "Price 3": "BNBUSDT",
    "Price 4": "FTTUSDT",
    "Price 5": "ADAUSDT",
    "Price 6": "DOGEUSDT",
    "Price 7": "AAVEUSDT",
    "Price 8": "DOTUSDT",
    "Price 9": "AVAXUSDT",
    "Price 10": "SOLUSDT",
    "Price 11": "DYDXUSDT",
    "Price 12": "LRCUSDT"
}

col1, col2, col3 = st.columns(3)

for i in range(len(crpytoList.keys())):
    selected_crypto_label = list(crpytoList.keys())[i]
    selected_crypto_index = list(df.symbol).index(crpytoList[selected_crypto_label])
    selected_crypto = st.sidebar.selectbox(
        selected_crypto_label, df.symbol, selected_crypto_index, key=str(i)
    )
    col_df = df_usdt[df_usdt.symbol == selected_crypto]
    col_price = round_value(col_df.weightedAvgPrice)
    col_percent = f"{float(col_df.priceChangePercent)}%"
    if i < 4:
        with col1:
            st.metric(selected_crypto, col_price, col_percent)
    if 3 < i < 8:
        with col2:
            st.metric(selected_crypto, col_price, col_percent)
    if i > 7:
        with col3:
            st.metric(selected_crypto, col_price, col_percent)



# st.download_button(
#    label="Download Binance data as CSV",
#    data=df_usdt,
#    file_name='large_df.csv',
#    mime='text/csv'
#    )

@st.cache
def convert_df(df_usdt):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df_usdt.to_csv().encode("utf-8")


csv = convert_df(df_usdt)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="Binance_Data_"+datetime.datetime.now().strftime('%d-%m-%Y_%H_%M')+".csv",
    mime="text/csv"
    )

df_final=df_usdt[['symbol','priceChangePercent','lastPrice']]

# col1, col2, col3 = st.columns(3)

# st.dataframe(df_final, height=2000)

df_top10=df_final.sort_values(by='priceChangePercent')
with col1:
    st.write('Top 10')
    st.table(df_top10.tail(10).sort_values(by='priceChangePercent',ascending=False))
with col3:
    st.write('Bottom 10')
    st.table(df_top10.head(10))
    # st.dataframe(df_top10.head(10))

st.subheader('FTX Leverages Tokens')

data=requests.get('https://ftx.com/api/markets').json()
data_lt=requests.get('https://ftx.com/api/lt/tokens').json()

data1=data['result']
data_lt1=data_lt['result']

df=pd.DataFrame(data1)
df_lt=pd.DataFrame(data_lt1)

df.name=df.name.replace('/USD','')
df1=df[df.isEtfMarket]
df2=df1[df1.name.str.contains('BULL') | df1.name.str.contains('BEAR')]
df2['change24h']=df2['change24h']*100
df2['change1h']=df2['change1h']*100
df_final=df2[['name','change1h','change24h','volumeUsd24h']]

st.dataframe(df_final)

@st.cache
def download_FtxData():
    df_final.to_csv(r"C:\Users\princ\Downloads\FTX_LT_Data_"+datetime.datetime.now().strftime('%d-%m-%Y_%H_%M')+".csv")


if st.button('Download FTX Data',on_click=download_FtxData()):
    st.write('downloaded successfully')

st.markdown(
    """
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""",
    unsafe_allow_html=True,
)
