# import base64
# import io
# from dotenv import load_dotenv

# load_dotenv()

# import streamlit as st

# st.title("ATS - Applicant Tracking System")
# import os
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# # Set up the Google Generative AI API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# # Function to get Gemini response
# def get_gemini_response(input,pdf_content,prompt):
#     model=genai.GenerativeModel("gemini-pro-vision")
#     response = model.generate_content([
#         input,pdf_content[0],prompt
#         ]
#     )
#     return response.text

# # Function to handle file upload and convert PDF to image
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_byte(uploaded_file.read())
#         first_page=images[0]
#         image_byte_arr=io.BytesIO()
#         first_page.save(image_byte_arr, format="JPEG")
#         image_byte_arr=image_byte_arr.getvalue()
#     # Prepare the PDF content for Gemini
#     # pdf content in bytes
#         pdf_parts=[
#             {
#                 "mime_type": "image/jpeg",
#                 "data":base64.b64encode(image_byte_arr).decode()
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    

# #Streamlit file uploader

# st.header("ATS Tracking System")
# input_text = st.text_input("Enter the job description here:")
# uploaded_file = st.file_uploader("Upload a resume (PDF)....", type=["pdf"])

# if uploaded_file is not None:
#     st.write("Resume uploaded successfully!")

# submit1=st.button("Tell me about the resume")
# submit2=st.button("How can I improvise my resume?")
# submit3=st.button("Percentage match with the job description")



# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of all the skills and ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """



# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")


from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   




