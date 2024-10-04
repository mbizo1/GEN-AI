import streamlit as stl
import Backend as bk

stl.title("GEN Ai Project")
input = stl.text_input("Enter text")
submit_button = stl.button("Submit")

if submit_button:
    output = bk.text_output(input)
    stl.write(output)