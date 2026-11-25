
import streamlit as st
import random

# ==========================================
# 1. 프로그램 기본 설정
# ==========================================

st.set_page_config(
    page_title="군사 무기류 위험도 분석 및 안전 가이드",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ 군사 무기류 위험도 분석 및 위급상황 대처 가이드")

st.write(
    "군사 무기류와 관련된 사고의 위험성을 알아보고 "
    "위급상황 발생 시 안전하게 대처하기 위한 예방 가이드입니다."
)

st.warning(
    "본 프로그램의 점수는 교육용 참고 수치이며, "
    "실제 사고 발생 확률이나 전문적인 위험 평가를 의미하지 않습니다."
)


# ==========================================
# 2. 데이터 구조 (딕셔너리 및 리스트)
# ==========================================

weapon_data = {
    "총기류": {
        "risk": 9,
        "description": "인명 피해 가능성이 매우 높은 위험 유형입니다.",
        "scenarios": [
            {
                "name": "정체불명의 총기 발견",
                "risk": 5,
                "advice": "총기에 접근하거나 만지지 말고 안전한 장소로 이동한 뒤 112에 신고합니다."
            },
            {
                "name": "총기 관련 위협 상황",
                "risk": 5,
                "advice": "위험 지역에서 벗어나 안전한 장소를 확보하고 112에 신고합니다."
            },
            {
                "name": "총기 관련 사고 목격",
                "risk": 4,
                "advice": "사고 현장에 접근하지 말고 안전거리를 유지하며 경찰의 안내를 따릅니다."
            },
            {
                "name": "공공장소에서 총기 의심 물체 발견",
                "risk": 5,
                "advice": "물체를 확인하거나 만지지 말고 주변 사람에게 접근하지 않도록 알린 뒤 신고합니다."
            },
            {
                "name": "총기 사고로 인한 부상자 발생",
                "risk": 5,
                "advice": "안전이 확보된 장소에서 119에 신고하고 구조대의 안내를 따릅니다."
            }
        ]
    },

    "폭발물류": {
        "risk": 10,
        "description": "폭발 및 파편으로 심각한 인명 피해가 발생할 수 있는 위험 유형입니다.",
        "scenarios": [
            {
                "name": "의심스러운 폭발물 발견",
                "risk": 5,
                "advice": "물체에 접근하거나 만지지 말고 주변 사람을 대피시킨 뒤 112에 신고합니다."
            },
            {
                "name": "폭발 사고 발생",
                "risk": 5,
                "advice": "폭발 지점과 잔해에서 멀어지고 안전한 장소에서 119에 신고합니다."
            },
            {
                "name": "폭발물 의심 신고 접수",
                "risk": 5,
                "advice": "현장에 접근하지 말고 관계 기관의 대피 안내와 통제에 따릅니다."
            },
            {
                "name": "공공시설에서 의심 물체 발견",
                "risk": 5,
                "advice": "물체를 이동시키지 말고 시설 관계자와 경찰에 알립니다."
            },
            {
                "name": "폭발 사고 이후 추가 위험 우려",
                "risk": 5,
                "advice": "현장으로 돌아가지 말고 구조기관이 안전을 확인할 때까지 대피합니다."
            }
        ]
    },

    "유해가스류": {
        "risk": 9,
        "description": "흡입 및 신체 접촉으로 심각한 건강 피해가 발생할 수 있는 위험 유형입니다.",
        "scenarios": [
            {
                "name": "정체불명의 가스 누출",
                "risk": 5,
                "advice": "가스가 의심되는 장소에서 벗어나 신선한 공기가 있는 안전한 장소로 이동합니다."
            },
            {
                "name": "유해가스 노출 의심",
                "risk": 5,
                "advice": "즉시 노출 장소를 벗어나고 119에 신고합니다. 직접 구조를 시도하지 않습니다."
            },
            {
                "name": "밀폐 공간 내 가스 사고",
                "risk": 5,
                "advice": "밀폐 공간에 다시 들어가지 말고 외부의 안전한 장소에서 구조기관의 도움을 요청합니다."
            },
            {
                "name": "건물 내부에서 정체불명의 냄새 발생",
                "risk": 4,
                "advice": "해당 장소에서 벗어나고 시설 관리자와 관계 기관에 알립니다."
            },
            {
                "name": "가스 누출로 인한 대피 안내",
                "risk": 5,
                "advice": "안내에 따라 안전한 장소로 이동하고 관계 기관의 지시를 따릅니다."
            }
        ]
    },

    "방사성 물질": {
        "risk": 10,
        "description": "방사선 노출이나 오염으로 건강 피해가 발생할 수 있는 위험 유형입니다.",
        "scenarios": [
            {
                "name": "방사성 물질 의심 물체 발견",
                "risk": 5,
                "advice": "물체에 접근하거나 만지지 말고 현장에서 벗어나 관계 기관에 신고합니다."
            },
            {
                "name": "방사선 경보 발생",
                "risk": 5,
                "advice": "공식적인 대피 또는 실내 대기 지침을 따릅니다."
            },
            {
                "name": "방사성 오염 의심 상황",
                "risk": 5,
                "advice": "의심 물질에 접촉하지 말고 관계 기관에 신고하여 안내를 받습니다."
            },
            {
                "name": "방사성 물질 관련 사고 발생",
                "risk": 5,
                "advice": "사고 현장에 접근하지 말고 안전한 장소에서 119에 신고합니다."
            },
            {
                "name": "방사선 관련 시설의 사고 안내",
                "risk": 4,
                "advice": "공식 안내를 확인하고 지정된 대피 및 안전 지침을 따릅니다."
            }
        ]
    },

    "화학물질": {
        "risk": 9,
        "description": "유해 화학물질의 누출이나 접촉으로 피해가 발생할 수 있는 위험 유형입니다.",
        "scenarios": [
            {
                "name": "정체불명의 화학물질 유출",
                "risk": 5,
                "advice": "유출 장소에 접근하지 말고 안전한 곳으로 대피한 뒤 119에 신고합니다."
            },
            {
                "name": "화학물질 접촉 의심",
                "risk": 5,
                "advice": "오염된 장소에서 벗어나고 119의 안내에 따라 응급조치를 받습니다."
            },
            {
                "name": "화학물질 보관 시설 사고",
                "risk": 4,
                "advice": "시설 주변에 접근하지 말고 관계 기관의 대피 안내를 따릅니다."
            },
            {
                "name": "화학물질 유출로 인한 대피 안내",
                "risk": 5,
                "advice": "공식적인 대피 경로와 관계 기관의 안내를 따릅니다."
            },
            {
                "name": "화학물질 사고로 인한 부상자 발생",
                "risk": 5,
                "advice": "오염된 장소에 직접 들어가지 말고 안전한 곳에서 119에 신고합니다."
            }
        ]
    },

    "생물학적 위험": {
        "risk": 9,
        "description": "병원체나 생물학적 오염으로 건강 피해가 발생할 수 있는 위험 유형입니다.",
        "scenarios": [
            {
                "name": "정체불명의 생물학적 물질 발견",
                "risk": 5,
                "advice": "물질을 만지거나 옮기지 말고 안전한 장소에서 관계 기관에 신고합니다."
            },
            {
                "name": "감염병 집단 발생 의심",
                "risk": 4,
                "advice": "보건당국의 안내를 확인하고 개인위생 수칙과 예방 지침을 따릅니다."
            },
            {
                "name": "생물학적 오염 의심 시설 발견",
                "risk": 5,
                "advice": "시설에 들어가지 말고 접근을 피한 뒤 관계 기관에 신고합니다."
            },
            {
                "name": "생물학적 위험 관련 경보 발생",
                "risk": 5,
                "advice": "공식적인 안내를 확인하고 보건당국의 안전 지침을 따릅니다."
            },
            {
                "name": "생물학적 오염 관련 사고 목격",
                "risk": 5,
                "advice": "사고 현장에 접근하지 말고 안전한 장소에서 관계 기관의 도움을 요청합니다."
            }
        ]
    }
}


# ==========================================
# 3. 위험도 분석 함수
# ==========================================

def analyze_risk(weapon):

    risk = weapon_data[weapon]["risk"]

    if risk >= 9:
        level = "매우 높음"
        message = "매우 높은 위험 수준입니다. 각별한 주의가 필요합니다."

    elif risk >= 7:
        level = "높음"
        message = "높은 위험 수준입니다. 안전거리를 유지해야 합니다."

    elif risk >= 4:
        level = "보통"
        message = "주의가 필요한 위험 수준입니다."

    else:
        level = "낮음"
        message = "상대적으로 낮은 위험 수준입니다."

    return risk, level, message


# ==========================================
# 4. 시뮬레이션 출력 함수
# ==========================================

def show_simulation(weapon):

    scenarios = weapon_data[weapon]["scenarios"]

    st.subheader("🚨 대표 위급상황 및 대처요령")

    st.write(
        weapon + "에 관한 대표적인 사고 상황과 "
        "일반인을 위한 안전 대처요령입니다."
    )

    # 이전 상황과 다른 무작위 상황 선택
    previous_scenario = st.session_state.get("current_scenario")

    available_scenarios = [
        scenario for scenario in scenarios
        if previous_scenario is None
        or scenario["name"] != previous_scenario["name"]
    ]

    selected_scenario = random.choice(available_scenarios)

    st.session_state["current_scenario"] = selected_scenario

    # 사고 상황 표 생성
    simulation_list = []

    simulation_list.append({
        "사고 유형": selected_scenario["name"],
        "위험도": str(selected_scenario["risk"]) + "점",
        "대처요령": selected_scenario["advice"]
    })

    st.table(simulation_list)

    # 위험도 결과 확인
    st.subheader("📊 상황별 위험도 분석")

    risk = selected_scenario["risk"]

    st.write(
        "선택된 시뮬레이션 : " +
        str(risk) + "점 / 5점"
    )

    if risk >= 5:
        st.error("고위험 상황 - 즉각적인 안전 확보 및 신고가 필요합니다.")

    elif risk >= 3:
        st.warning("주의 상황 - 안전거리 확보 및 관계 기관 신고가 필요합니다.")

    else:
        st.info("상황을 주의 깊게 확인하고 안전을 확보해야 합니다.")


# ==========================================
# 5. 무기류 선택 화면
# ==========================================

st.divider()

st.subheader("1. 분석할 무기류 선택")

weapon_list = list(weapon_data.keys())

selected_weapon = st.selectbox(
    "무기류 종류를 선택하세요.",
    weapon_list
)


# ==========================================
# 6. 위험도 분석 버튼
# ==========================================

if st.button("🔍 위험도 분석", use_container_width=True):

    st.session_state["selected_weapon"] = selected_weapon
    st.session_state["analysis_done"] = True
    st.session_state["simulation_done"] = False
    st.session_state["current_scenario"] = None


# ==========================================
# 7. 위험도 분석 결과 출력
# ==========================================

if st.session_state.get("analysis_done", False):

    weapon = st.session_state["selected_weapon"]

    risk, level, message = analyze_risk(weapon)

    st.divider()

    st.subheader("2. 위험도 분석 결과")

    st.write(
        "다음 위험요소에 대한 위험도 분석 결과입니다."
    )

    # 위험도 표
    result_table = [{
        "위험요소": weapon,
        "위험도": str(risk) + "점",
        "위험 수준": level
    }]

    st.table(result_table)

    st.write(weapon_data[weapon]["description"])

    # 위험도 강조
    if risk >= 9:
        st.error("🚨 고위험 경고 : " + str(risk) + "점 / 10점")

    elif risk >= 7:
        st.warning("⚠️ 위험 경고 : " + str(risk) + "점 / 10점")

    else:
        st.info("위험도 : " + str(risk) + "점 / 10점")

    st.write(message)

    # ======================================
    # 8. 위급상황 시뮬레이션 버튼
    # ======================================

    st.divider()

    if st.button("🚨 위급상황 시뮬레이션", use_container_width=True):

        st.session_state["simulation_done"] = True

    if st.session_state.get("simulation_done", False):

        show_simulation(weapon)


# ==========================================
# 9. 하단 안내
# ==========================================

st.divider()

st.caption(
    "본 프로그램은 안전교육 및 사고 예방을 위한 교육용 가이드입니다."
)

st.caption(
    "실제 긴급상황에서는 112(경찰) 또는 119(소방·구급)에 신고하고 "
    "현장 관계자의 안내를 따르세요."
)
