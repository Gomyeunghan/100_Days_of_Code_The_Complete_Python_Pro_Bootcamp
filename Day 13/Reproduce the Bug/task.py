from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_images 의 index 는 0~5 이다.
dice_num = randint(0, 5)
# randint 는 1~6까지 이다 index값을 초과 할수 있다
print(dice_images[dice_num])
