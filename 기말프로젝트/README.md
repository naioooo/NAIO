# Term_Project 2017182005 김민규


## 1. 게임의 소개

__제목 : 일대일 2D 축구__

 

- copy 게임이라면, 원 게임에 대한 정보 및 스크린샷

 

사진 클릭시 게임에 대한 설명으로 이동

[![Alt text](https://user-images.githubusercontent.com/34563332/94274827-22ec5880-ff81-11ea-9411-9277b92db746.jpg)](https://namu.wiki/w/Head%20Soccer)



 

__- 게임의 목적, 방법 등 간단한 설명__

   

   게임은 2P로 진행되며 주어진 시간동안 각 상대팀 골대를 향해 볼을 집어넣어 더 많은 점수를 획득하여 승리를 하는 

   2D형식의 일대일 축구 게임입니다.

 

 

## 2. GameState (Scene) 의 수 및 각각의 이름

 

  1. 타이틀 로딩화면

 

  2. 게임시작타이틀화면

 

  3. 선수 선택 화면

 

  4. 게임 화면

 

     총 4가지로 구성되었습니다.

 

## 3. 각 GameState 별 다음 항목

 

__- 한줄짜리 설명__

  1. 타이틀 로딩화면

       게임을 시작하는 간략적인 화면입니다.

     

  2. 게임시작타이틀화면

       스타트 버튼을 누르면 선택창으로 넘어가는 화면입니다.

 

  3. 선수 선택 화면

       각각의 플레이어는 선수를 선택할 수 있는 선택화면입니다.

 

  4. 게임 화면

       고른 선수들로 게임이 이루어 지는 화면입니다.

 

__- 화면에 표시할 객체들의 목록__

  1. 타이틀 로딩화면  
  
       없습니다       
         
  2. 게임시작타이틀화면
        
       스타트 버튼 객체 
       
       
  3. 선수 선택 화면

       선수들을 나열하는 객체, 준비완료를 누르는 버튼 객체, 게임 시작버튼 객체


  4. 게임 화면

       선수 객체, 공 객체, 골대 객체, 스코어 객체, 땅 객  

 

__- 처리할 키/마우스 등 이벤트__

     

  2. 게임시작타이틀화면

      아무키나 누르면 다음 화면으로 넘어가는 이벤트

 

  3. 선수 선택 화면

      키보드를 이용해 선수를 탐색하며 선수를 고를수있는 이벤트

 

  4. 게임 화면

       방향키와 임의의 슛키를 활용해 볼을 다루며 차는 이벤트

 

__- 다른 State 로 이동한다면, 각 이동에 대한 조건 및 방법__


![Alt text](https://user-images.githubusercontent.com/34563332/94274831-241d8580-ff81-11ea-9efd-3fbad3b25263.jpg)



## 4. 필요한 기술

__- 다른 과목에서 배운 기술__

     공을 자연스럽게 움직이기 위한 알고리즘

     

__- 이 과목에서 배울 것으로 기대되는 기술__

     게임 스테이트 변환을 통한 자연스러운 ui

     파이썬을 통해 여러 파일로 분할하여 간단하게 만드는 함수

     

 

__- 다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술 (이 항목은 과제 본문에도 적어 낸다)__

    
     캐릭터가 이동하며 화면 끝에 도달할때 자연스러운 카메라의 움직임
     
     공의 움직임을 더욱 자연스럽게 만들 수 있는 알고리즘

     
 __- 기말프로젝트 1차 발표 ppt 내용

![Alt text](https://user-images.githubusercontent.com/34563332/95649615-3c60d900-0b19-11eb-91e8-043f5bced660.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649634-687c5a00-0b19-11eb-925e-eb2afecd2242.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649639-78943980-0b19-11eb-89a6-7ec6308f2b42.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649644-7f22b100-0b19-11eb-8a63-8639d195fbdf.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649647-83e76500-0b19-11eb-9b90-1f4a563754c9.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649655-91045400-0b19-11eb-9062-e7a45d30747e.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649658-95c90800-0b19-11eb-9e9d-1d103b90e2e8.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649664-99f52580-0b19-11eb-92f5-80fd46f03f49.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649666-9eb9d980-0b19-11eb-85d0-bebc444974ad.png)

![Alt text](https://user-images.githubusercontent.com/34563332/95649669-a4172400-0b19-11eb-9f23-65df6d58e0aa.png)


 

 


     
