import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh

import streamlit.components.v1 as components

st.set_page_config(layout='wide')
# st_autorefresh(interval=60*1000, key="dataframerefresh")

components.html('''<!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/markets/" rel="noopener" target="_blank"><span class="blue-text">Markets</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
    {
    "symbols": [
    {
      "description": "",
      "proName": "FTX:BTCPERP"
    },
    {
      "description": "",
      "proName": "FTX:SOLUSD"
    },
    {
      "description": "",
      "proName": "FTX:ETHPERP"
    },
    {
      "description": "",
      "proName": "FTX:AVAXPERP"
    },
    {
      "description": "",
      "proName": "FTX:FTTUSD"
    },
    {
      "description": "",
      "proName": "FTX:ADAPERP"
    },    
    {
      "description": "",
      "proName": "FTX:FTMPERP"
    },
    {
      "description": "",
      "proName": "FTX:WAVESPERP"
    },
    {
      "description": "",
      "proName": "FTX:LOOKSUSD"
    },
    {
      "description": "",
      "proName": "FTX:BNBPERP"
    },
    {
      "description": "",
      "proName": "FTX:DOGEPERP"
    },
    {
      "description": "",
      "proName": "FTX:DOTPERP"
    },
    {
      "description": "",
      "proName": "FTX:AAVEPERP"
    },
    {
      "description": "",
      "proName": "FTX:LINKPERP"
    }
    ,
    {
      "description": "",
      "proName": "FTX:LTCPERP"
    }
    ,
    {
      "description": "",
      "proName": "FTX:COMPPERP"
    }
    ,
    {
      "description": "",
      "proName": "FTX:UNIPERP"
    },
    {
      "description": "",
      "proName": "FTX:MATICPERP"
    },
    {
      "description": "",
      "proName": "FTX:GRTPERP"
    },
    {
      "description": "",
      "proName": "FTX:ETCPERP"
    }
    ,
    {
      "description": "",
      "proName": "FTX:XTZPERP"
    }
    ,
    {
      "description": "",
      "proName": "FTX:XLMPERP"
    }
  ],
      "showSymbolLogo": true,
      "colorTheme": "light",
      "isTransparent": false,
      "displayMode": "adaptive",
      "locale": "en"
    }
      </script>
    </div>
    <!-- TradingView Widget END -->'''
    )

c1,c2,c3=st.columns(3)
# with st.sidebar:
#     st.components.v1.html('''<div class="tradingview-widget-container">
#                           <div class="tradingview-widget-container__widget"></div>
#                           <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/crypto-screener/" rel="noopener" target="_blank"><span class="blue-text">Crypto Screener</span></a> by TradingView</div>
#                           <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
#                           {
#                           "width": "100%",
#                           "height": "100%",
#                           "defaultColumn": "moving_averages",
#                           "defaultScreen": "general",
#                           "market": "crypto",
#                           "showToolbar": true,
#                           "colorTheme": "light",
#                           "locale": "en"
#                         }
#                         </script>
#                         </div>'''
#              , height=150, scrolling=False)


# with c2:
#     components.html('''<!DOCTYPE html>
#       <html>
#       <head>
#       <meta charset="utf-8">
#       <meta http-equiv="X-UA-Compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width,initial-scale=1.0">
#       </head>
#       <body>
#       <!-- COPY QC WIDGET TAG AND SCRIPT BELOW -->
#       <qc-trend
#       coin-name="ETH"
#       background="#1e1e1e"
#       theme="dark"
#       currency-code="USD"
#       width="70%"
#       height="85px"></qc-trend>
#       <script src="https://quantifycrypto.com/widgets/trend/js/qc-trend-widget.js"></script>
#       </body>
#       </html>
#           ''')
#
# with c3:
#     components.html('''<!DOCTYPE html>
#       <html>
#       <head>
#       <meta charset="utf-8">
#       <meta http-equiv="X-UA-Compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width,initial-scale=1.0">
#       </head>
#       <body>
#       <!-- COPY QC WIDGET TAG AND SCRIPT BELOW -->
#       <qc-trend
#       coin-name="BNB"
#       background="#1e1e1e"
#       theme="dark"
#       currency-code="USD"
#       width="70%"
#       height="85px"></qc-trend>
#       <script src="https://quantifycrypto.com/widgets/trend/js/qc-trend-widget.js"></script>
#       </body>
#       </html>
#           ''')

# with c4:
#     components.html('''<!DOCTYPE html>
#       <html>
#       <head>
#       <meta charset="utf-8">
#       <meta http-equiv="X-UA-Compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width,initial-scale=1.0">
#       </head>
#       <body>
#       <!-- COPY QC WIDGET TAG AND SCRIPT BELOW -->
#       <qc-trend
#       coin-name="LOOKS"
#       background="#1e1e1e"
#       theme="dark"
#       currency-code="USD"
#       width="70%"
#       height="85px"></qc-trend>
#       <script src="https://quantifycrypto.com/widgets/trend/js/qc-trend-widget.js"></script>
#       </body>
#       </html>
#           ''')

# with c5:
#     components.html('''<!DOCTYPE html>
#       <html>
#       <head>
#       <meta charset="utf-8">
#       <meta http-equiv="X-UA-Compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width,initial-scale=1.0">
#       </head>
#       <body>
#       <!-- COPY QC WIDGET TAG AND SCRIPT BELOW -->
#       <qc-trend
#       coin-name="DOT"
#       background="#1e1e1e"
#       theme="dark"
#       currency-code="USD"
#       width="70%"
#       height="85px"></qc-trend>
#       <script src="https://quantifycrypto.com/widgets/trend/js/qc-trend-widget.js"></script>
#       </body>
#       </html>
#           ''')
