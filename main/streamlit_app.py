import streamlit as st

st.title("데이터시각화 11장")


# 페이지 설정
st.set_page_config(
    page_title="seo._.bangwool's Streamlit",
    page_icon="🙂",
    layout="wide",

    initial_sidebar_state="expanded",

    menu_items={
        'Get help': "https://docs.streamlit.io",
        'Report a bug': "https://streamlit.io",
        'About': "# 서장훈 \n - 홍익대학교 (https://www.hongik.ac.kr)"
    }
)


# 사이드바
#st.sidebar.title("위젯")

#st.sidebar.checkbox("외국인 포함")
#st.sidebar.checkbox("고령인구 포함")

# 구분선
#st.sidebar.divider()

# 라디오 버튼
#st.sidebar.radio("데이터 타입", ['전체', '남성', '여성'])

# 슬라이더
#st.sidebar.slider("나이", 0, 100, (20, 50))

# 셀렉트박스
#st.sidebar.selectbox("지역", ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])
