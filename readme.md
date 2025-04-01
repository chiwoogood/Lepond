# Lepond
[Lepond](https://lepond.kr)

## 📌 프로젝트 개요

개발자가 아닌 사람도 홈페이지 및 상품을 관리할 수 있는 쇼핑몰을 구현 중입니다.

## 1. 기능 

### 1. 회원 관리

- 사용자 회원가입 및 로그인  
- 회원정보 수정, 탈퇴 (예정)  
- 마케팅 수신 동의 여부 저장  
- 관리자 페이지 접근 제어  
- 유저별 다중 주소 설정 및 기본 주소 설정(예정)
- 구매 내역(예정)
- 배송 조회(예정)
- 마이 페이지(Order, Cart, Profile, Address, MyCommunity, Contact)
---

### 2. 상품 기능

- 상품 리스트 페이지  
- 상품 상세 페이지  
  - 썸네일 이미지  
  - 옷 상세 설명  
  - 가격  
  - 재고  
  - 사이즈 옵션  
  - 컬러 옵션  
  - 구매 이력 있는 사용자 기준 별점 옵션(예정)
- 상품별 리뷰
  - 리뷰 리스트(예정)
  - 구매 이력 있는 사용자 기준 및 리스트 작성(예정)
- 상품별 Q&A 게시판  
  - 관리자 답변 여부 및 답변(예정)  

---

### 3. 게시판 시스템

- **공지사항 (Notice)**  
  - 관리자 작성
  - 공지사항 조회수(예정)  
- **리뷰 (Review)**  
  - 로그인 사용자만 작성 가능  
  - 별점 포함 (예정)  
- **문의사항 (Q&A)**  
  - 비공개/공개 설정 가능 (예정)  
  - 관리자 답변 기능 제공 (예정)  

---

### 4. 관리자 기능

- 상품 등록 / 수정 / 삭제  
- 상품 카테고리 설정  
- 사용자 Q&A 답변  
- 리뷰 및 문의 모니터링  

---

### 5. 장바구니 기능 **(개발 예정)**

- 로그인 사용자별 장바구니 저장  
- 수량 변경 및 선택 삭제 
- 장바구니에서 결제 연동  

---

### 6. 주문 및 결제 시스템 **(개발 예정)**

- 주문서 작성 및 결제 수단 선택  
- 결제 완료 후 주문 내역 저장 및 재고 차감  
- 주문 상태 확인  
  - 결제 완료 / 배송 조회  
- 주문 취소 및 환불 처리  

---

## 2. Version

- ### Backend
  - Django 4.2.4
  - Python 3.11.9

- ### Database
  - Maria 11.7.2

- ### DevOps / Infra
  - Docker 28.0.4
  - Docker Compose 2.34.0
  - Gunicorn 23.0.0
  - Nginx 1.27.4
  - AWS EC2 (Ubuntu 22.02)
  - AWS S3
  - AWS Route 53

- ### API
  - Solapi AlimTalk API
  - daum 도로명 주소 API

## 4.Structure
accounts/ : 사용자 인증, 회원 가입, 로그인, 주소지 설정, 내 Q&A 모아보기, 내 Review 모아보기, 회원 정보 수정 

shop/ : Product list, Product detail, Product Image, Thumbnails, Color, status, metarial, caution, content, review, Q%A, User Rating

main/ : Privacy, Instagram, About Lepond, Contact, Main Image, footer message, message Framework

community/ : Notice, Q&A List, Q%A 작성, Review List, Review, 

payments/ : 결제 예정

carts/ : 장바구니 예정

templates/ : base.html, product.html로 템플릿 상속
base.html과 product.html과 다른 차이는 product.html를 상속하는 경우에는 제공하는 Image, html이 많아 모바일에 적합


/ : 주문/결제 기능

## 5. ERD

### 메인 ERD
![메인ERD](./mainerd.png)
admin페이지에서 메인 이미지, FooterMessage등을 변경 가능
봄에는 노란 꽃 이미지, 여름엔 좀 시원해보이는 걸로, 가을에는 낙엽, 겨울에는 하얗게
FooterMessage는 배송이 지연되거나 명절 때 이용할 계획(ex 추석 명절로 ~~~날 부터 배달 시작돼염) 

### 유저 ERD
![유저ERD](./usererd.png)
유저별 구매 내역, 배송 조회 기능 추가 예정정

### 샵 ERD
![샵ERD](./shoperd.png)


### 커뮤니티 ERD
![커뮤니티ERD](./communityerd.png)


### 프로젝트 ERD
![전체ERD](./erd.png)

**payments, carts 추가 예정**

## 6. Superuser
관리자 계정 및 테스트용 구매자 계정 정보
[관리자 페이지](https://www.lepond.kr/admin) 
ID : admintest
PW : lepondtest123!

## 7. 개발 기간 및 일정
개발 기간: 2024.12 ~ 2025.09 (9개월 목표)



## 8. 개선 예정 사항
쇼핑몰 프로젝트를 AWS EC2 기반으로 구축하면서 인프라에 대한 이해도와 실습 경험을 쌓을 수 있었다는 점에서 의미가 있었지만, 1인 개발자 입장에서 유지 비용 측면에서는 다소 부담이 되는 부분이 있었다.

EC2 + EBS + S3 + 도메인 + 알림톡(Solapi) 등을 모두 합산하면,
월 기본 유지비만 약 5만 원 이상 발생하고, 알림톡 사용량에 따라 6~7만 원을 넘어설 수도 있음

처음 예상했던 비용보다 실제 운영비가 더 높게 나왔고,
Cafe24와 같은 호스팅 서비스와 비교했을 때 '크게 저렴하다는 느낌은 들지 않음'

또한 EC2는 설정 자유도는 높지만 트래픽 과금, 스토리지 관리, 로그 처리 등을 모두 수동으로 해야 해 운영 부담도 있었음.

✅ 향후 계획
프로젝트 기능이 완성된 이후에는 비용 효율성과 운영 간소화를 위해,
AWS Lightsail로 이전할 예정이다.

Lightsail은 월 3.5달러(약 5천 원)부터 시작 가능하며,
트래픽 포함 요금제로 예측 가능한 비용 관리가 가능

정말 만약에 너무 잘되면 다시 EC2로 옮길 예정


이미지 기본 가로 세로 px 설정
- 600 * 800으로 고정할 때 이쁜 것 같긴함 
페이지 렌더링 지연시 Bootstrap Spinner추가 예정
404.page, 50x page등 에러시 페이지 개선 예정