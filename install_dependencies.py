#!/usr/bin/env python3
"""
ResearchScope AI - Dependency Installation Script
This script helps install all required dependencies with compatible versions.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"   {e.stderr}")
        return False

def main():
    print("🚀 ResearchScope AI - Dependency Installation")
    print("=" * 50)
    
    # Check if Python is available
    print(f"🐍 Python version: {sys.version}")
    
    # Handle spaces in python path for Windows
    python_executable = f'"{sys.executable}"'

    # Upgrade pip first
    if not run_command(f"{python_executable} -m pip install --upgrade pip", "Upgrading pip"):
        print("⚠️  Warning: Could not upgrade pip, continuing anyway...")
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    
    # Install core dependencies first
    core_deps = [
        "streamlit==1.28.1",
        "google-generativeai==0.3.2",
        "protobuf==4.24.4",
        "python-dotenv==1.0.0",
        "requests==2.31.0",
        "beautifulsoup4==4.12.2",
        "sqlalchemy==2.0.23",
        "pydantic==2.5.0",
        "typing-extensions==4.8.0"
    ]
    
    for dep in core_deps:
        if not run_command(f"{python_executable} -m pip install {dep}", f"Installing {dep}"):
            print(f"⚠️  Warning: Could not install {dep}")
    
    # Install LangChain and related packages
    langchain_deps = [
        "langchain==0.1.0",
        "langchain-community==0.0.10"
    ]
    
    for dep in langchain_deps:
        if not run_command(f"{python_executable} -m pip install {dep}", f"Installing {dep}"):
            print(f"❌ Failed to install {dep}")
            return False
    
    # Install CrewAI last
    if not run_command(f"{python_executable} -m pip install crewai==0.11.0", "Installing CrewAI"):
        print("❌ Failed to install CrewAI")
        return False
    
    print("\n🎉 Installation completed!")
    print("\n📋 Next steps:")
    print("1. Get your Google API Key from: https://makersuite.google.com/app/apikey")
    print("2. Create a .env file with: GOOGLE_API_KEY=your_key_here")
    print("3. Run the app with: python run_app.py")
    print("\n🚀 Ready to use ResearchScope AI!")

if __name__ == "__main__":
    main() 