![header](https://capsule-render.vercel.app/api?type=Waving&color=61380B&height=200&text=Project&fontColor=FFFFFF)

<h1 align="center"> 🍴 먹기 싫은 음식을 제외하고 추천하는 맛집 지도 🍴 </h1>
<div align='right'>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Folium-77B829?style=flat-square&logo=Folium&logoColor=white"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=VisualStudioCode&logoColor=white"/>
</div>

<br>
<br>
<br>
<h2 align="left"> 주제 선정 배경 </h2>
<p align="left">
  '야먹자'의 프로젝트는 이렇게 생겨났습니다!
  <br>
  <br>
  👩 : 우리 뭐 먹을까?<br>
  🧑 : 아무거나! 나는 어제 고기 먹어서 고기만 아니면 돼.<br>
  👩 : 나는 오늘 점심에 짬뽕을 먹어서 중국집은 싫어.<br>
  🧑 : 그럼 이 주변에서 뭘 먹어야하지?<br>
  <br>
  친구들과 저녁에 모여 메뉴를 정할 때면 항상 오랜 시간이 걸리고 힘들었습니다.<br>
  좋아하는 음식을 찾는 것보다 먹기 싫은 음식을 제외하는게 더 빨랐고, 이런 상황에서 아이디어가 떠올랐습니다.<br>
  그래서 '야먹자'는 일반적인 맛집을 추천해주는 서비스에 추가로 '먹기 싫은 음식을 제외'하는 기능을 넣게 되었습니다.
  <br>
  <h3 align='left'> 추가 기능 </h3>
  - 2차로 갈 수 있는 카페 추천☕<br>
  - 자차를 이용하는 사람들을 위해 주차장 위치 제공🅿️
</p>
<br>
<br>
<h2 align="left"> 사용 방법 </h2>
<h3 align='left'> 1. 원하는 지역명 검색 </h3>
'영등포' 입력 → '출발' 버튼 클릭<br>
<img src="https://github.com/syur997/Project_Yamukja/assets/110324563/395cfb9f-c69f-4b3d-a593-d8b511178324.png" width="400" height="150"/>
<br>
<br>
<h3 align='left'> 2. 검색한 지역의 식당 및 카페 확인 </h3>
마커를 누르지 않아도 식당 카테고리를 한 눈에 알아볼 수 있도록 'Folium Custom Icon'을 사용하여 직관적으로 표현<br>
<img src="https://github.com/syur997/Project_Yamukja/assets/110324563/398aa2b5-f1d0-49f0-916c-09c92f595695.png" width="400" height="300"/>
<br>
<br>
<h3 align='left'> 3. 원하는 식당(카페) 클릭 </h3>
지도에서 원하는 위치의 식당(카페)를 클릭 → 식당(카페)의 정보가 담긴 popup 표시<br>
<img src="https://github.com/syur997/Project_Yamukja/assets/110324563/35844d71-660f-44fa-83e3-7f0ae1143d03.png" width="400" height="400"/><br>
(식당명, 전화번호는 비식별화하였습니다.)<br>
<br>
<br>
<h3 align='left'> 4. 카테고리 필터링 </h3>
'먹기 싫은 음식을 제외'하는 주제에 맞게 메뉴별 카테고리를 필터링 할 수 있도록 OpenStreetMap 기능 사용<br>
<img src="https://github.com/syur997/Project_Yamukja/assets/110324563/fd2fcb55-0759-4327-823b-0c3a5fdf4f18.png" width="400" height="400"/><br>
- 카페와 주차장만 보고 싶은 경우 → '식당' 체크박스 해제 → 모든 '식당' 카테고리(한식, 양식, 중식 등)가 숨겨짐
<br>
<br>
<h3 align='left'> 5. 원하는 식당에서 맛있게 식사하기! </h3>
🍝 🍔 🍚 🍗 🍕 🍜 🍖 
