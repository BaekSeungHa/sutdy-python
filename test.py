def how_many_person(person_list):
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

