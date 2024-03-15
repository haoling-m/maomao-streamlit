import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    info_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        temp = np.random.randn(5, 1)
        info_text.text(temp)
        new_rows = last_rows[-1, :] + temp.cumsum(axis=0)
        status_text.text(new_rows)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.5)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="empty Demo", page_icon="🧷")
st.markdown("# empty Demo")
st.sidebar.header("empty Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

plotting_demo()
