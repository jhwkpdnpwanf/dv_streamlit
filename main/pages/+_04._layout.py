import pandas as pd
import streamlit as st


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
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>04. Streamlit 기능 실습: Layout</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>데이터시각화 강의록을 따라가며 작성해보았습니다. <div>", unsafe_allow_html=True)

st.markdown("---")











import pandas as pd
df = pd.DataFrame(
    {'id': [1, 2, 3],
     'name': ['Alice', 'Bob', 'Charlie'],
     'age': [24, 34, 45]
     }
)




'## [Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=["a", "b", "c"]
)


'##### :orange[st.area_chart()]'
st.area_chart(chart_data)

'### :orange[(Metric)]'
coll, col2, col3 = st.columns (3) #3개의 컬럼 생성
coll.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
columns=["lat", "lon"],
)

st.map(df)





'### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)  # 👉 차트 출력

st.divider()    # 👉 구분선




'### :orange[Altair: st.altair_chart()]'

import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x="a", y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"]
    )
)

st.altair_chart(c, use_container_width=True)




'### :orange[Plotly: st.plotly_chart()]'
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
st.plotly_chart(fig, key="iris", on_select="rerun")



'### :orange[컬럼: st.columns()]'
col_1, col_2, col_3 = st.columns([1,2,1])   # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('### 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('### 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])    
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 내용을 변경해야 오류가 없음

col_3.write('### 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에, 여기서는 셀렉트박스의 내용을 변경해야 오류가 없음


'### :orange[탭: st.tabs()]'

# 탭 인스턴스 생성. 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])

with tab_1:
    st.write(
        '''
        ```python

        import pandas as pd

        df = pd.DataFrame(
            {'id': [1, 2, 3],
             'name': ['Alice', 'Bob', 'Charlie'],
             'age': [24, 34, 45]
            }
        )
        ```
        '''
    )

with tab_2:
    st.write(
        '''
        ```r

        df <- data.frame(
            id = c(1, 2, 3),
            name = c('Alice', 'Bob', 'Charlie'),
            age = c(24, 34, 45)
        )
        ```
        '''
    )

tab_3.write(
    '''
    ```julia

    using DataFrames

    df = DataFrame(
        id = [1, 2, 3],
        name = ["Alice", "Bob", "Charlie"],
        age = [24, 34, 45]
    )
    ```
    '''
)


'### :orange[확장 레이아웃: st.expander()]'

with st.expander('🔍 확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 콘텐츠를 숨기거나 보여줄 때 사용됩니다.')
