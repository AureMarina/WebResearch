from openai import OpenAI
import os
from dotenv import load_dotenv

# ================ 1. 初始化llm =====================

load_dotenv()
base_url = os.getenv("bapi_url")
base_key = os.getenv("bapi_key")

client = OpenAI(base_url = base_url, api_key = base_key)

# resp = client.responses.create(
#     model="gpt-4.1",
#     input=[{
#         "role": "user",
#         "content": "给我讲一个冷笑话"
#     }]
# )
# print(resp.output_text)
