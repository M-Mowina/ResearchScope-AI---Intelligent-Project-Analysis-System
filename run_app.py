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
    
    # Define the path to the app.py file
    app_path = os.path.join("src", "app.py")

    # Run streamlit app
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", app_path,
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Thanks for using ResearchScope AI!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting Streamlit: {e}")
        print("💡 Make sure you have installed all requirements: pip install -r requirements.txt")
    except FileNotFoundError:
        print(f"❌ Error: Could not find the Streamlit app at '{app_path}'")
        print("💡 Please ensure the file exists and the path is correct.")

if __name__ == "__main__":
    main() 