#!/usr/bin/env python3
"""
ResearchScope AI - Dependency Test Script
This script tests if all required dependencies are properly installed.
"""

import sys

def test_import(module_name, description):
    """Test if a module can be imported"""
    try:
        __import__(module_name)
        print(f"✅ {description} - OK")
        return True
    except ImportError as e:
        print(f"❌ {description} - FAILED: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {description} - WARNING: {e}")
        return True

def main():
    print("🧪 ResearchScope AI - Dependency Test")
    print("=" * 40)
    
    # Test core dependencies
    print("\n📦 Testing core dependencies...")
    core_tests = [
        ("streamlit", "Streamlit"),
        ("google.generativeai", "Google Generative AI"),
        ("protobuf", "Protobuf"),
        ("dotenv", "Python-dotenv"),
        ("requests", "Requests"),
        ("bs4", "BeautifulSoup4"),
        ("sqlalchemy", "SQLAlchemy"),
        ("pydantic", "Pydantic"),
    ]
    
    core_results = []
    for module, description in core_tests:
        result = test_import(module, description)
        core_results.append(result)
    
    # Test LangChain dependencies
    print("\n🔗 Testing LangChain dependencies...")
    langchain_tests = [
        ("langchain", "LangChain"),
        ("langchain_community", "LangChain Community"),
        ("langchain.tools", "LangChain Tools"),
    ]
    
    langchain_results = []
    for module, description in langchain_tests:
        result = test_import(module, description)
        langchain_results.append(result)
    
    # Test CrewAI
    print("\n🤖 Testing CrewAI...")
    crewai_result = test_import("crewai", "CrewAI")
    
    # Test our custom modules
    print("\n🔧 Testing custom modules...")
    try:
        from project_analysis_crew_fixed import analyze_project
        print("✅ Project Analysis Crew - OK")
        custom_result = True
    except Exception as e:
        print(f"❌ Project Analysis Crew - FAILED: {e}")
        custom_result = False
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 Test Summary:")
    
    all_core = all(core_results)
    all_langchain = all(langchain_results)
    
    if all_core and all_langchain and crewai_result and custom_result:
        print("🎉 All tests passed! Your environment is ready.")
        print("\n🚀 You can now run the app with:")
        print("   python run_app.py")
        return True
    else:
        print("❌ Some tests failed. Please run the installation script:")
        print("   python install_dependencies.py")
        
        if not all_core:
            print("   - Core dependencies need to be installed")
        if not all_langchain:
            print("   - LangChain dependencies need to be installed")
        if not crewai_result:
            print("   - CrewAI needs to be installed")
        if not custom_result:
            print("   - Custom modules have issues")
        
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 