import streamlit as st
from pathlib import Path

st.title("아파트 실거래가 지도 시각화")

# ------------------------------------------------
# 디렉터리 설정
# ------------------------------------------------
# 현재 파일: .../main/pages/lab03.py
BASE_DIR = Path(__file__).resolve().parents[1]
data_dir = BASE_DIR / "modules" / "lab03"

scatter_path = data_dir / "pydeck_apt_scatter.html"
hexagon_path = data_dir / "pydeck_apt_hexagon.html"
polygon2d_path = data_dir / "pydeck_apt_polygon_2d.html"
polygon3d_path = data_dir / "pydeck_apt_polygon_3d.html"


# ------------------------------------------------
# 1. 아파트 거래 산점도 지도 (개별 거래 위치)
# ------------------------------------------------
st.subheader("1. 아파트 거래 산점도 지도")

st.markdown("""
아파트 실거래가 데이터를 개별 거래 단위로 표시한 지도입니다.

- 각 점은 한 건의 아파트 거래를 의미합니다.  
- 위도, 경도 정보를 그대로 사용해 지도 위에 위치를 표시합니다.  
- 거래가 많이 이루어진 지역일수록 점이 조밀하게 모여 보입니다.  
""")

if scatter_path.is_file():
    with open(scatter_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=600, scrolling=False)
else:
    st.error(f"산점도 지도 HTML 파일을 찾을 수 없습니다: {scatter_path}")


# ------------------------------------------------
# 2. 아파트 거래 Hexagon 밀집도 지도
# ------------------------------------------------
st.subheader("2. 아파트 거래 Hexagon 밀집도 지도")

st.markdown("""
같은 거래 데이터를 기반으로, **일정 영역별 거래 밀집도를 보여주는 Hexagon 방식** 지도입니다.

- 지도를 육각형 격자로 나누고, 각 격자에 포함된 거래 건수를 집계합니다.  
- 거래가 많을수록 색이 진해지고, 3차원 높이가 높게 표시됩니다.  
- 개별 위치보다는, 어느 지역에 거래가 많이 몰려 있는지를 한눈에 보기 좋습니다.
""")

if hexagon_path.is_file():
    with open(hexagon_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=650, scrolling=False)
else:
    st.error(f"Hexagon 지도 HTML 파일을 찾을 수 없습니다: {hexagon_path}")


# ------------------------------------------------
# 3. 구별 아파트 거래 요약 지도 (2D Polygon)
# ------------------------------------------------
st.subheader("3. 구별 요약 값 2D 폴리곤 지도")

st.markdown("""
행정구역(예: 자치구) 단위로 아파트 거래 정보를 집계하여 **색으로 표현한 2차원 폴리곤 지도**입니다.

- 각 폴리곤은 하나의 행정구를 의미합니다.  
- 구별 요약 지표(예: 평균 거래금액, 거래 건수 등)를 색의 농도로 표현합니다.  
- 지도의 높이는 사용하지 않고, 평면 상에서 구별 차이를 비교하는 데 초점을 둡니다.
""")

if polygon2d_path.is_file():
    with open(polygon2d_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=650, scrolling=False)
else:
    st.error(f"2D 폴리곤 지도 HTML 파일을 찾을 수 없습니다: {polygon2d_path}")


# ------------------------------------------------
# 4. 구별 아파트 거래 요약 지도 (3D Polygon)
# ------------------------------------------------
st.subheader("4. 구별 요약 값 3D 폴리곤 지도")

st.markdown("""
위의 **2D 폴리곤 지도를 3차원으로 확장한 지도**입니다.

- 각 구의 요약 지표를 색뿐 아니라 높이로도 표현합니다.  
- 값이 큰 구는 색이 진하고, 기둥처럼 더 높게 솟아오른 형태로 보입니다.  
- 구별 상대적인 차이를 직관적으로 파악하기 좋습니다.
""")

if polygon3d_path.is_file():
    with open(polygon3d_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=650, scrolling=False)
else:
    st.error(f"3D 폴리곤 지도 HTML 파일을 찾을 수 없습니다: {polygon3d_path}")


# ------------------------------------------------
# 5. 시각화 방식 비교 정리
# ------------------------------------------------
st.subheader("5. 시각화 방식 비교")

st.markdown("""
- **산점도 지도**: 개별 거래 위치를 그대로 보여 주는 방식  
- **Hexagon 지도**: 일정 영역별 거래 밀집도를 강조하는 방식  
- **2D 폴리곤 지도**: 구 단위 요약 값을 색으로 표현  
- **3D 폴리곤 지도**: 구 단위 요약 값을 색과 높이로 동시에 표현  

동일한 아파트 실거래가 데이터를 사용하더라도,  
어떤 시각화 방식을 선택하는지에 따라 강조되는 정보가 달라진다는 점을 보여주는 예시입니다.
""")
