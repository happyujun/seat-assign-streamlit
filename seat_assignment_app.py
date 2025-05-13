import random
import streamlit as st
import pandas as pd
import time

# 전체 학생 명단 (34명)
students = [
    "강주하", "강지완", "고수아", "김무경", "김산", "김영재", "김지헌", "나재겸", "나호정", "노영서",
    "노하윤", "민지현", "박준기", "백영민", "서원", "손지안", "신희철", "안지유", "오서은", "오은유",
    "이승규", "이승민", "이연아", "이은율", "이준범", "이지영", "임가온", "장유석", "정민서", "정수빈",
    "최민기", "편윤아", "한려원", "홍예진"
]

seat_structure = [5, 5, 6, 6, 6, 6]
seat_labels = ["1열", "2열", "3열", "4열", "5열", "6열"]

def assign_seats_fixed(students, structure):
    fixed_name = "홍예진"
    remaining_students = [s for s in students if s != fixed_name]
    random.shuffle(remaining_students)

    seat_map = []
    idx = 0

    for col_idx, count in enumerate(structure):
        col = []
        for row_idx in range(count):
            if col_idx == 0 and row_idx == 4:  # 1열 5행 고정
                col.append(fixed_name)
            else:
                col.append(remaining_students[idx] if idx < len(remaining_students) else "")
                idx += 1
        seat_map.append(col)
    return seat_map

def format_for_display(seat_map):
    max_rows = max(len(col) for col in seat_map)
    table = []
    for row in range(max_rows-1, -1, -1):
        row_data = []
        for col in seat_map:
            row_data.append(col[row] if row < len(col) else "")
        table.append(row_data)
    return table

# Streamlit UI
st.set_page_config(page_title="9학년 2반 자리배치", layout="centered")
st.title("🎓 9학년 2반 자리배치")

# 클릭할 때마다 자리 애니메이션 표시
if st.button("자리 랜덤 배치하기 🎲"):
    placeholder = st.empty()

    # 🔁 3초간 자리 계속 섞이도록 애니메이션
    for _ in range(15):  # 약 3초간 (0.2초 x 15)
        temp_map = assign_seats_fixed(students.copy(), seat_structure)
        temp_table = format_for_display(temp_map)
        temp_df = pd.DataFrame(temp_table, columns=seat_labels)

        styled_temp_df = temp_df.style.set_properties(**{
            'text-align': 'center'
        }).hide(axis="index")

        placeholder.dataframe(styled_temp_df, use_container_width=True)
        time.sleep(0.05)

    # ✅ 최종 자리 확정
    final_map = assign_seats_fixed(students.copy(), seat_structure)
    final_table = format_for_display(final_map)
    final_df = pd.DataFrame(final_table, columns=seat_labels)

    styled_final_df = final_df.style.set_properties(**{
        'text-align': 'center'
    }).hide(axis="index")

    placeholder.dataframe(styled_final_df, use_container_width=True)

    st.markdown(
        "<div style='text-align:center; font-size:24px; margin-top:20px;'>🪑 <strong>교탁</strong> 🪑</div>",
        unsafe_allow_html=True
    )
