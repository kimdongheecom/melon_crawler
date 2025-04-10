"""
AWS 서비스 어댑터 (AWS Service Adapter)

이 패키지는 AWS 클라우드 서비스와의 통합을 담당합니다.
주요 기능:
- AWS S3 스토리지 서비스 연동
- AWS Lambda 서버리스 컴퓨팅 연동
- AWS DynamoDB 데이터베이스 연동
- AWS SQS 메시지 큐 연동
- AWS CloudWatch 모니터링 연동

사용되는 주요 클래스:
- S3Adapter: S3 스토리지 서비스 연동
- LambdaAdapter: Lambda 함수 실행 관리
- DynamoDBAdapter: DynamoDB 데이터베이스 연동
- SQSAdapter: 메시지 큐 관리
- CloudWatchAdapter: 모니터링 및 로깅 관리
""" 