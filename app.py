import streamlit as st
from src.keboola.connect import add_keboola_table_selection
from src.render_stats import render_stats

st.image('static/keboola_logo.png', width=400)

# Web App Title
st.markdown('''
# **Keboola Component Benchmark Viewer**
---
''')

# Adds a table selection form to the sidebar of streamlit
add_keboola_table_selection()
if "extracted_file" not in st.session_state:
    st.write(
        "In order to use this app, you must have artifacts enabled in your project."
        ""
    )
if "extracted_file" in st.session_state:
    render_stats()
