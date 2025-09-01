from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

# Configure page
st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)




# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .upload-section {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 2px dashed #dee2e6;
        text-align: center;
        margin: 1rem 0;
    }
    
    .button-primary {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .button-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .result-section {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #28a745;
    }
    
    .sidebar-section {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .stButton > button {
        width: 100%;
        margin: 0.5rem 0;
    }
    
    .file-uploader {
        border: 2px dashed #dee2e6;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        background: #f8f9fa;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #28a745 0%, #20c997 100%);
        height: 8px;
        border-radius: 4px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, pdf_content, job_description):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_prompt, pdf_content[0], job_description])
        return response.text
    except Exception as e:
        return f"Error processing request: {str(e)}"

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Convert the PDF to image
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")
            return None
    else:
        return None

# Main App
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📄 ATS Resume Expert</h1>
        <p style="font-size: 1.2rem; margin: 0;">Professional Resume Analysis & Job Matching System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation and info
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-section">
            <h3>🚀 How it Works</h3>
            <ol style="text-align: left;">
                <li>Upload your resume (PDF)</li>
                <li>Paste the job description</li>
                <li>Choose analysis type</li>
                <li>Get professional insights</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="sidebar-section">
            <h3>💡 Features</h3>
            <ul style="text-align: left;">
                <li>Resume Analysis</li>
                <li>Job Match Percentage</li>
                <li>Keyword Analysis</li>
                <li>Professional Feedback</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Job Description Input
        st.markdown("### 📝 Job Description")
        job_description = st.text_area(
            "Paste the job description here...",
            height=200,
            placeholder="Enter the complete job description including requirements, responsibilities, and qualifications...",
            key="job_description"
        )
        
        # Resume Upload
        st.markdown("### 📎 Resume Upload")
        uploaded_file = st.file_uploader(
            "Choose your resume file",
            type=["pdf"],
            help="Upload your resume in PDF format for analysis"
        )
        
        if uploaded_file is not None:
            st.success(f"✅ Resume uploaded successfully: {uploaded_file.name}")
            
            # File info
            file_size = len(uploaded_file.getvalue()) / 1024  # KB
            st.info(f"📊 File size: {file_size:.1f} KB")
    
    with col2:
        # Analysis Options
        st.markdown("### 🔍 Analysis Options")
        
        if uploaded_file is not None and job_description.strip():
            # Resume Analysis Button
            if st.button("📊 Analyze Resume", key="analyze_btn", use_container_width=True):
                st.session_state.analyze_clicked = True
                st.session_state.percentage_clicked = False
            
            # Percentage Match Button
            if st.button("🎯 Get Match Percentage", key="percentage_btn", use_container_width=True):
                st.session_state.percentage_clicked = True
                st.session_state.analyze_clicked = False
        else:
            st.warning("⚠️ Please upload a resume and enter job description to proceed")
    
    # Results Section
    if uploaded_file is not None and job_description.strip():
        st.markdown("---")
        st.markdown("### 📋 Analysis Results")
        
        # Initialize session state
        if 'analyze_clicked' not in st.session_state:
            st.session_state.analyze_clicked = False
        if 'percentage_clicked' not in st.session_state:
            st.session_state.percentage_clicked = False
        
        # Process analysis requests
        if st.session_state.analyze_clicked:
            with st.spinner("🔍 Analyzing your resume..."):
                pdf_content = input_pdf_setup(uploaded_file)
                if pdf_content:
                    input_prompt1 = """
                    You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
                    Please provide a professional evaluation covering:
                    
                    1. **Overall Assessment**: Brief summary of candidate's fit
                    2. **Strengths**: Key qualifications that align with the role
                    3. **Areas for Improvement**: Missing skills or experience
                    4. **Recommendations**: Specific suggestions to improve the resume
                    
                    Format your response in a clear, professional manner with bullet points and sections.
                    """
                    
                    response = get_gemini_response(input_prompt1, pdf_content, job_description)
                    
                    st.markdown("""
                    <div class="result-section">
                        <h4>📊 Resume Analysis Report</h4>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(response)
                    
                    # Download option
                    st.download_button(
                        label="📥 Download Analysis Report",
                        data=response,
                        file_name="resume_analysis_report.txt",
                        mime="text/plain"
                    )
        
        elif st.session_state.percentage_clicked:
            with st.spinner("🎯 Calculating match percentage..."):
                pdf_content = input_pdf_setup(uploaded_file)
                if pdf_content:
                    input_prompt3 = """
                    You are a skilled ATS (Applicant Tracking System) scanner with deep understanding of data science and ATS functionality. 
                    Your task is to evaluate the resume against the provided job description and provide:
                    
                    1. **Match Percentage**: A single percentage number (e.g., "75%")
                    2. **Missing Keywords**: List of important keywords/skills missing from the resume
                    3. **Final Assessment**: Brief summary of overall match quality
                    
                    Format your response clearly with these three sections.
                    """
                    
                    response = get_gemini_response(input_prompt3, pdf_content, job_description)
                    
                    st.markdown("""
                    <div class="result-section">
                        <h4>🎯 Job Match Analysis</h4>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(response)
                    
                    # Download option
                    st.download_button(
                        label="📥 Download Match Report",
                        data=response,
                        file_name="job_match_report.txt",
                        mime="text/plain"
                    )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 2rem;">
        <p>Built with ❤️ using Streamlit & Gemini AI</p>
        <p>Professional ATS Resume Analysis System</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()




