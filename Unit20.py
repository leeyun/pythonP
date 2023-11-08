"""
    Unit 20 [FizzBuzz]
    1. 1 ~ 100까지 출력
    2. 3의 배수는 Fizz
    3. 5의 배수는 Buzz
    4. 3 5의 배수는 FizzBuzz
"""
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(f"{num}")
