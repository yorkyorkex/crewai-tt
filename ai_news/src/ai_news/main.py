#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

# 添加正確的 src 目錄到 Python 路徑
current_file = os.path.abspath(__file__)
print(f"Current file: {current_file}")

# 從 ai_news/src/ai_news/main.py 向上兩層到 ai_news/src
src_dir = os.path.dirname(os.path.dirname(current_file))
print(f"Src directory: {src_dir}")

sys.path.insert(0, src_dir)
print(f"Python path: {sys.path[:3]}")

try:
    from ai_news.crew import AiNews

    warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

    # This main file is intended to be a way for you to run your
    # crew locally, so refrain from adding unnecessary logic into this file.
    # Replace with inputs you want to test with, it will automatically
    # interpolate any tasks and agents information

    def run():
        """
        Run the crew.
        """
        current_date = datetime.now()
        inputs = {
            'topic': 'AI LLMs',
            'current_year': str(current_date.year),
            'date': current_date.strftime('%Y-%m-%d')
        }
        
        try:
            AiNews().crew().kickoff(inputs=inputs)
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")

    if __name__ == "__main__":
        run()
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()