'''def how_many_person(person_list):
    cnt = int(len(person_list) / 5)
    return cnt


person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4
n_person = how_many_person(person_list)
print(str(n_person) + '명의 정보가 담겨 있습니다.')
'''


def compute_average_age(person_list):
    age = 0
    cnt = len(person_list)
    for i in range(4):
        age = age + person_list[i][1]
        avr_age = age / cnt
    return avr_age
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1, person2, person3, person4
average_age = compute_average_age(person_list)
print('평균 나이는 ', str(average_age), '세입니다.')






