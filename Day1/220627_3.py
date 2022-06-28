import random
import time

# =============================================================================
# 시작말
# =============================================================================
print('0~9사이의 숫자를 맞추는 게임입니다.')
time.sleep(1)
print('숫자와 위치까지 맞출 경우 스트라이크로 1점')
time.sleep(1)
print('숫자만 맞출 경우 볼로 0.5점')
time.sleep(1)
print('게임을 시작합니다.')

range_2 = [0, 9] # 0~9 사이의 숫자를 뽑습니다.

def get_player():
    test_list = []
    while True:
        a = int(input("숫자를 입력하시오. (단, 0~9사이의 숫자를 입력하셔야 합니다.) : "))
        if a not in test_list:
            test_list.append(a)
        if len(test_list) == 3:
            break
    return test_list

def get_com():
    a_set = set([])
    
    while len(a_set) < 3:
        n = random.randint(range_2[0], range_2[1])
        a_set.add(n)
    return list(a_set)

# =============================================================================
# s, b의 개수를 계산해서 return
# =============================================================================
def get_sb(a, b):
    s = 0
    bb = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            s += 1
    for i in a:
        for ii in b:
            if i == ii:
                bb += 1
    return s, bb-s

def game():
    a = get_player()
    b = get_com()
    print(a)
    print(b)
    
    return get_sb(a, b)

def game_check(a, b):
    score = 0
    result = 'Loss'
    score += a * 1
    score += b * 0.5
    
    if score == 3:
        result = 'Win'
    return score, result

te4 = game()
score = game_check(te4[0], te4[1])
print("스트라이크 : {0}, 볼 : {1}".format(te4[0], te4[1]))
print("당신의 점수는 : {0}".format(score[0]))
print("당신의 승부는 : {0}".format(score[1]))