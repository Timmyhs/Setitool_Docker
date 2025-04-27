from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os


app = FastAPI()

# 設定 CORS，前端 localhost:8080 發送請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #"http://localhost:8080"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 Gemini API
GOOGLE_API_KEY = "AIzaSyBZhJ8r2NkVNuIWhH3BefBDeQQprJ4WNlE"
genai.configure(api_key=GOOGLE_API_KEY)

# 定義輸入格式
class TextInput(BaseModel):
    content: str

@app.post("/analyze")
async def analyze_text(data: TextInput):
    try:
        print(f"Received content: {data.content}")  # 輸入的內容
        # Gemini prompt 避免模型暴走
        prompt = f"""
        你是一個情緒分析模型，只需要回覆三種結果之一：正面、中性、負面。
        使用者輸入：「{data.content}」
        請根據文字情緒內容判斷並只回覆一個詞：正面、中性 或 負面，不要多說話。
        """

        model = genai.GenerativeModel("gemini-1.5-flash") #gemini-pro
        response = model.generate_content(prompt)
        result = response.text.strip()

        # 基本驗證
        if result not in ["正面", "中性", "負面"]:
            result = "無法判斷"

        return {"result": result}

    except Exception as e:
        print(f"Error: {str(e)}")  # Test
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        return {"error": str(e)}
