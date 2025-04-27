# 使用 Nginx 作為 Web 伺服器
FROM nginx:alpine

# 複製自訂的 nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 複製靜態檔案
COPY dist/ /usr/share/nginx/html

# 開放 8080 端口，且讓 Cloud Run 知道要綁定到 8080
EXPOSE 8080

# 直接啟動 nginx
#Test