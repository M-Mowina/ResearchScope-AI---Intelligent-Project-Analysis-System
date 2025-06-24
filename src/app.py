import streamlit as st
import os
from dotenv import load_dotenv
from project_analysis_crew_fixed import analyze_project
import time

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="ResearchScope AI - Intelligent Project Analysis",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .stTextArea > div > div > textarea {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 15px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
    }
    .result-box {
        background: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
    }
    .agent-info {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🔬 ResearchScope AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Intelligent Project Analysis System</p>', unsafe_allow_html=True)
    
    # --- API Key Check ---
    # Securely check for the API key from environment variables
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        if not api_key:
            st.error("⚠️ API Key Not Found!")
            st.markdown("""
                Create a `.env` file in the project root and add:
                `GOOGLE_API_KEY="YOUR_KEY_HERE"`
            """)
            st.stop()
        else:
            st.success("✅ API Key Loaded")
        
        st.markdown("---")
        
        # Information about the system
        st.header("ℹ️ About")
        st.markdown("""
        **ResearchScope AI** uses advanced AI agents to:
        
        🔍 **Extract Keywords** - Identify key technical concepts
        📚 **Research Papers** - Find relevant academic sources
        📝 **Summarize Findings** - Create comprehensive summaries
        ✅ **Validate Results** - Ensure alignment with requirements
        
        Powered by CrewAI and Google's Gemini Pro.
        """)
        
        st.markdown("---")
        
        # Example projects
        st.header("💡 Example Projects")
        
        example_projects = {
            "Smart Home Energy Management": """
            Develop an AI-powered energy management system for smart homes that can:
            1. Monitor and analyze real-time energy consumption patterns
            2. Predict energy usage based on historical data and weather conditions
            3. Automatically optimize energy distribution across different home systems
            4. Provide personalized recommendations for energy savings
            5. Integrate with existing smart home devices and solar panel systems
            """,
            "Healthcare AI Assistant": """
            Create an AI-powered healthcare assistant that can:
            1. Analyze patient symptoms and medical history
            2. Provide preliminary diagnosis suggestions
            3. Recommend appropriate medical tests
            4. Monitor patient vital signs in real-time
            5. Integrate with electronic health records
            """,
            "Autonomous Vehicle Navigation": """
            Build an autonomous vehicle navigation system that can:
            1. Process real-time sensor data from cameras, LiDAR, and radar
            2. Implement advanced path planning algorithms
            3. Handle complex traffic scenarios and edge cases
            4. Ensure passenger safety through redundant systems
            5. Adapt to different weather and road conditions
            """
        }
        
        selected_example = st.selectbox(
            "Choose an example:",
            list(example_projects.keys())
        )
        
        if st.button("Load Example"):
            st.session_state.project_description = example_projects[selected_example]
            st.rerun()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📋 Project Description")
        
        # Project description input
        project_description = st.text_area(
            "Enter your project description:",
            height=300,
            placeholder="Describe your project in detail, including goals, requirements, and technical specifications...",
            key="project_description"
        )
        
        # Analysis button
        if st.button("🚀 Start Analysis", type="primary", use_container_width=True):
            if not project_description.strip():
                st.error("❌ Please enter a project description")
            else:
                with st.spinner("🤖 AI agents are analyzing your project..."):
                    try:
                        # Create progress indicators
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Simulate progress updates
                        for i, step in enumerate(["Extracting keywords...", "Researching papers...", "Summarizing findings...", "Validating results..."]):
                            status_text.text(step)
                            progress_bar.progress((i + 1) * 25)
                            time.sleep(0.5)
                        
                        # Perform the actual analysis
                        result = analyze_project(project_description)
                        
                        progress_bar.progress(100)
                        status_text.text("✅ Analysis complete!")
                        
                        # Store result in session state
                        st.session_state.analysis_result = result
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
                        st.error("Please check your API key and try again.")
    
    with col2:
        st.header("📊 Analysis Status")
        
        if 'analysis_result' in st.session_state:
            st.success("✅ Analysis Complete!")
            
            # Download button
            result_text = st.session_state.analysis_result
            st.download_button(
                label="📥 Download Report",
                data=result_text,
                file_name="research_analysis_report.txt",
                mime="text/plain"
            )
        else:
            st.info("⏳ No analysis performed yet")
            st.markdown("""
            **Ready to analyze your project?**
            
            1. Enter your project description
            2. Click "Start Analysis"
            3. Wait for AI agents to complete their work
            4. Review the comprehensive report
            """)
    
    # Display results
    if 'analysis_result' in st.session_state:
        st.markdown("---")
        st.header("📋 Analysis Results")
        
        # Create tabs for better organization
        tab1, tab2 = st.tabs(["📄 Full Report", "🔍 Key Insights"])
        
        with tab1:
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.text_area(
                "Analysis Report",
                value=st.session_state.analysis_result,
                height=600,
                disabled=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with tab2:
            # Extract key insights (this is a simplified version)
            result = st.session_state.analysis_result
            st.markdown("### 🔍 Key Insights Extracted")
            
            # Simple keyword extraction (in a real implementation, you'd parse the result more intelligently)
            if "keyword" in result.lower() or "research" in result.lower():
                st.success("✅ Research papers found and analyzed")
            if "summary" in result.lower():
                st.success("✅ Comprehensive summary generated")
            if "validation" in result.lower():
                st.success("✅ Project requirements validated")
            
            st.info("💡 For detailed insights, check the Full Report tab above.")

if __name__ == "__main__":
    main() 