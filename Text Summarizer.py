# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:01:12 2023

@author: lenovo
"""

import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline('summarization')

# Streamlit app header
st.title("Text Summarizer")

# User input for long text
long_text = st.text_area("Paste your long text here:")

# User input for min and max lengths
min_length = st.number_input("Enter the minimum length for the summary:", min_value=1, max_value=1000, value=30)
max_length = st.number_input("Enter the maximum length for the summary:", min_value=min_length, max_value=2000, value=150)

# Function to summarize text
def summarize_text(long_text, min_length, max_length):
    summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
    return summary

# Generate summary on button click
if st.button("Generate Summary"):
    if long_text:
        summary = summarize_text(long_text, min_length, max_length)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
