import streamlit as st
import requests

class run_streamlit_app():

    # Define the page background image
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url(https://cdn.leonardo.ai/users/3f6ba5a1-8d42-491a-8e0d-2e7632a50c37/generations/76ba7da8-4b52-4873-ade6-ac36fd48fd4b/variations/UniversalUpscaler_76ba7da8-4b52-4873-ade6-ac36fd48fd4b.jpg);
        background-size: 100%;
        background-position: center;
        background-repeat: repeat;
        background-attachment: local;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Define the styles for headers
    st.markdown("""
    <style>
    h1, h2, h3 {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page title and header
    st.markdown("<h1 style='text-align: center;'>AI SMART FARMER</h1>", unsafe_allow_html=True)
    st.header("Your AI smart farming assistant")
    st.markdown("AI Farming Decision Support System from Innovation imperial")

    # side bar
    st.sidebar.success("select any page and explore smart farmer")

    # User input textbox
    user_input = st.text_input("Enter your question:")


    # Function to make request to FastAPI backend
    def make_request(self):
        url = "http://fastapi:8000/answer"  # URL of the FastAPI backend
        response = requests.post(url, json={"question": self.user_input})
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            return "Error: Unable to get response from backend."
        
      # Display response
    def display_response(self):
        if st.button("Get Answer"):
            if self.user_input:
                answer = self.make_request()
                st.write("Output:", answer)
            else:
                st.warning("Please enter a question.")

# Instantiate the run_smartApp class
App = run_streamlit_app()

if __name__ == "__main__":
    App.display_response()
  







