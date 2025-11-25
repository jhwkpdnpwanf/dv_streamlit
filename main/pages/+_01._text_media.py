import streamlit as st
from pathlib import Path

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

st.markdown("<div class='big-title'>01. Streamlit 기능 실습: Text media</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>데이터시각화 강의록을 따라가며 작성해보았습니다. <div>", unsafe_allow_html=True)

st.markdown("---")










'# 일반 텍스트'
st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.markdown('# 마크다운 : st.markdown()')
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

'# st.write()'
st.write('# 마크다운 H1 : st.write()')
st.write('## 마크다운 H2 : st.write()')
st.write('빈 줄 추가')

'색상이 있는 텍스트'
st.write(':red[빨간색 텍스트]')
st.write(':blue[파란색 텍스트]')

'### 코드 블록: st.code()'
st.code('print("Hello, World!")', language='python', line_numbers=True)

'### 코드+결과: st.echo()'
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'Chunghun Ha'
    st.write("Hello, Streamlit!", name)

'### Latex 수식 작성: st.latex()'
st.latex(r'\int_a^b f(x)dx')

st.divider()  # 👉 구분선


'# Streamlit Magic'

'''
### 마크다운 헤더3
- 마크다운 목록1. **굵게** 표시
- 마크다운 목록2. *기울임* 표시
    - 마크다운 목록2-1
    - 마크다운 목록2-2

### 마크다운 링크
- [네이버](https://naver.com)
- [구글](https://google.com)

### 마크다운 인용
> 인용문: "Streamlit은 데이터 앱을 쉽게 만들 수 있는 프레임워크입니다."

### 마크다운 표
| 헤더1 | 헤더2 |
|-------|-------|
| 데이터1 | 데이터2 |

### 마크다운 코드 블록
``` python
def hello_world():
    print("Hello, World!")
```
'''

file_path = Path(__file__).resolve().parents[2] / "data" / "image" / "bangwool.jpg"
audio_path = Path(__file__).resolve().parents[2] / "data" / "audio" / "1358494969496731829.mp4"
audio_path2 = Path(__file__).resolve().parents[2] / "data" / "audio" / "1358491467890430094.mp4"


'# • 미디어 삽입'
st.image(file_path, caption='깃 방울', use_container_width=True)

'# • 오디오: st.audio() - 동희 목소리'
st.audio(audio_path, format='audio/mpeg', loop=True)

'# • 오디오: st.audio() - 동희 목소리2'
st.audio(audio_path2, format='audio/mpeg', loop=True)

# '# • 동영상: st.video()'
# st.video('./data/stars.mp4', format='video/mp4', loop=True)
# st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # YouTube 링크

'# • 콜아웃'
'# :orange[정보: st.info()]'
st.info('This is a purely informational message', icon='ℹ️')

'# :orange[경고: st.warning()]'
st.warning('This is a warning message', icon='⚠️')

'# :orange[에러: st.error()]'
st.error('This is an error message', icon='⭕')

'# :orange[성공: st.success()]'
st.success('This is a success message', icon='✅')
