import streamlit as st

def main():
    st.title("Bicep Curl Form Detector")
    st.subheader("This app allows you to judge the form of your bicep curls using OpenCV and Mediapipe")
    st.divider()
    st.text("Before we begin, let's take you through the onboarding process.")
    hand = ""
    button_pressed = False
    if not button_pressed:
        if st.button("Click to start." ):
            button_pressed = True
    else:
        arm_selected = st.selectbox( "Which arm would you like to use?" , ["Left", "Right"] )
        hand = arm_selected
    # start_button_not_pressed = false
    # if start_button_not_pressed: 
    #     st.button("Click to start.",  )
    #     hand = st.selectbox(
    #     "Which hand would you like to use for the demo?",
    #     ("Left", "Right")
    # if st.button("Click to start." ):
    #     arm_selected = st.selectbox( "Which arm would you like to use?" , ["Left", "Right"] )
    #     hand = arm_selected

    st.text(hand)


if __name__ == '__main__':
    main()