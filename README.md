# Setitool_Docker 情緒分析工具
本專案是一個簡單的情緒分析網頁，前端使用 Vue 3 開發，後端使用 FastAPI。
前後端分離，並分別部署在 Google Cloud Run 上，達成即時情緒分析功能。

## 功能介紹
使用者輸入文字後，送到後端進行情緒分析
後端以 AI 模型分析文字內容情緒（正向、負向、中立）
將分析結果即時回傳前端顯示，正向及負向結果分別顯示晴天及雨天特效

## 技術架構
前端: Vue3 + Axios	Cloud Run (Docker + Nginx)
後端: FastAPI	Cloud Run (Docker)
雲端: Google Cloud Platform	

## 專案結構說明
Sentiment_Analysis：存放後端 FastAPI 程式碼

Vue_sent：存放前端 Vue 3 程式碼

## 前端部署流程
- 使用 npm run build 打包專案，產生 dist/ 資料夾
- 使用自訂 Dockerfile 及 nginx.conf 建立 Docker 映像檔
- 將映像檔 push 到 Google Container Registry
- 從映像檔部署至 Cloud Run，開放 8080 port
- 
## 後端部署流程
- 建立 FastAPI 專案，並撰寫 Dockerfile
- 同樣打包、push、部署到 Cloud Run
- 開放 8080 port，提供情緒分析 API
