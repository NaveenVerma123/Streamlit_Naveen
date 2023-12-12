
import streamlit as st

def find_greatest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find Greatest Among Three Numbers")

    # User input for three numbers
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)
    num3 = st.number_input("Enter the third number", value=0)

    # Button to find the greatest number
    if st.button("Find Greatest"):
        greatest = find_greatest(num1, num2, num3)
        st.success(f"The greatest number is: {greatest}")

if __name__ == "__main__":
    main()
