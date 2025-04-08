# Melon API

FastAPI 기반의 웹 애플리케이션입니다.

## 시작하기

### 요구사항
- Docker
- Docker Compose

### 설치 및 실행

1. 저장소 클론
```bash
git clone [repository-url]
cd melon
```

2. Docker 컨테이너 실행
```bash
docker-compose up --build
```

3. API 접속
- Swagger UI: http://localhost:8888/docs
- API 서버: http://localhost:8888

## API 엔드포인트
- GET /: Welcome 메시지
- /users: 사용자 관련 API (prefix) 