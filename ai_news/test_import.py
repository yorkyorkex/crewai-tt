#!/usr/bin/env python
import sys
import os

# 添加 src 目錄到 Python 路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    print("Testing imports...")
    from ai_news.crew import AiNews
    print("✅ AiNews import successful")
    
    print("Creating AiNews instance...")
    crew_instance = AiNews()
    print("✅ AiNews instance created")
    
    print("Getting crew...")
    crew = crew_instance.crew()
    print("✅ Crew created successfully")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()