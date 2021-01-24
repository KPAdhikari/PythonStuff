
#Refs:
# https://www.youtube.com/watch?v=ZZ4B0QUHuNc&t=590s
# https://www.streamlit.io/
# installed 'streamlit' with pip3
#
# During which it suggested to update pip3 with following command:
#     /usr/local/opt/python/bin/python3.7 -m pip install --upgrade pip
# and I indeed updated pip3 with above command
#
# Next I tried to run 'streamlit hello' as suggested in youtube video
#   but during it's run, it recommended to install the Watchdog module
#   for better performance, so I installed that with
#        pip3 install watchdog
#
# Then I ran 'streamlit hello' in the terminal again, which gave a bunch
#    of texts in the terminal that included the following, while also
#    opening a webpage http://localhost:8501/ in my localhost
##################
# KPAd's FunPrompt $ streamlit hello
#
#  👋 Welcome to Streamlit!
# .....
# .....
# Privacy Policy:
#  As an open source project, we collect usage statistics. We cannot see and do
#  not store information contained in Streamlit apps. You can find out more by
#  reading our privacy policy at: https://streamlit.io/privacy-policy
#
#  If you'd like to opt out of usage statistics, add the following to
#  ~/.streamlit/config.toml, creating that file if necessary:
#
#    [browser]
#    gatherUsageStats = false
#
#
#  Welcome to Streamlit. Check out our demo in your browser.
#
#  Local URL: http://localhost:8501
#  Network URL: http://192.168.0.158:8501
#
#  Ready to create your own Python apps super quickly?
#  Head over to https://docs.streamlit.io
#
#  May you create awesome apps!
#
#  (kp: terminal hanging, with control gone to the web-browser)
#
##################
#
#  Then as the youtube guy did, I am creating this myapp.py file and
#  copying his lines (also installing 'yfinance' with pip3.
#
#  Now to run it, use the following command in the terminal:
#
#          streamlit run myapp.py
#
#  Which will spawn up a web-server (in a browser tab) with the charts
#  The fun part is that if we edit this file and save it, the web-app
#     will detect that and will say "Source file changed." notice along
#     with a convenient "Rerun" button right next to that, making it so
#     easy to update the texts, charts or anything that has been changed.
#     Also, there is "Always Rerun" button next to "Rerun", which when
#     clicked, instead of "Rerun", we don't even have to click any of these
#     buttons later when we have any change in the source file, rather it
#     will automatically rerun/update it.
#
#   It turns out we can also zoom-in and zoom-out the charts with the
#      two-finger pinching in/out moves on the track-pad of my macbook air
#      once we click on the chart first.
#   And, double clicking on it, would take it to the original zooming scale.
#

import yfinance as yf
import streamlit as st
import pandas as pd

#kp: In the following, the video says, it uses Markdown
st.write("""
## Simple Stock Price App

Shown are the stock **closing price** and **volume** of **Google**!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')
# Open High   Low Close Volume Dividends Stock Splits



st.write("""
## Closing Price

""")

st.line_chart(tickerDf.Close)


st.write("""
## Volume

""")
st.line_chart(tickerDf.Volume)
