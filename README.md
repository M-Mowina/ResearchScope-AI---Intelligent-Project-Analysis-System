# ResearchScope AI - Intelligent Project Analysis System

ResearchScope AI is an advanced project analysis system that leverages multiple AI agents to perform comprehensive research and analysis of technical projects. The system uses Google's Gemini model to power a team of specialized agents that work together to extract insights, gather research, and validate project requirements.

## 🌟 Features

- **🔍 Keyword Extraction**: Automatically identifies key technical terms from project descriptions
- **📚 Research Paper Discovery**: Web scraping for relevant academic papers and technical documentation
- **📝 Intelligent Summarization**: Creates comprehensive summaries of research findings
- **✅ Requirement Validation**: Ensures alignment between project goals and research insights
- **🤖 Multi-Agent Collaboration**: Sequential processing using CrewAI framework
- **🎨 Modern Web Interface**: Beautiful Streamlit UI for easy interaction
- **📊 Real-time Progress Tracking**: Visual feedback during analysis
- **💾 Report Export**: Download analysis results as text files

## 🚀 Quick Start

### Option 1: Web Interface (Recommended)

1. **Install dependencies** (choose one method):
   ```bash
   # Method 1: Use the installation script (recommended)
   python install_dependencies.py
   
   # Method 2: Manual installation
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app**:
   ```bash
   python run_app.py
   ```
   Or directly with Streamlit:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and navigate to `http://localhost:8501`

4. **Enter your Google API Key** in the sidebar

5. **Start analyzing projects** by entering your project description!

### Option 2: Command Line Interface

1. **Setup environment**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file** with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Run the analysis**:
   ```python
   from project_analysis_crew_fixed import analyze_project
   
   project_description = """
   Your project description here
   """
   result = analyze_project(project_description)
   print(result)
   ```

## 🔧 Troubleshooting

### Common Issues

#### 1. MessageMapContainer Error
If you encounter this error:
```
AttributeError: module 'google._upb._message' has no attribute 'MessageMapContainer'
```

**Solution**: Use the installation script to ensure compatible versions:
```bash
python install_dependencies.py
```

#### 2. SQLAlchemy Import Error
If you encounter this error:
```
ModuleNotFoundError: No module named 'sqlalchemy'
```

**Solution**: The installation script now includes SQLAlchemy. Run:
```bash
python install_dependencies.py
```

#### 3. LangChain Import Errors
If you get import errors with LangChain or CrewAI:
```bash
# Test your environment first
python test_dependencies.py

# If tests fail, reinstall dependencies
python install_dependencies.py
```

#### 4. Import Errors
If you get import errors with `langchain_google_genai`:
- The project now uses a custom LLM wrapper that avoids this issue
- Make sure you're using `project_analysis_crew_fixed.py` instead of the original

#### 5. API Key Issues
- Ensure your Google API Key is valid and has access to Gemini Pro
- Check that the API key is properly set in the environment or entered in the web interface

#### 6. Dependency Conflicts
If you have conflicts with existing packages:
```bash
# Create a virtual environment
python -m venv researchscope_env
source researchscope_env/bin/activate  # On Windows: researchscope_env\Scripts\activate
python install_dependencies.py
```

### Testing Your Setup
Before running the app, test your environment:
```bash
python test_dependencies.py
```

This will verify that all dependencies are properly installed and working.

## 📋 Example Projects

The web interface includes several example projects you can try:

### Smart Home Energy Management
AI-powered energy management system for smart homes with real-time monitoring, predictive analytics, and automated optimization.

### Healthcare AI Assistant
Intelligent healthcare assistant for symptom analysis, preliminary diagnosis, and medical test recommendations.

### Autonomous Vehicle Navigation
Advanced navigation system for autonomous vehicles with sensor processing, path planning, and safety systems.

## 🏗️ Project Structure

```
ResearchScope-AI/
├── app.py                      # Streamlit web application
├── run_app.py                  # App launcher script
├── project_analysis_crew_fixed.py  # Fixed core analysis engine
├── project_analysis_crew.py    # Original version (may have compatibility issues)
├── install_dependencies.py     # Dependency installation script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── run_app.bat                 # Windows launcher
├── run_app.sh                  # Unix/Linux/Mac launcher
└── .env                        # Environment variables (create this)
```

## 🤖 AI Agents

The system uses four specialized AI agents working in sequence:

1. **🔍 Keyword Extractor**
   - Analyzes project descriptions
   - Extracts key technical terms and concepts
   - Identifies research-relevant keywords

2. **📚 Research Agent**
   - Searches for relevant academic papers
   - Analyzes technical documentation
   - Uses web scraping tools for discovery

3. **📝 Summarization Expert**
   - Creates comprehensive research summaries
   - Highlights key insights and applications
   - Maintains technical accuracy

4. **✅ Validation Expert**
   - Compares project requirements with findings
   - Identifies gaps and areas for additional research
   - Ensures alignment between goals and insights

## ⚙️ Configuration

### Required API Key
- **Google Generative AI API Key**: Required for the Gemini Pro model
- Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Enter it in the web interface sidebar or set it in your `.env` file

### Environment Variables
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## 🎨 Web Interface Features

- **📱 Responsive Design**: Works on desktop and mobile devices
- **🎯 Progress Tracking**: Real-time updates during analysis
- **📊 Results Organization**: Tabbed interface for full reports and key insights
- **💾 Export Functionality**: Download analysis reports as text files
- **🔧 Easy Configuration**: API key management in the sidebar
- **💡 Example Projects**: Pre-loaded examples to get started quickly

## 🔧 Technical Details

### Dependencies
- **CrewAI**: Multi-agent framework for orchestration
- **LangChain**: LLM integration and tool management
- **Google Generative AI**: Gemini Pro model for AI capabilities
- **Streamlit**: Web interface framework
- **BeautifulSoup**: Web scraping capabilities
- **Requests**: HTTP client for web requests

### Architecture
The system follows a sequential processing pipeline:
1. Project description input
2. Keyword extraction
3. Research paper discovery
4. Content summarization
5. Requirement validation
6. Results presentation

## 🚨 Important Notes

- **Web Scraping**: The current implementation uses simplified web scraping. For production use, consider:
  - Academic APIs (Semantic Scholar, arXiv, PubMed)
  - More robust error handling
  - Rate limiting and respect for robots.txt
  - Proper academic paper databases

- **API Usage**: The system makes multiple API calls to Google's Gemini Pro. Monitor your usage to stay within limits.

- **Privacy**: Project descriptions are sent to Google's API for processing. Ensure no sensitive information is included.

- **Compatibility**: The project uses a custom LLM wrapper to avoid compatibility issues with the official LangChain Google AI integration.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check that your API key is valid
2. Ensure all dependencies are installed using `python install_dependencies.py`
3. Verify your internet connection
4. Check the console for error messages
5. Try the troubleshooting steps above

For additional help, please open an issue on the GitHub repository. 