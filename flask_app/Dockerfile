# 使用官方的Python基礎鏡像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製requirements.txt並安裝依賴
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式文件
COPY app/ app/

# 暴露應用程式的端口
EXPOSE 5000

# 運行Flask應用
CMD ["python", "app/main.py"]
