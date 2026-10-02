import random
import art

# 1. computer가 1~100까지의 랜덤 수를 저장한다[x]
# 2. easy일경우 10번의 기회 hard일 경우 5번의 기회 가 필요하다.[x]
# 3. 숫자를 입력하면 랜덤으로 저장된 숫자와 비교한다.
# 4. 랜덤으로 저장된 숫자가 사용자가 입력한 숫자보다 높으면 Too high를 프린트한다.
# 5. 랜덤으로 저장된 숫자가 사용자가 입력한 숫자보다 낮으면 Too low를 프린트한다.
# 6. 틀리면 기회가 한번씩 사라진다.
# 7. 기회 안에 맞출경우 You got it! answer was {random_number}. 를 출력한다.
# 8. art를 프린트한다.


def compare(r_number , u_number ):
    if r_number > u_number:
        print("Too low")
        return False
    elif r_number < u_number :
        print("Too high")
        return False
    elif r_number == u_number :
        print(f"You got it! The answer was {r_number}.")
        return True





def play_game():
    random_number = random.randint(0 , 100)
    user_number = 0
    life = 0
    print(art.logo)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")
    if difficulty == "easy":
        life = 10
    else:
        life = 5
    while user_number != random_number :
        if life < 1:
            print("You have run out of guesses. Refresh the page to run again")
            return
        user_number = int(input("Make a guess : "))
        if(not compare(random_number , user_number)):
            print("Guess Again")
            life -= 1
            print(f"You have {life} attempts remaining to guess the number")
        else:
            return







play_game()