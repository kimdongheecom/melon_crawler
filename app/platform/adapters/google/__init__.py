"""
Google 서비스 어댑터 (Google Service Adapter)

이 패키지는 Google 클라우드 서비스와의 통합을 담당합니다.
주요 기능:
- Google Cloud Storage 연동
- Google Cloud Functions 서버리스 연동
- Google BigQuery 데이터 분석 연동
- Google Cloud Pub/Sub 메시징 연동
- Google Cloud Monitoring 모니터링 연동

사용되는 주요 클래스:
- GCSAdapter: Cloud Storage 연동
- GCFAdapter: Cloud Functions 관리
- BigQueryAdapter: BigQuery 데이터 분석
- PubSubAdapter: 메시지 큐 관리
- MonitoringAdapter: 모니터링 및 로깅 관리
""" 