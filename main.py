import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)
style_text = """
  <style>
    .block-container {
      padding: 1.5rem 1rem;
    }
  </style>
"""

def run():
    st.markdown(style_text, unsafe_allow_html=True)
    st.write("## Graded Assignment  - Tools in Data Science")
    st.subheader("To find the largest among given three numbers")
    st.write("**Enter the numbers below:**")
    num1 = st.number_input("**NUMBER 1**", value=0.0, format="%g")
    num2 = st.number_input("**NUMBER 2**", value=0.0, format="%g")
    num3 = st.number_input("**NUMBER 3**", value=0.0, format="%g")
    max_num = max(num1, num2, num3)

    largest_btn = st.button("Find Largest", type="primary")

    if largest_btn:
      st.write("### The LARGEST NUMBER is = " + f":red[{max_num}]")


if __name__ == "__main__":
    run()
