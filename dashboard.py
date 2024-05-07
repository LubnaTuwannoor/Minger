
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your data
data = pd.ExcelFile("Global Superstore lite.xlsx")
# Assuming you have a DataFrame df from your data
# For example:
# df = data.parse("Sheet1")

# Create a bar chart
def create_bar_chart():
    plt.bar(df['Column1'], df['Column2'])
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Bar Chart')
    st.pyplot()

# Main function to run the Streamlit app
def main():
    st.title('Your Streamlit App Title')
    st.write("Here's some data:")
    st.write("And here's a visualization:")
    st.write("Support Values")
    st.write("Confidence Values")
    st.write("Lift Values")

if __name__ == '__main__':
    main()
