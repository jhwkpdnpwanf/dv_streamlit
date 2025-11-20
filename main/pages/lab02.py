import streamlit as st
from pathlib import Path

st.title("lab02: CCTV 지도 시각화 방식 비교")

# ------------------------------------------------
# 디렉터리 설정
# ------------------------------------------------
# 현재 파일: .../main/pages/lab02.py
BASE_DIR = Path(__file__).resolve().parents[1]
data_dir = BASE_DIR / "modules" / "lab02"

scatter_path = data_dir / "pydeck_cctv_scatter_map.html"
hexagon_path = data_dir / "pydeck_cctv_hexagon_map.html"
heatmap_path = data_dir / "pydeck_cctv_heatmap.html"


# ------------------------------------------------
# 1. CCTV 위치 산점도 지도 (ScatterplotLayer)
# ------------------------------------------------
st.subheader("1. CCTV 위치 산점도 지도")

st.markdown("""
이 지도는 **각 CCTV 설치 위치를 점으로 직접 표시하는 산점도(Scatterplot) 기반 시각화 지도**입니다.

- 위도·경도 좌표를 그대로 사용해 점을 찍는 방식입니다.
- 점의 크기·색을 단순하게 유지하여 순수한 위치 분포를 확인하기에 적합합니다.
- 특정 도로나 시설 주변의 설치 현황을 세밀하게 관찰할 때 유용합니다.   
""")

if scatter_path.is_file():
    with open(scatter_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=600, scrolling=False)
else:
    st.error(f"산점도 지도 HTML 파일을 찾을 수 없습니다: {scatter_path}")


# ------------------------------------------------
# 2. CCTV 밀집도 Hexagon 지도 (HexagonLayer)
# ------------------------------------------------
st.subheader("2. CCTV 밀집도 Hexagon 지도")

st.markdown("""
이 지도는 **3D로 CCTV 개수를 집계하여 시각화하는 HexagonLayer** 방식입니다.

- 지도 공간을 일정한 육각형 단위로 나누어 CCTV 개수를 집계합니다.
- 개수가 많을수록 색이 진해지고, 3D 높이가 커집니다.  
- 지역별 CCTV 밀집 패턴(고·저밀도 구역) 을 직관적으로 파악할 수 있습니다.  
""")

if hexagon_path.is_file():
    with open(hexagon_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=650, scrolling=False)
else:
    st.error(f"Hexagon 지도 HTML 파일을 찾을 수 없습니다: {hexagon_path}")


# ------------------------------------------------
# 3. CCTV Heatmap 지도 (HeatmapLayer)
# ------------------------------------------------
st.subheader("3. CCTV 밀도 Heatmap 지도")

st.markdown("""
이 지도는 PyDeck의 **HeatmapLayer를 활용한 열지도(Heatmap) 기반 시각화** 방식입니다.

- CCTV가 많이 밀집된 지역일수록 더 진하고 붉은 색으로 표현합니다.  
- HexagonLayer처럼 높이는 없고, 색 기반의 연속적인 밀도 표현이 특징입니다.    
- 연속적인 밀도 변화를 보기에 적합하여,  
  도심·상권·주거지의 CCTV 집중 경향을 빠르게 파악할 수 있습니다.  
""")

if heatmap_path.is_file():
    with open(heatmap_path, "r", encoding="utf-8") as f:
        html_str = f.read()
    st.components.v1.html(html_str, height=650, scrolling=False)
else:
    st.error(f"Heatmap 지도 HTML 파일을 찾을 수 없습니다: {heatmap_path}")


# ------------------------------------------------
# 4. 세 가지 시각화 방식 비교 요약
# ------------------------------------------------
st.subheader("4. 시각화 방식 비교 정리")

st.markdown("""
- **ScatterplotLayer (산점도)**  
  - 개별 CCTV 설치 위치를 정확한 좌표에 표시할 수 있습니다.  
  - 세밀한 위치 분석에 적합합니다.  

- **HexagonLayer (3D 밀집도)**  
  - 영역 단위로 CCTV 개수를 집계합니다.  
  - 지역별 밀집 구역을 직관적으로 파악하기 좋습니다.     

- **HeatmapLayer (히트맵)**  
  - 색의 농도로 연속적인 밀도를 표현합니다.  
  - 도시의 CCTV 집중권을 빠르게 시각화하는 데 적합합니다.  

같은 CCTV 데이터를 사용하더라도,  
시각화 방식에 따라 강조되는 정보가 어떻게 달라지는지 확인할 수 있는 예시입니다.
""")
