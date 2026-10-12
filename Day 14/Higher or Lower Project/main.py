import art
import game_data
import random
# game_data 에 랜덤값의 인덱스로 두명을 뽑는다.
# 두명의 팔로워가 누가 더 많은지 를 비교한다.
# 맞췄다면 유저의 score를 올린다.
# 맞췄다면 게입을 재게한다.
# Compare A : {name}, a {description} , from {country}.
# Against B : {name}, a {description} , from {country}.
compare = {}
against = {}
compare_target = {}
against_target = {}
game_over = False

score = 0

def compare_data(target , against):
    if target['follower_count'] > against['follower_count']:
        return 1
    else:
        return 0


while game_over == False:
    compare = random.choice(game_data.data)
    against = random.choice(game_data.data)
    if compare == against:
         against = random.choice(game_data.data)


    print(art.logo)
    if score > 0:
        print(f"You're right! Current score : {score}")
    print(f'Compare A : {compare['name']}, a {compare['description']} , from {compare["country"]}.')
    print(art.vs)
    print(f'Compare A : {against['name']}, a {against['description']} , from {against["country"]}.')
    choice = input(str("Who has more followers? Type 'A' or 'B' : "))
    if(choice == 'A'):
        compare_target = compare
        against_target = against
    else :
        compare_target = against
        against_target = compare
    if compare_data(compare_target, against_target) == 1:
        score += 1
        print("\n" * 100)
    else :
        game_over = True
        print("\n" * 100)
print(f"Sorry, that's wrong. Final score : {score}")