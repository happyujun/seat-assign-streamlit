import random
import streamlit as st
import pandas as pd
import time

def assign_seats(students):
    random.shuffle(students)
    seat_structure = [4, 5, 6, 6, 6, 6]
    seat_map = [[] for _ in range(6)]
    index = 0

    for col in range(6):
        rows = seat_structure[col]
        for row in range(rows):
            if index < len(students):
                seat_map[col].append(students[index])
                index += 1
            else:
                seat_map[col].append('')
    return seat_map

def get_table_data(seat_map):
    max_rows = max(len(col) for col in seat_map)
    table_data = []

    for row in range(max_rows-1, -1, -1):  # 아래쪽이 교탁이므로 거꾸로 출력
        row_data = []
        for col in range(6):
            if row < len(seat_map[col]):
                row_data.append(seat_map[col][row])
            else:
                row_data.append('')
        table_data.append(row_data[:2] + [''] + row_data[2:4] + [''] + row_data[4:6])

    # 마지막 줄에 '교탁' 표시
    table_data.append(['']*3 + ['🪑 교탁 🪑'] + ['']*3)
    return table_data

# Streamlit 앱 설정
st.set_page_config(page_title="자리 배치", layout="centered")

# 상단 헤더와 버튼을 나란히 배치
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🎓 9학년 2반 자리배치 랜덤배치")
with col2:
    start = st.button("자리 랜덤 배치하기 🎲")

students = [
    "강주하", "강지완", "고수아", "김무경", "김산", "김영재", "김지헌", "나재겸", "나호정", "노영서",
    "노하윤", "민지현", "박준기", "백영민", "서원", "손지안", "신희철", "안지유", "오서은", "오은유",
    "이승규", "이승민", "이연아", "이은율", "이준범", "이지영", "임가온", "장유석", "정민서", "정수빈",
    "최민기", "편윤아", "한려원"
]

placeholder = st.empty()

# 버튼이 클릭되면 자리 섞기 + 애니메이션
if start:
    for _ in range(15):  # 약 5초간 반복
        seat_map = assign_seats(students.copy())
        table_data = get_table_data(seat_map)
        df = pd.DataFrame(table_data, columns=["1열", "2열", "", "3열", "4열", "", "5열", "6열"])
        placeholder.dataframe(df, use_container_width=True)
        time.sleep(0.3)
    st.success("✅ 자리 배치 완료되었습니다! 다시 뽑고 싶으면 위 버튼을 누르세요.")
