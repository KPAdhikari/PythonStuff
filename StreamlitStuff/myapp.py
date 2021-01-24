
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

import yfinance as yf
import streamlit as st
import pandas as pd
