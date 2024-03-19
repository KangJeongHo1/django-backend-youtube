# 1일차
## 프로젝트 셋팅
### 1. Github
- 레포지토리 생성 => 명령어 그대로 복붙
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결
- git clone https://github.com/KangJeongHo1/django-backend-youtube

### 2. Docker Hub
- 회원가입
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis))
- AccessToken 값을 Github 레포지토리에 등록

### 3. Django 프로젝트 세팅
- 실제 베포 환경
- requirement.txt => 실제 베포할 때 사용
- requirement.dev.txt => 개발하고 연습할 떄 사용 (파이썬 패키지 관리)
- 실전 : 패키지 의존성 관리 => 버전관리, 패키지들 간의 관계 관리

- docker-compose run --rm app sh -c 'python manage.py runserver'

*3/15 주말 공부*
- 도커 배운 것 정리
- 유튜브(인기 급상승) 데이터베이스 모델 구조 고민해오기
    - user: username(charfield)
    - 구독은 어떻게 하는지, 좋아요, 싫어요 등등

## Youtube API 개발

### (1) 모델 구조
1. User (Custom)
- email
- password
- nickname
- is_business(boolean): personal, business

2. Video
- title
- link
- description
- category
- views_count
- thumbnail
- video_uploaded_url (S3)
- video_file(FileField)
- User:FK

3. Reaction
- User:FK
- Video:FK
- reaction

4. Comment
- User:FK
- Video:FK
- like
- dislike
- content

5. Subcription (채널 구독)
- User:FK => subscriber (구독한) -> 내가 구독한 사람
- User:FK => subscribed_to (구독을 당한) -> 나를 구독한 사람

6. Notification

- User:FK
- message
- is_read

7. Common

- created_at
- updated_at

8. Chatting (예정)
- User:FK (nickname)


만들어야 하는 테이블(모델)
- users, videos, reactions, comments, subscriptions, common
- docker-composer run --rm app sh -c 'python manage.py startapp users'
- docker-composer run --rm app sh -c 'python manage.py startapp videos'
- docker-composer run --rm app sh -c 'python manage.py startapp reactions'
- docker-composer run --rm app sh -c 'python manage.py startapp comments'
- docker-composer run --rm app sh -c 'python manage.py startapp subscriptions'
- docker-composer run --rm app sh -c 'python manage.py startapp common'

### Custom User Model Create

- TDD => 개발 및 디버깅 시간을 엄청나게 줄일 수 있습니다. PDB(Python Debugger)

## DRF 세팅
- DjangoRestframework
- drf-spectacular / swagguer-ui, redoc / requirements.txt 추가
- docker-compose build