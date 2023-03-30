# Portfolio

1. Python 가상환경을 일치시켜줍니다.  아래 순서대로 진행
```
# 가상환경 생성
cd myproject
python -m venv .venv

# 가상환경 접속
$ . .venv/bin/activate   # Linux
$ . .venv/Script/activate  # Windows

# 가상환경 패키지 설치
pip install -r requirements.txt

```

2. 서버를 구동합니다.
```
cd myproject
python manage.py runserver 
```
