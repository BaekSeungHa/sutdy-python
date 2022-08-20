#수 입력받기
number = int(input("수를 입력하세요: "))

#입력받은 수에 2를 나눈 나머지가 1이면 홀수!
if number%2 == 1:
    print(number, "홀수 입니다.")
else:
    print(number, "짝수 입니다.")