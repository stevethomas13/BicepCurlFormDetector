import streamlit as st

def main():
    st.title("Bicep Curl Form Detector")
    st.subheader("This app allows you to judge the form of your bicep curls using OpenCV and Mediapipe")
    st.text("Before we begin, let's take you through the onboarding process.")
    hand = ""
    if st.button("Click to start."):
        st.text("Which hand would you like to use for the demo?")
        if st.checkbox("Left"):
            hand = "Left"
        if st.checkbox("Right"):
            hand = "Right"


    slider_value = st.slider("Slider", min_value=0.5, max_value=3.5)
    st.text(f"Slider value is {slider_value}")

    st.sidebar.text("text on side panel")
    st.sidebar.checkbox("Side Panel Checkbox")


if __name__ == '__main__':
    main()