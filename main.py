



# main.py 开头添加以下代码
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()  # 自动读取项目根目录的 .env 文件

# 读取 API 密钥
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

# 校验密钥是否加载成功
if not DASHSCOPE_API_KEY:
    raise ValueError("❌ 未找到 DASHSCOPE_API_KEY！请检查 .env 文件是否配置正确")

# 后续正常使用密钥调用 API 即可
print(f"✅ API 密钥加载成功（前8位）：{DASHSCOPE_API_KEY[:8]}...")






import json
import logging
from agent import VideoFileOperationAgent

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    agent = VideoFileOperationAgent()
    result = agent.run({
        "video_path": "../video/42.mp4",
        "keywords": ["食品生产许可证申请书", "法定代表人授权委托书"],
        "rec_start": "2026-01-30 10:09:00",
        "search_start": "2026-01-30 10:09:00",
        "search_end": "2026-01-30 10:10:00"
    })
    
    print(json.dumps(result, indent=4, ensure_ascii=False))
    
    events = result.get("events", [])
    if events:
        first_event = events[0]
        print(f"\n✅ 成功捕获事件！")
        print(f"事件的应用名称是: {first_event.get('app_name', '未识别到应用名称')}")
        print(f"具体行为: {first_event.get('behavior_category', '未知')}")
        print(f"操作描述: {first_event.get('description', '无')}")
        print(f"第一个事件的操作类型是: {first_event.get('operation_type', '未知')}")
        print(f"变更前文件名是: {first_event.get('original_filename', '未知')}")
        print(f"变更后文件名是: {first_event.get('modified_filename', '未知')}")
    else:
        print("\n⚠️ 未能识别到任何有效事件。")