data = [
("환자가 호흡곤란, 혼돈, 심한 객혈 발생, 급성 폐부종 진행 중.", 1),
("발작성 호흡곤란과 약열, 흉통이 있는 상태에서 급성 객혈이 보고되어 숨을 제대로 쉬지 못함.", 1),
("환자의 호흡이 매우 어려워지고, 스스로 균형을 잡지 못하는 상태로 심각한 객혈이 동반됨.", 1),
("지속적인 심한 객혈과 호흡곤란으로 인해 환자의 혈액 흐름이 크게 저하되어 응급 치료가 필요함.", 1),
("환자가 강한 통증을 호소하고 있으며, 환자의 의식이 흐려지는 상태에서 급성 객혈 발생.", 1),
("응급실에 도착한 환자는 호흡곤란과 채색이 매우 어두운 상태에서 급성 객혈을 호소.", 1),
("호흡 패턴이 불규칙하고 빠르게 변하며 심각한 객혈이 발생하여 환자의 생명이 위협받음.", 1),
("혈액 산소 포화도가 매우 낮은 상태에서 급성 객혈이 발행.", 1),
("지속적인 심한 객혈과 급격한 호흡곤란으로 인해 환자의 혈압이 급격히 하락.", 1),
("호흡 곤란으로 인한 위험한 증상으로 호흡 중단이 걸림돌이 되는 경우가 있으며 급성 객혈이 발생함.", 1),
("산소 포화도가 낮고 기침과 객혈이 동반한 급성 준비가 필요한 환자 상태.", 2),
("흉통이 수반되는 기침과 객혈을 호소하며 급성 호흡기 증상 진단이 고려되어짐.", 2),
("호흡 곤란이 있고 호흡 중 객혈이 나오며 환자의 상태가 영 좋지 않음.", 2),
("흉통과 함께 급격한 호흡 곤란 및 객혈이 발생하여 신속한 처치가 필요함.", 2),
("호흡 곤란으로 잠깐의 의식 잃음이 일어날 정도로 악화되며 객혈 증상이 함께 나타남.", 2),
("환자가 호흡에 큰 불편을 느끼고 흉통과 함께 객혈이 나타납니다.", 2),
("기침과 객혈을 동반한 흉통이 발생하며, 호흡기 관련 증상으로 병원을 찾게 됨.", 2),
("객혈이 끊임없이 발생하고 있으며, 이와 함께 호흡 곤란과 흉통이 있습니다.", 2),
("급성 천식 증상으로 호흡이 어렵고, 기침과 객혈이 같이 나타남.", 2),
("가슴에 불편함을 호소하며, 기침과 함께 객혈이 나오고 있음.", 2),
("기침과 객혈이 끊임없이 일어나지만, 흉통과 호흡곤란은 약간만 느껴짐.", 3),
("간헐적으로 아프다는 호흡기 증상을 호소하며, 객혈 발생이 일어남.", 3),
("환자가 기침과 함께 객혈 증상을 가지지만, 그 외에는 아프다는 증언이 없습니다.", 3),
("가벼운 호흡 곤란을 호소하며 객혈이 보입니다. 흉통은 가끔 발생.", 3),
("기침과 함께 객혈 증상이 나타났지만, 흉통과 호흡곤란은 경미한 정도.", 3),
("간헐적으로 기침과 객혈이 발생하는 상태로 호흡기 관련 동반 증상은 없습니다.", 3),
("맑은 콧물과 함께 감염된 기침과 객혈이 나타난 상태.", 3),
("호흡 곤란이 있으나 도움 별록 없이도 보호 시인상 일어남.", 3),
("기침, 객혈이 발생하며 흉통은 한동안 통제할 부탁없이 꾸준한 상태.", 3),
("기침과 객혈이 있는 상태로, 흉통은 급격하지 않지만 가끔 증상이 악화되는 경우.", 3),
("기침을 동반한 객혈이 있지만, 일상적인 활동에 큰 지장이 없는 환자 상태입니다.", 4),
("간헐적으로 기침과 객혈이 나타나고 가벼운 흉통이 있습니다. 통증은 일시적.", 4),
("부종과 객혈이 보이며 기침이 있다지만 호흡곤란은 없습니다.", 4),
("가벼운 기침과 객혈이 발생하며 통증 및 호흡곤란은 없는 상태입니다.", 4),
("환자가 기침과 객혈을 동반한 경미한 흉통이 있는 시일로 호흡호로 인해 악화되지 않습니다.", 4),
("가벼운 기침과 객혈이 동반되며 호흡곤란이 발생하지 않는 상태입니다.", 4),
("기침과 객혈 증상이 경미하거나 중간 정도로 발생하며 호흡곤란은 느끼지 않습니다.", 4),
("보통의 기침과 함께 경미한 객혈이 나타납니다. 환자의 호흡곤란은 없습니다.", 4),
("간헐적인 객혈이 나타내는 데 기침과 함께 신 소견이 없는 환자입니다.", 4),
("가벼운 기침과 객혈 증상과 함께 경미한 흉통이 시간이 지남에 따라 점점 나아짐.", 4),
("큰 문제는 아니지만, 일상생활에 곤란함을 겪고 있는 환자들에게 치료 안내를 권장합니다.", 5),
("거의 없는 객혈과 기침이나 경미한 흉통은 호흡곤란을 유발하지 않습니다.", 5),
("일주일에 한 번 객혈이 나오며, 어느 정도 쉬는 후 호전됩니다.", 5),
("기침과 함께 객혈이 나오지만, 극히 드물며 응급실 치료가 필요하지 않은 상태입니다.", 5),
("환자의 기침과 함께 객혈이 나와도 호흡곤란 습관이나 통증이 발생하지 않습니다.", 5),
("연료 같아 시한 조금의 기침과 객혈이 있으나 경미합니다.", 5),
("가벼운 기침과 객혈이 동반되어 증상 발생 외에 다른 호흡기 지장이 없는 상태입니다.", 5),
("기침과 객혈이 발생하나 비응급적 성 겪고 있느니 호흡곤란 경험이 없습니다.", 5),
("떨어지는 기분 없이 기침과 함께 객혈이 나오며 처리됩니다.", 5),
("간헐적으로 발생하는 기침과 객혈이 있지만 큰 문제가 되지 않은 상태입니다.", 5),
("기침으로 인해 가래가 많이 나오고, 숨을 쉴 때 흉부가 아프고 가슴이 답답합니다.", 4),
("기침이 심하여 밤에 잠을 제대로 못 자고, 피로와 가슴 통증이 계속해서 나타납니다.", 4),
("호흡이 어려워 말을 할 때마다 기침이 심해지고, 가슴에서 찡거림과 인후통이 느껴집니다.", 4),
("기침으로 인해 피로와 숨쉬기 곤란을 동반하며, 가래가 노랗게 나와 체력이 감소합니다.", 4),
("기침이 심해져 숨을 쉬기 어려워져 피로와 가슴 통증이 동반되며, 일상 생활에 지장을 겪습니다.", 4),
("기침으로 인해 호흡이 어려워지고 피로를 동반하며, 천명 소리와 가래가 토할 수 있습니다.", 4),
("기침으로 인해 가래가 초록색으로 변하고, 숨을 쉴 때 가슴이 답답하고 흉통이 심합니다.", 4),
("기침이 지속되어 숨을 쉴 때마다 호흡 소리가 나고, 가래가 노랗게 나옵니다.", 3),
("기침으로 인해 가래가 많이 나오며, 피로와 가슴의 찡거림이 심하게 나타납니다.", 3),
("기침이 심하여 피로와 인후통을 동반하며, 음식을 삼키기 어렵고 가래가 노랗게 나옵니다.", 3),
("마른 기침으로 인해 피로와 두통을 동반하며, 호흡 소리가 들리고 가래가 갈색으로 변합니다.", 3),
("기침으로 인해 호흡이 어려워져 가슴이 답답하며, 가래가 토할 수 있고 피로를 느낍니다.", 3),
("기침이 심하여 가래가 노랗게 변하고, 숨을 쉴 때 가슴에서 통증이 느껴집니다.", 3),
("기침으로 인해 피로와 인후통이 심해지며, 가래가 노랗고 끈적끈적합니다.", 3),
("기침으로 인해 가래가 노랗고 피로를 동반하며, 숨을 쉴 때 가슴이 답답한 상태입니다.", 3),
("기침이 심하여 피로와 어지러움을 동반하며, 호흡 소리와 가래가 나타납니다.", 3),
("기침으로 인해 가래가 많이 나오고, 숨을 쉴 때 흉부가 아프며 답답합니다.", 3),
("기침으로 인해 피로가 심해져 일상 생활에 지장을 겪고 있으며, 호흡 소리가 들립니다.", 3),
("기침이 심하여 밤에 잠을 제대로 못 자고, 피로와 가슴 통증이 계속해서 나타납니다.", 3),
("호흡이 어려워 말을 할 때마다 기침이 심해지고, 가슴에서 찡거림과 인후통이 느껴집니다.", 3),
("기침으로 인해 피로와 숨쉬기 곤란을 동반하며, 가래가 노랗게 나와 체력이 감소합니다.", 3),
("기침이 심해져 숨을 쉬기 어려워져 피로와 가슴 통증이 동반되며, 일상 생활에 지장을 겪습니다.", 3),
("기침으로 인해 호흡이 어려워지고 피로를 동반하며, 천명 소리와 가래가 토할 수 있습니다.", 3),
("기침으로 인해 가래가 초록색으로 변하고, 숨을 쉴 때 가슴이 답답하고 흉통이 심합니다.", 3),
("기침으로 인해 피로와 가슴 통증이 있으며, 가래가 투명에서 노란색으로 변합니다.", 2),
("기침이 심하여 숨을 쉴 때 가슴에서 가벼운 찡거림과 두통을 느낄 수 있습니다.", 2),
("기침으로 인해 피로를 동반하며, 가래가 투명하고 얇게 나오는 상태입니다.", 2),
("기침이 계속되어 가래가 투명하고 체력이 약간 감소한 상태입니다.", 2),
("기침으로 인해 가래가 흰색이며, 가슴에서 가벼운 답답함이 느껴집니다.", 2),
("기침이 심해져 숨을 쉬기 어려워지며, 호흡 소리가 가끔 나타납니다.", 2),
("기침으로 인해 가래가 투명하게 나오고, 일상 생활에는 큰 지장이 없습니다.", 2),
("기침이 지속되어 피로를 동반하며, 가래가 투명하고 얇게 나옵니다.", 2),
("기침으로 인해 가래가 투명하게 나와 체력에 약간 영향을 미칩니다.", 2),
("기침이 심하여 숨을 쉬기 어려워져 피로를 느끼고, 가래가 투명하게 나옵니다.", 2),
("기침으로 인해 피로와 가슴 통증이 나타나며, 가래가 투명에서 흰색으로 변합니다.", 2),
("기침이 심해져 가래가 투명하게 나오고, 가슴이 가끔 찡그린다는 느낌이 있습니다.", 2),
("기침으로 인해 가래가 흰색이며, 숨을 쉴 때 가슴이 가벼운 찡거림이 느껴집니다.", 2),
("기침이 계속되어 피로와 가끔씩 가슴 통증이 나타나며, 가래가 투명하게 나옵니다.", 2),
("기침으로 인해 가래가 투명하게 나와 체력에 약간 영향을 줍니다.", 2),
("기침이 심하여 숨을 쉬기 어려워져 피로를 느끼며, 가래가 투명하게 나옵니다.", 2),
("기침으로 인해 가래가 투명하게 나와 체력에 약간 영향을 미칩니다.", 2),
("기침이 심해져 피로를 동반하며, 가래가 투명하게 나오고 얇게 퍼집니다.", 2),
("기침으로 인해 가래가 투명하고 얇게 나오며, 가끔 가슴 통증이 있습니다.", 2),
("기침이 계속되어 피로를 동반하며, 가래가 투명하게 나옵니다.", 2),
("기침으로 인해 가래가 흰색이며, 가슴에서 가벼운 찡거림이 느껴집니다.", 2),
("기침이 심해져 숨을 쉬기 어려워져 피로를 느끼고, 가래가 투명하게 나옵니다.", 2),
("기침으로 인해 피로와 가슴 통증이 나타나며, 가래가 투명에서 흰색으로 변합니다.", 2),
("기침이 심해져 가래가 투명하게 나오고, 가슴이 가끔 찡그린다는 느낌이 있습니다.", 2),
("기침으로 인해 가래가 흰색이며, 숨을 쉴 때 가슴이 가벼운 찡거림이 느껴집니다.", 2),
("기침이 계속되어 피로와 가끔씩 가슴 통증이 나타나며, 가래가 투명하게 나옵니다.", 2),
("흉부 불편감이 느껴지면서 입술이 청색이 되고 가슴 통증이 동반되고 있습니다.", 3),
("신경과민 상태에서 흉부 불편감과 가래가 발생하며, 호흡 시 휘파람 소리가 납니다.", 3),
("기침과 가래가 모여 호흡곤란이 발생하고, 그로 인해 긴장감과 불안감이 높아졌습니다.", 2),
("가슴 통증과 함께 입술 청색증이 발생하며, 가래와 기침이 지속적으로 나타납니다.", 2),
("호흡곤란과 흉부 불편감이 발생하여 호흡 시 휘파람 소리가 나며 손톱이 청색이 됩니다.", 3),
("기침과 가래가 누적되어 호흡기 문제로 인해 급한 신경과민이 발생하고 있습니다.", 2),
("가슴 통증을 동반한 기침과 가래 때문에 호흡 시 휘파람 소리와 흉부 불편감을 겪고 있습니다.", 2),
("호흡곤란과 흉부 불편감이 있는 상태에서 신경과민과 긴장감이 동반되어 손톱이 청색을 띠고 있습니다.", 2),
("입술, 손톱, 피부의 청색증에 가래와 기침이 모여 흉부 불편감과 맥박이 빨라집니다.", 4),
("신경과민 상태에서 입술, 손톱의 청색증이 발생하며, 기침과 가래가 지속적으로 발생합니다.", 2),
("가슴 통증에 흉부 불편감이 추가되어 있고, 호흡 시 휘파람 소리와 호흡곤란이 동반되고 있습니다.", 3),
("흉부 불편감이 느껴지면서 입술이 청색이 되고 가슴 통증이 동반되고 있습니다.", 3),
("신경과민 상태에서 흉부 불편감과 가래가 발생하며, 호흡 시 휘파람 소리가 납니다.", 3),
("기침과 가래가 모여 호흡곤란이 발생하고, 그로 인해 긴장감과 불안감이 높아졌습니다.", 4),
("가슴 통증과 함께 입술 청색증이 발생하며, 가래와 기침이 지속적으로 나타납니다.", 4),
("호흡곤란과 흉부 불편감이 발생하여 호흡 시 휘파람 소리가 나며 손톱이 청색이 됩니다.", 3),
("기침과 가래가 누적되어 호흡기 문제로 인해 급한 신경과민이 발생하고 있습니다.", 4),
("가슴 통증을 동반한 기침과 가래 때문에 호흡 시 휘파람 소리와 흉부 불편감을 겪고 있습니다.", 4),
("호흡곤란과 흉부 불편감이 있는 상태에서 신경과민과 긴장감이 동반되어 손톱이 청색을 띠고 있습니다.", 4),
("입술, 손톱, 피부의 청색증에 가래와 기침이 모여 흉부 불편감과 맥박이 빨라집니다.", 2),
("신경과민 상태에서 입술, 손톱의 청색증이 발생하며, 기침과 가래가 지속적으로 발생합니다.", 4),
("가슴 통증에 흉부 불편감이 추가되어 있고, 호흡 시 휘파람 소리와 호흡곤란이 동반되고 있습니다.", 3),
("흉부 불편감과 호흡곤란으로 인한 신경과민에 가래와 기침이 빈번하게 발생하고 있습니다.", 4),
("호흡 시 휘파람 소리가 나고, 기침과 가래로 인해 흉통이 발생하며 신경과민이 높아집니다.", 4),
("입술과 손톱의 청색증이 동반된 상태에서 호흡곤란과 가래가 지속적으로 발생하고 있습니다.", 2),
("가슴 통증에 입술 청색증이 동반되어 호흡 시 휘파람 소리가 나고 가래와 기침이 발생합니다.", 3),
("흉통과 호흡곤란이 동반된 상태에서 입술, 손톱의 청색증이 발생하며 가래와 기침이 지속됩니다.", 2),
("호흡곤란과 흉부 불편감으로 인해 호흡 시 휘파람 소리가 나며 신경과민과 긴장감이 높아집니다.", 3),
("흉부불편감과 함께 가래가 발생하고 호흡 시 휘파람 소리나 기침과 호흡곤란이 발생합니다.", 3),
("신경과민 상태에서 입술 청색증과 함께 가슴 통증과 흉부 불편감이 동반되고 있습니다.", 3),
("호흡 시 휘파람 소리와 함께 기침이 발생하며 가슴 통증과 입술 청색증이 동반되고 있습니다.", 3),
("호흡곤란으로 인해 흉부가 답답하고 기침도 동반됩니다.", 3),
("흉통과 함께 쓰러질 것 같은 느낌이 들며 기침이 지속됩니다.", 3),
("기침이 지속되고, 폐 속에 가래가 많이 쌓여 호흡이 어려워집니다.", 3),
("천식 발작으로 인해 호흡 걱정과 함께, 가슴이 찌르는 것 같은 통증이 있습니다.", 2),
("호흡 곤란으로 인해 기침을 하고 폐에서 가래가 많이 발생합니다.", 3),
("호흡부족으로 인해 숨쉬기가 힘들고 긴장감이 생깁니다.", 3),
("기침 유발과 함께 흉부가 답답한 느낌이 드는 경우가 있습니다.", 3),
("폐렴으로 인해 흉부가 아픈 것 같고 기침과 함께 힘겹습니다.", 2),
("호흡도 참을 수 없게 어려워져 흉부 압박감과 함께 시야가 어두워집니다.", 2),
("천식 발작으로 인해 호흡이 어려워지고, 가슴 아래에서 막힌 기분이 들면서 꼼짝이지 못합니다.", 2),
("흉통과 함께 기침이 매우 심하고, 폐에서 지속적인 적신성 가래가 발생합니다.", 2),
("호흡 곤란으로 인해 기침이 지속적이고 흉통이 생깁니다.", 3),
("흉부가 답답하고 폐에서 가래가 계속 발생하여 한숨도 못 쉴 것 같습니다.", 2),
("천식 발작으로 인해 호흡기 근육이 수축되어 어지럽고, 시야까지 어두워지는 경우도 있습니다.", 2),
("폐렴으로 인해 침과 함께 흉통이 발생하고 숨쉬기 어려워집니다.", 2),
("호흡 곤란으로 인해 공기가 마시기 힘들고 가슴 속이 답답합니다.", 3),
("가래가 발생하며 매우 기침이 심한 경우가 있습니다.", 3),
("천식으로 인해 숨쉬기가 어려워지며 흉부가 답답하고 아프기도 합니다.", 2),
("호흡 부족으로 인해 기침이 계속되고 한숨도 쉴 수 없는 상태입니다.", 3),
("폐기종으로 인해 숨쉬기가 힘들어지면서 흉부도 아파지기 시작합니다.", 2),
("환자는 가슴 답답함과 흉통이 동반되며 두통과 발열이 동시에 나타나 있습니다.", 3),
("환자는 코막힘과 기침이 동반되어 호흡곤란을 느끼며, 가슴 통증도 동반되고 있습니다.", 3),
("환자는 기침과 흉통이 동반되어 호흡 시 쉬익 소리가 나고, 식욕 감퇴와 발열이 있습니다.", 3),
("환자는 체중감소와 피로를 호소하며 호흡곤란과 가슴 답답함이 동시에 발생하고 있다.", 2),
("환자는 두통과 가슴 통증이 함께 있고, 인후통으로 인해 흉통이 발생하고 있는 상태입니다.", 4),
("환자는 천명과 가래가 발생하며 식욕 감퇴를 호소하고, 피로와 인후통이 동반되고 있다.", 3),
("환자는 호흡곤란과 흉통이 발생하며 코막힘으로 인해 인후통이 동반되고 있다.", 3),
("환자는 기침과 가래 때문에 체중 감소를 경험하며, 쉼 없이 나오는 콧물과 인후통이 있다.", 3),
("환자는 가슴 답답함과 발열로 인한 코막힘이 동반되어 호흡 시 쉬익 소리가 있으며 식욕 감퇴가 있다.", 3),
("환자는 체중 감소와 코막힘으로 인해 인후통이 동반되고 있으며, 피로와 호흡 시 쉬익 소리가 동반되고 있다.", 2),
("호흡이 심하게 어려워 숨을 쉬는 것이 거의 불가능합니다.", 1),
("산소 공급이 부족하여 의식이 혼미하고 심한 혼란 상태입니다.", 1),
("가슴 통증과 함께 호흡이 매우 어려워 힘들게 숨을 쉴 수 있습니다.", 1),
("심한 코막힘이 동반되어 호흡이 거의 이루어지지 않습니다.", 1),
("숨을 쉬면서 실신하는 상태로 응급 조치가 필요합니다.", 1),
("호흡이 심하게 빨라져서 정상적인 호흡 패턴이 나타나지 않습니다.", 1),
("산소 부족으로 인해 의식을 잃고 혼수 상태에 빠집니다.", 1),
("호흡이 어려워 숨을 쉬는 것이 거의 불가능하며 응급 수술이 필요합니다.", 1),
("호흡이 매우 어려워 혼란과 혼돈 상태에 놓입니다.", 1),
("호흡이 거의 이루어지지 않아 심장마비와 같은 생명 위협적인 상태입니다.", 1),
("숨가쁨과 가슴이 빡빡한 느낌에, 콧물이 줄줄 흐릅니다.", 3),
("기침과 가래가 동반되며, 코막힘과 재채기가 잦아집니다.", 3),
("호흡 곤란과 흉통이 같이 나타나며, 비대칭 코통증이 있습니다.", 2),
("숨가쁨과 호흡 곤란이 있으며, 기침이 갑자기 심해집니다.", 2),
("기관지 천식 증상으로 호흡곤란과 호흡 참견이 발생합니다.", 3),
("호흡이 어려워지며, 가래와 숨가쁨이 동시에 발생합니다.", 3),
("흉통이 생기며, 비대칭 코통증과 코막힘이 동반됩니다.", 2),
("천식 발작으로 호흡곤란과 기침 증상이 악화되었습니다.", 2),
("숨쉬는 데 불편함이 있으며, 가래와 흉통이 동반됩니다.", 3),
("코막힘과 콧물이 계속 나오며 가래와 숨가쁨이 일어납니다.", 3),
("콧물이 많이 나오며, 기관지 천식 증상으로 인한 호흡곤란이 있습니다.", 3),
("숨쉬기 어려워지며, 재채기가 계속되고 코가 막힙니다.", 3),
("기침과 가래 때문에 호흡 참견이 발생하고 있습니다.", 3),
("기관지 천식 증상으로 인해 호흡 참견과 코 막힘이 발생합니다.", 3),
("재채기와 코막힘이 동반되어 가래와 기침이 발생하고 있습니다.", 3),
("호흡 참견으로 인해 콧물이 나오며 기침이 발생합니다.", 3),
("가래와 기침이 나타나고, 숨가쁨이 동반되며 흉통이 느껴집니다.", 2),
("재채기와 가래가 동반되어 호흡 참견이 일어납니다.", 3),
("기관지 천식 증상으로 인해 호흡곤란이 발생하며 코막힘이 심해집니다.", 3),
("비대칭 코통증과 가래, 기침이 동반되며 호흡 참견이 발생합니다.", 3),
("콧물과 가래가 나오며 호흡 참견과 기침이 동반됩니다.", 3),
("기관지 천식 증상으로 인해 호흡곤란과 흉통이 동반됩니다.", 3),
("숨가쁨과 호흡곤란이 동반되며 코막힘이 심해집니다.", 2),
("호흡곤란과 기침으로 인해 가슴이 빡빡한 느낌이 듭니다.", 3),
("콧물과 가래가 나오며 숨쉬기가 매우 어려워집니다.", 3),
("재채기와 코막힘이 동반되며 호흡곤란이 발생합니다.", 2),
("기침과 가래 때문에 숨쉬기 어렵고 코가 막힙니다.", 2),
("호흡 참견이 발생하며 코막힘과 콧물이 나옵니다.", 2),
("기관지 천식 증상으로 인해 숨가쁨과 흉통이 동반됩니다.", 3),
("호흡곤란이 발생하며 가래와 재채기가 동시에 발생합니다.", 3),
("코막힘이 있어 숨쉬기 어렵고 흉통이 동반됩니다.", 3),
("호흡 참견과 기침이 동반되며 콧물이 나옵니다.", 3),
("숨가쁨과 가래가 나오며 재채기가 계속됩니다.", 3),
("재채기와 기관지 천식 증상이 나타나 모며 호흡곤란이 있습니다.", 4),
("천식 발작으로 호흡 참견이 있는 상태에서 기침이 심해집니다.", 3),
("코막힘이 심해져 숨가쁨이 동반되며 흉통이 느껴집니다.", 3),
("호흡곤란이 발생하며 가래와 진한 콧물이 나옵니다.", 3),
("숨쉬기 어려워지며 가래와 독특한 코통증이 있습니다.", 3),
("호흡 곤란과 재채기가 동반되며 가래가 계속 나옵니다.", 3),
("가래와 콧물이 나오며, 흉통과 숨가쁨이 동반됩니다.", 3),
("재채기와 기침이 동반되어 숨쉬기 어려워지고 있습니다.", 4),
("콧물과 흉통이 동반되어 숨쉬는 데 어려움을 겪고 있습니다.", 3),
("호흡곤란이 발생하며 기관지 천식 증상으로 인해 숨쉬기가 힘들어집니다.", 3),
("숨가쁨과 가래가 동반되어 호흡 참견이 일어납니다.", 3),
("비대칭 코통증과 가슴이 빡빡한 증상이 있다며 호흡 참견이 발생합니다.", 2),
("코막힘과 가래, 기침, 재채기가 동시에 나타나고 있습니다.", 3),
("기관지 천식 증상으로 인해 원인 불명의 코통증과 코막힘이 발생합니다.", 3),
("호흡 참견과 흉통이 동반되며 기관지 천식 증상이 나타납니다.", 3),
("콧물이 나오며 숨가쁨과 기침이 동시에 발생하고 있습니다.", 3),
("호흡곤란과 가래가 동시에 발생하며, 재채기가 계속됩니다.", 3),
("호흡 곤란이 심해져 입김이 매우 약해졌습니다.", 2),
("환자의 코와 입 주변이 부어올라 호흡이 매우 어려워졌습니다.", 2),
("알레르기로 인한 기도 경축으로 인해 호흡이 완전히 막혔습니다.", 1),
("환자가 혼자 숨을 쉴 수 없고, 구조적인 도움이 필요합니다.", 1),
("천식 발작으로 인해 호흡 소리가 거칠어졌고, 호흡이 불규칙해졌습니다.", 2),
("호흡이 불규칙하고 얕아져서 환자의 얼굴이 청발색을 띠고 있습니다.", 2),
("호흡 곤란으로 인해 말을 할 수 없고, 호흡이 시도될 때마다 참견하는 소리가 납니다.", 2),
("코와 입 주변이 부어올라서 호흡이 불가능하게 막혔습니다.", 1),
("호흡이 불규칙하고 쉽게 피로해지며, 빠른 대처가 필요합니다.", 2),
("환자의 숨소리가 거칠어지고, 가슴이 빡빡해지며, 숨을 쉬는 게 어려워졌습니다.", 2),
("의식이 흐려지고 호흡이 얕고 약해졌습니다.", 1),
("알레르기 반응으로 인해 숨을 쉬는 데 힘이 들며, 환자의 얼굴이 창백해졌습니다.", 1),
("환자가 호흡 소리와 함께 쉰 숨을 내뱉으며 몸이 약해졌습니다.", 1),
("환자의 입 주변이 부어올라서 어떤 소리도 내지 못하고 호흡이 어려워졌습니다.", 2),
("호흡이 얕고 불규칙해져서 환자가 혼자 호흡을 제어할 수 없습니다.", 2),
("천식 발작으로 인해 환자의 얼굴이 창백해지고, 코와 입 주변이 부어올라졌습니다.", 2),
("의식이 혼미해지고 호흡이 매우 약해져 신속한 응급 처치가 필요합니다.", 1),
("호흡이 불규칙하고 느려져서 환자가 혼자 호흡을 유지할 수 없습니다.", 1),
("환자가 미열과 함께 호흡이 어려워지고, 피로감과 혼동이 나타났습니다.", 2),
("호흡 소리가 거칠어져 환자의 얼굴이 창백해지고, 호흡이 어려워졌습니다.", 2),
("코막힘이 심해서 숨쉬기 어렵고, 약간의 두통과 코 주변 압통이 있습니다.", 3),
("코가 막혀 숨을 쉬기 어려워서 불편함을 느끼지만 다른 증상은 없습니다.", 4),
("코가 완전히 막혀 숨을 쉬기 매우 어려우며, 비강 분비물과 함께 코 주변 피부가 붓고 가려움이 있습니다.", 2),
("심한 코막힘으로 인해 호흡이 거의 불가능하고, 눈 주변에 부종과 붉은 발적이 동반됩니다.", 1),
("코막힘이 심하여 호흡이 어렵고, 가려움과 함께 비강 분비물이 많이 나옵니다.", 2),
("코가 부종되어 호흡이 제한되고, 눈 주변에 가려움과 피부발진이 나타납니다.", 2),
("코막힘이 심해서 입으로 숨쉬고, 코 주변 부위에 압통과 불편감을 느낍니다.", 3),
("코가 완전히 막혀 숨을 쉬기 어렵고, 비강 분비물이 노란색으로 변하며 두통이 있습니다.", 2),
("코가 막혀 숨을 쉬기 어려우며, 코 주변 피부가 가려워서 당기는 느낌이 있습니다.", 3),
("코막힘이 심해서 호흡이 어렵고, 코 주변 부위에 약한 통증이 있습니다.", 3),
("코막힘이 심해서 호흡이 어렵고, 가려움과 함께 코 주위에 발진이 나타납니다.", 2),
("코가 완전히 막혀 호흡이 거의 불가능하며, 코 주변에 부종과 붉은 발적이 동반됩니다.", 1),
("코막힘이 심하여 호흡이 어렵고, 비강 분비물이 많이 나오며 두통이 동반됩니다.", 2),
("코가 부종되어 호흡이 제한되고, 눈 주변에 가려움과 피부 발진이 나타납니다.", 2),
("코막힘이 심해서 입으로 숨쉬고, 코 주변 부위에 압통과 불편감을 느낍니다.", 3),
("코가 완전히 막혀 숨을 쉬기 어려우며, 비강 분비물이 노란색으로 변하고 두통이 있습니다.", 2),
("코가 막혀 숨을 쉬기 어려우며, 코 주변에 약한 통증이 있습니다.", 3),
("코막힘이 심해서 호흡이 어렵고, 코 주변에 두드러기와 가려움이 나타납니다.", 2),
("코가 완전히 막혀 숨을 쉬기 거의 불가능하며, 비강 분비물이 노란색으로 변하고 두통이 심합니다.", 1),
("코막힘이 심해서 호흡이 어렵고, 코 주변 부위가 붓고 통증을 동반합니다.", 2),
("코가 막혀 숨을 쉬기 어렵고, 코 주위에 가려움과 붓기가 있습니다", 3),
("코막힘이 심해서 호흡이 어렵고, 비강 분비물이 노란색이고 약한 두통이 있습니다.", 2),
("코가 완전히 막혀 숨을 쉬기 거의 불가능하며, 코 주변에 피부발진과 압통이 있습니다.", 1),
("코막힘이 심해서 숨을 쉬기 어렵고, 가려움과 함께 코 주변에 붉은 발진이 나타납니다.", 2),
("코가 완전히 막혀 숨을 쉬기 거의 불가능하며, 코 주위에 붓기와 가려움이 동반됩니다.", 1),
("코막힘이 심해서 호흡이 어렵고, 비강 분비물이 많이 나와 약한 두통이 있습니다.", 2),
("코가 부종되어 호흡이 제한되고, 눈 주변에 가려움과 압통이 동반됩니다.", 2),
("코막힘이 심해서 입으로 숨쉬고, 코 주변 부위에 통증과 불편감을 느낍니다.", 3),
("코가 완전히 막혀 숨을 쉬기 어려우며, 비강 분비물이 노란색으로 변하고 두통이 동반됩니다.", 2),
("코막힘이 심해서 호흡이 어렵고, 코 주변 피부가 가려워서 당기는 느낌이 있습니다.", 3),
("코가 막혀 숨을 쉬기 어려우며, 코 주변에 약한 통증이 있습니다.", 3),
("코막힘이 심해서 호흡이 어렵고, 코 주변에 두드러기와 가려움이 나타납니다.", 2),
("코가 완전히 막혀 숨을 쉬기 거의 불가능하며, 비강 분비물이 노란색으로 변하고 두통이 심합니다.", 1),
("코막힘이 심해서 호흡이 어렵고, 코 주변 부위가 붓고 통증을 동반합니다.", 2),
("코가 막혀 숨을 쉬기 어렵고, 코 주위에 가려움과 붓기가 있습니다.", 3),
("코막힘이 심해서 호흡이 어렵고, 비강 분비물이 노란색이고 약한 두통이 있습니다.", 2),
("코가 완전히 막혀 숨을 쉬기 거의 불가능하며, 코 주변에 피부발진과 압통이 있습니다.", 1),
("코막힘이 심해서 숨을 쉬기 어렵고, 가려움과 함께 코 주변에 붉은 발진이 나타납니다.", 2),
("코가 완전히 막혀 숨을 쉬기 거의 불가능하며, 코 주위에 붓기와 가려움이 동반됩니다.", 1),
]