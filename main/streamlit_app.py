import streamlit as st

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="seo._.bangwool's Streamlit",
    page_icon="😺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# CSS 스타일
# -------------------------------------------------
st.markdown("""
<style>

html, body {
    font-family: 'Segoe UI', sans-serif;
}

/* 큰 타이틀 */
.big-title {
    font-size: 2.1rem;
    font-weight: 700;
    color: #111;
    padding-bottom: 0.2rem;
}

/* 부제목 */
.subtitle {
    font-size: 1.05rem;
    color: #333;
    margin-bottom: 1rem;
}

/* 라이트 인포 카드 */
.info-box {
    padding: 1rem 1.3rem;
    background: #f4f4f4;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    margin-bottom: 1.4rem;
    font-size: 0.97rem;
    color: #333;
}

/* 카드 기본 */
.card {
    padding: 1.2rem 1.4rem;
    background: #f8f8f8;
    border-left: 6px solid #444;
    border-radius: 8px;
    margin-bottom: 1.2rem;
}

/* 섹션 제목 */
.section-title {
    font-size: 1.35rem;
    font-weight: 650;
    margin-top: 2.2rem;
    padding-bottom: 0.2rem;
    border-bottom: 2px solid #d3d3d3;
    color: #111;
}

/* footer */
.footer-card {
    padding: 1rem 1.3rem;
    background: #fafafa;
    border-radius: 8px;
    border: 1px solid #e6e6e6;
    font-size: 0.95rem;
}

/* bullet 아이콘 */
.icon-bullet {
    font-size: 1.2rem;
    margin-right: 6px;
    color: #444;
}

</style>
""", unsafe_allow_html=True)



# -------------------------------------------------
# 메인 제목
# -------------------------------------------------
st.markdown("<div class='big-title'>데이터시각화 실습 페이지</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>공공데이터 기반 시각화 실습을 위한 Streamlit 프로젝트입니다.</div>", unsafe_allow_html=True)



# -------------------------------------------------
# 소개 인포박스
# -------------------------------------------------
st.markdown("""
<div class='info-box'>
  이 프로젝트는 데이터시각화 수업의 실습 내용을 정리한 페이지입니다.<br>
  여러 공공데이터를 활용해 다양한 시각화 기법을 실습하고 비교할 수 있도록 구성되어 있습니다.<br>
  lab2와 lab3는 각 lab 폴더의 
  <b>make_files_code.ipynb</b>에서 html 파일 생성 과정을 확인할 수 있습니다.<br>
  원하는 실습 페이지는 좌측 사이드바에서 선택할 수 있습니다.
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 실습 페이지 구성
# -------------------------------------------------
st.markdown("<div class='section-title'>실습 페이지 구성</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
  <span class='icon-bullet'>▪️</span>
  <b>lab01 — 범죄·치안 데이터 시각화</b><br>
  CCTV·경찰관서·인구·범죄 발생 데이터를 비교하고,<br>
  상관계수 히트맵, 막대그래프, 선그래프 등 다양한 시각화를 수행합니다.
</div>

<div class='card'>
  <span class='icon-bullet'>▪️</span>
  <b>lab02 — PyDeck 지도 시각화</b><br>
  CCTV 위치 데이터를 활용해 산점도, Hexagon 밀집도, Heatmap 등<br>
  서로 다른 공간 시각화를 비교하고 분석합니다.
</div>

<div class='card'>
  <span class='icon-bullet'>▪️</span>
  <b>lab03 — 부동산 실거래가 분석 (예정)</b><br>
  매매/전월세 실거래가를 이용한 가격 분포 및 지역별 분석 등을 다룰 예정입니다.
</div>
""", unsafe_allow_html=True)



# -------------------------------------------------
# 데이터 출처 (URL + 사용한 데이터 설명)
# -------------------------------------------------
st.markdown("<div class='section-title'>데이터 출처</div>", unsafe_allow_html=True)

st.markdown(
    """
<div class="footer-card">

  <p style="margin:0 0 8px 0;">
    <b>서울 열린데이터광장</b><br>
    <a href="https://data.seoul.go.kr/" target="_blank">
      https://data.seoul.go.kr/
    </a><br>
    - 서울시 자치구 CCTV 설치현황<br>
    - 서울시 5대 범죄 발생현황
  </p>

  <p style="margin:8px 0 8px 0;">
    <b>공공데이터포털</b><br>
    <a href="https://www.data.go.kr/" target="_blank">
      https://www.data.go.kr/
    </a><br>
    - 국토교통부 아파트 매매 실거래가
  </p>

  <p style="margin:8px 0 8px 0;">
    <b>VWorld</b><br>
    <a href="https://www.vworld.kr/" target="_blank">
      https://www.vworld.kr/
    </a><br>
    - 행정경계(시군구) 공간 데이터
  </p>

  <p style="margin:8px 0 0 0;">
    <b>Mapshaper</b><br>
    <a href="https://mapshaper.org/" target="_blank">
      https://mapshaper.org/
    </a><br>
    - 행정경계 GeoJSON 단순화 및 가공
  </p>

</div>
""",
    unsafe_allow_html=True,
)




# -------------------------------------------------
# 사이드바
# -------------------------------------------------
st.sidebar.title("메뉴")
st.sidebar.markdown("실습 페이지로 이동하세요.")
st.sidebar.markdown("---")