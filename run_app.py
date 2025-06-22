#!/usr/bin/env python3
"""
ResearchScope AI - Streamlit App Launcher
"""

import subprocess
import sys
import os

def main():
    """Launch the Streamlit application"""
    print("🚀 Starting ResearchScope AI...")
    print("📱 Opening Streamlit app in your browser...")
    print("🔑 Don't forget to enter your Google API Key in the sidebar!")
    print("\n" + "="*50)
    
    # Run streamlit app
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Thanks for using ResearchScope AI!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting Streamlit: {e}")
        print("💡 Make sure you have installed all requirements: pip install -r requirements.txt")

if __name__ == "__main__":
    main() 