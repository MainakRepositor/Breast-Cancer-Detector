"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Artificial Neural Networks</b> for the Breast Cancer Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    rad = st.slider("Radius", float(df["radius_mean"].min()), float(df["radius_mean"].max()))
    tex = st.slider("Texture", float(df["texture_mean"].min()), float(df["texture_mean"].max()))
    per = st.slider("Perimeter", float(df["perimeter_mean"].min()), float(df["perimeter_mean"].max()))
    are = st.slider("Area", float(df["area_mean"].min()), float(df["area_mean"].max()))
    smo = st.slider("Smoothness", float(df["smoothness_mean"].min()), float(df["smoothness_mean"].max()))
    com = st.slider("Compactness", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    con = st.slider("Concavity", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    sym = st.slider("Symmetry", float(df["symmetry_mean"].min()), float(df["symmetry_mean"].max()))
    fad = st.slider("Fractal Dimension", float(df["fractal_dimension_mean"].min()), float(df["fractal_dimension_mean"].max()))
       


    # Create a list to store all the features
    features = [rad,tex,per,are,smo,com,con,sym,fad]

    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Detected Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person has Breast Cancer!!")
        else:
            st.success("The person is safe from Breast Cancer")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", round((score*100)),"%")
