from sys import exit

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
for s in a:
    if s in opartor:  # 연산자를 기준으로 문자열을 나눔
        temp = ''.join(map(str, a[lop:a.index(s)]))  # 연산자 이전의 값을 문자열로 함수에 저장
        string_list.append(temp)
        string_list.append(s)
        lop = a.index(s) + 1
del string_list[-1]  # 마지막 "=" 제거

"""나눈 문자열을 앞에서부터 천천히 계산하는 기능"""
while len(string_list) > 1:  # 리스트 속 원소가 하나 남을때까지
    math_expr = string_list[0] + string_list[1] + string_list[2]  # 계산할 식
    try:
        result = str(eval(math_expr))  # 입력받은 식 계산
    except ZeroDivisionError:
        print("Can't division as 0")
        exit()
    except TypeError:
        print("Enter a number")
        exit()
    except Exception as e:
        print(e)
        exit()
    string_list = string_list[3:]
    string_list.insert(0, result)

print(result)
