#!/usr/bin/env python
import sys
import os

# 添加正確的 src 目錄到 Python 路徑
current_file = os.path.abspath(__file__)
src_dir = os.path.join(os.path.dirname(current_file), 'src')
sys.path.insert(0, src_dir)

try:
    from ai_news.crew import AiNews
    from datetime import datetime

    def test_single_run():
        """
        測試單一主題運行
        """
        current_date = datetime.now()
        inputs = {
            'topic': 'Test FileWriterTool',
            'current_year': str(current_date.year),
            'date': f"{current_date.strftime('%Y-%m-%d')}_test"
        }
        
        print("🧪 Testing single topic with FileWriterTool...")
        AiNews().crew().kickoff(inputs=inputs)

    if __name__ == "__main__":
        test_single_run()
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()