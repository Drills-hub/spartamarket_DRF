# spartamarket_DRF

Django REST Framework를 학습하기 위한 spartamarket_DRF 프로젝트 입니다.


## 목차

- [개발 환경](#개발환경)
- [소개 및 앱 구성](#소개및앱구성)
- [ERD](#ERD)
- [기능](#기능)


# 개발 환경

- **프레임워크 및 라이브러리**
  - Django: 4.2
  - Django REST Framework: 3.15

- **언어**
  - Python: 3.10

- **운영 체제**
  - Windows 11

- **데이터베이스**
  -SQLite3: 3

- **개발 도구**
  - Visual Studio Code
 



## 소개 및 앱 구성

이 프로젝트의 목적은 Django REST Framework를 학습하기 위한 spartamarket_DRF 프로젝트 입니다.
중고 마켓을 모티브로 구성 되어있으며,기본적인 회원기능과 상품기능으로 구분되어있습니다.

앱의 구성은 크게 두 가지로 회원기능인 "accounts"와 상품기능인"products"로 나누어 집니다.
<details>
  <summary>accounts</summary>
📦accounts
 ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┣ 📜0002_user_name_alter_user_gender.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜0001_initial.py
 ┃ ┣ 📜0002_user_name_alter_user_gender.py
 ┃ ┗ 📜__init__.py
 ┣ 📂__pycache__
 ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┣ 📜serializer.cpython-310.pyc
 ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┗ 📜__init__.cpython-310.pyc
 ┣ 📜admin.py
 ┣ 📜apps.py
 ┣ 📜models.py
 ┣ 📜serializer.py
 ┣ 📜tests.py
 ┣ 📜urls.py
 ┣ 📜views.py
 ┗ 📜__init__.py
</details>
<details>
  <summary>products</summary>
  📦products
 ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜0001_initial.cpython-310.pyc
 ┃ ┃ ┣ 📜0002_hashtag_product_hashtag.cpython-310.pyc
 ┃ ┃ ┣ 📜0003_rename_hashtag_product_hashtags.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┣ 📜0001_initial.py
 ┃ ┗ 📜__init__.py
 ┣ 📂__pycache__
 ┃ ┣ 📜admin.cpython-310.pyc
 ┃ ┣ 📜apps.cpython-310.pyc
 ┃ ┣ 📜models.cpython-310.pyc
 ┃ ┣ 📜serializer.cpython-310.pyc
 ┃ ┣ 📜urls.cpython-310.pyc
 ┃ ┣ 📜views.cpython-310.pyc
 ┃ ┗ 📜__init__.cpython-310.pyc
 ┣ 📜admin.py
 ┣ 📜apps.py
 ┣ 📜models.py
 ┣ 📜serializer.py
 ┣ 📜tests.py
 ┣ 📜urls.py
 ┣ 📜views.py
 ┗ 📜__init__.py
</details>
# ERD


## 기능

프로젝트의 주요 기능을 나열합니다.
- 기능 1
- 기능 2
- 기능 3

## 설치 방법

프로젝트를 설치하는 방법을 단계별로 설명합니다. 예를 들어:

```bash
git clone https://github.com/username/repository.git
cd repository
pip install -r requirements.txt
