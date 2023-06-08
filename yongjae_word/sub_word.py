symptom_scores = {
    '소실된 의식': 12,
    "심부전": 12,
    '뇌경색 증상': 11,
    '사지 마비': 11,
    '의식 변화': 10,
    '기억 상실': 10,
    "발작": 10,
    '혼란 상태': 9,
    '가슴 통증': 6,
    '청각 손실': 12,
    '시야 손실': 9,
    '감각 소실': 9,
    "경련": 7,
    "저림": 6,
    '손발 차가움': 6,
    '심한 두통': 5,
    '기운 없음': 3,
    "오심": 3,
    "구토": 3,
    "호흡곤란": 8,
    "호흡음": 8,
    '흉부 압박감': 6,
    "코막힘": 4,
    "기침": 3,
    "저체온증": 8,
    '혈압 저하': 8,
    '사지 부종': 7,
    '혈압 상승': 5,
    "빈혈": 6,
    "황달": 5,
    '목의 부종': 4,
    '혈액 흘림': 9,
    "혈뇨": 6,
    '점막 출혈': 5,
    "근육통": 5,
    "화상": 5,
    "코피": 4,
    "고열": 4,
    '음식 섭취 곤란': 6,
    '알레르기 반응': 4,
    '가려운 발진': 4,
    '체중 감소': 3,
}

def get_severity_level(score):
    if score > 80:
        return "level 1"
    elif score > 60:
        return "level 2"
    elif score > 40:
        return "level 3"
    elif score > 20:
        return "level 4 "
    else:
        return "level 5"