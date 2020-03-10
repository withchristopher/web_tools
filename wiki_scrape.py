#Export Wikipedia as a Script

import pandas as pd
import wikipedia as wp
import easygui

#Popup window
URL = easygui.enterbox("Enter full Wikipedia URL:")

page_title = URL.strip('https://en.wikipedia.org/wiki/')
html = wp.page(page_title).html().encode("UTF-8")
try:
    df = pd.read_html(html)[0]  # 2nd table incase of content table
except IndexError:
    df = pd.read_html(html)[1]
print(df.to_string())

#Output as excel
df.to_excel('{0}.xlsx'.format(page_title))