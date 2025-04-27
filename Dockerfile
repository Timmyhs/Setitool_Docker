FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# 開放端口
EXPOSE 8080

# 啟動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]