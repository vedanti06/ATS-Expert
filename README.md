# 📄 ATS Resume Expert

A professional and intelligent resume analysis system that matches resumes against job descriptions using advanced AI technology.

## ✨ Features

- **📊 Resume Analysis**: Comprehensive evaluation of resume content and structure
- **🎯 Job Match Percentage**: AI-powered matching score calculation
- **🔍 Keyword Analysis**: Identifies missing skills and qualifications
- **📋 Professional Reports**: Detailed feedback with actionable recommendations
- **💾 Download Results**: Export analysis reports for offline review
- **🎨 Modern UI**: Professional, responsive design with intuitive navigation

## 🚀 How It Works

1. **Upload Resume**: Drag and drop your PDF resume
2. **Input Job Description**: Paste the complete job posting
3. **Choose Analysis**: Select between detailed analysis or match percentage
4. **Get Results**: Receive professional insights and recommendations

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: Google Gemini 1.5 Flash
- **PDF Processing**: pdf2image + Pillow
- **Styling**: Custom CSS with modern design principles

## 📋 Requirements

- Python 3.8+
- Google Gemini API key
- Poppler utilities (for PDF processing)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ATS
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🔑 API Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## 📱 Usage

1. **Launch the app** in your browser
2. **Upload your resume** in PDF format
3. **Paste the job description** you want to match against
4. **Choose analysis type**:
   - 📊 **Resume Analysis**: Detailed feedback and recommendations
   - 🎯 **Match Percentage**: Quick compatibility score
5. **Review results** and download reports

## 🎨 UI Improvements

The application now features:
- **Professional Design**: Modern gradient headers and clean layouts
- **Responsive Layout**: Optimized for different screen sizes
- **Intuitive Navigation**: Clear sections and logical flow
- **Visual Feedback**: Progress indicators and status messages
- **Download Options**: Export analysis results for offline use

## 🔧 Customization

You can customize the application by:
- Modifying the CSS styles in the `st.markdown` section
- Adjusting the AI prompts for different analysis types
- Adding new features or analysis options
- Customizing the color scheme and branding

## 📊 Sample Output

The system provides structured analysis including:
- Overall assessment and fit score
- Key strengths and qualifications
- Areas for improvement
- Specific recommendations
- Missing keywords and skills

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Streamlit
- Powered by Google Gemini AI
- Designed for professional use

---

**Built with ❤️ for better job matching and career success**

