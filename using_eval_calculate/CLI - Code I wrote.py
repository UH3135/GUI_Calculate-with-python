a = input()
opartor = [
    "+",
    "-",
    "*",
    "/",
    "="
]  # 연산자 리스트
string_list = []  # 나눈 문자열을 담을 리스트
lop = 0  # 문자열 나누는 것을 도와주는 변수

"""입력 받은 값을 나누는 기능"""
if a[-1] not in opartor:
    a = a + "="
    print(a)
for s in a:
    if s in opartor:  # 연산자를 기준으로 문자열을 나눔
        temp = ''.join(map(str, a[lop:a.index(s)]))  # 연산자 이전의 값을 문자열로 함수에 저장
        string_list.append(temp)
        string_list.append(s)
        lop = a.index(s) + 1
del string_list[-1]

print(string_list)