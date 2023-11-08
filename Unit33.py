"""
    Unit 33 [클로저 사용]

    1. 함수 안에서 전역 변수 변경
    - global 전역변수
        x = 10
        def func():
            global x -> 전역변수임을 선언
            x = 20 -> 바뀜
        전역변수가 없을 경우 해당 변수는 전역 변수가 됨

    2. namespace
    파이썬은 변수를 namespace에 저장한다. locals() 함수를 사용하면
    현재 스페이스의 딕셔너리 형태로 출력 함수 안에서 사용하면 그 함수안에 변수들 출력
    
    3. 상위 함수 변수를 하위 함수에 변경
    - nonlocal 상위지역변수
        def A():
            x = 10
            def B():
                nonlocal x
                x = 20
        nonlocal은 현재 바로 상위 함수를 nonlocal로 인식한다.
    
    4. global과 nonlocal의 차이
    global은 전역 변수를 nonlocal은 현재 바로 상위 함수로 나아가 변수를 인식

    5. 클로저 사용하기
    클로저란 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때
    다시 꺼내서 사용하는 함수를 뜻함
    클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용, 또한 클로저에 속한 지역변수는
    바깥에서 직접 접근할 수 없으므로 데이털르 숨기고 싶을 때 사용
        def calc():
            a = 3
            b = 3
            def mul_add(x):
                return a*x + b
            return mul_add
        c = calc() -> c안에 속한 함수를 클로저 a, b는 유지되며 숨김 가능 
        print(c(1), c(2), c(3))

    6. lambda 클로저
        def calc():
            a = 3
            b = 5
            return lambda x: a*x + b
        c = calc()
        print(c(1), c(2), c(3))
    
    7. 클로저의 지역 변수 변경하기
        def calc():
            a = 3
            b = 5
            total = 0
            def mul_add(x):
                nonlocal total
                total = total + a * x + b
                print(total)
            return mul_add
        c = calc()
        c(1) -> 8
        c(2) -> 19
        c(3) -> 33
"""
# 연습문제: 호출 횟수를 세는 함수 만들기
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
c = counter()
for i in range(10):
    print(c(), end = ' ')

# 심사문제: 카운트다운 함수 만들기
def countdown(n):
    cnt = n + 1
    def count():
        nonlocal cnt
        cnt -= 1
        return cnt
    return count

n = int(input())
c = countdown(n)
for i in range(n):
    print(c(), end = ' ')