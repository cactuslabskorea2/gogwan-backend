# Python 3.11 slim 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY main.py .
COPY reference_images/ ./reference_images/
COPY web_service/ ./web_service/

# Cloud Run은 PORT 환경 변수를 제공
ENV PORT=8080

# 애플리케이션 실행
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
