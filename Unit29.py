"""
    Unit 29 [함수]
    1. 함수 독스트링 사용
        def func():
            '''
            독스트링    
            '''
        print(add.__doc__)
    
    2. 함수 여러개의 반환값
    여러 개를 반환할 경우 튜플로 반환되며 언패킹한다.

    3. 호출 스택 과정
    전역 프레임 -> 호출한 함수 스택 쌓임(밑에서부터 위에서 사라짐)
"""
# 연습문제: 몫과 나머지를 구하는 함수 만들기
x = 10
y = 3
def get_quotient_remainder(x, y):
    return x // y,  x % y
quotient, remainder = get_quotient_remainder(x, y)
print("몫: {0}, 나머지: {1}".format(quotient, remainder))

# 심사문제: 사칙 연산 함수 만들기
x, y = map(int, input().split())
def calc(x, y):
    return x + y, x - y, x * y, x / y
a, s, m, d = calc(x, y)
print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a, s, m, d))