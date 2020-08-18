user_input = input()  # 유저 입력
operator = [
    "+",
    "-",
    "*",
    "/",
    "="
]  # 연산자
string_list = []
lop = 0

if user_input[-1] not in operator:
    user_input += "="
for i, s in enumerate(user_input):
    if s in operator:
        if user_input[lop:i].strip != "":
            string_list.append(user_input[lop:i])
            string_list.append(s)
            lop = i + 1
string_list = string_list[:-1]

while len(string_list) != 1:
    temp = string_list[0] + string_list[1] + string_list[2]
    del string_list[0:3]
    string_list.insert(0, str(eval(temp)))
result = float(string_list[0])
print("result: {}".format(result))
