# PythonWebSite

영업활동에 따른 전자부품 Stock 구매를 위한 견적작업 대상 사이트의 검색 결과를 종합하여 게시하기 위한 프로젝트 구현 전 검색 자동화 테스트 작업 

이로 인해 대상 전자 부품의 재고 수량, 단가, 납기 정보를 한 번에 확인하여 업무 효율 향상 가능

## 개발환경

### Python3.x(3.11.5) 설치
```shell
$ python3 --version
```

- Window / MacOS : [Python](https://www.python.org/) 에서 설치파일 다운로드 받은 뒤 설치
- MacOS : ```brew install python3``` 명령어 설치 (Homebrew : 맥의 패키지 관리 Tool)

### Flask 2.3.x 설치

- Window / MacOS : [Flask](https://flask.palletsprojects.com) 에서 [Virtual environments](https://flask.palletsprojects.com/en/2.3.x/installation/#virtual-environments) 참고하기

- 환경 생성
```shell
$ mkdir {{폴더명}}
$ cd {{폴더명}}
# $ python3 -m venv .venv 여기까지 공홈에 있는 방법
$ python3 -m venv {{폴더명2}}
$ cd {{폴더명2}}
```
- 환경 활성화
```shell
$ cd bin
$ source activate
```
- Flask 설치
```shell
$ pip install Flask  
```

### Selenium 설치
```shell
$ pip install selenium  
```

### Flask 실행
```shell
$ flask --app {{실행할 파일명}} run
# or Python 실행
$ python {{실행할 파일명.py}}
```

### 디렉토리 구조

```shell
/homepage1
    /bin
    /include
    /lib
    /templates
      /index.html
      /results.html
    /hello.py
    /search.py
```
