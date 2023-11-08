"""
    Unit 30 [함수의 위치 인수와 키워드 인수]
    1. 위치 인수
    : 함수에 인수를 순서대로 넣는 방식

    2. 언패킹 사용
    + 함수(*리스트)
    + 함수(*튜플)
        인수를 순서대로 넣을 때 리스트나 튜플을 사용하며 *를 붙여 함수에 넣어준다
        * 는 언패킹 한다는 의미, 단 매개변수의 갯수와 요소 갯수가 같아야 한다.
    
    3. 가변 인수 함수
    + def 함수이름(*args):
        코드
        args는 튜플타입이다. 직접 여러개 넣어도 되고 리스트(튜플) 언패킹 사용 가능
        
        고정 인수와 가변 인수를 함께 사용할 경우 고정 인수가 먼저 온다.
        + def 함수이름(변수1, *args):
            코드
            순서대로 첫번째 인수가 변수1에 들어온다
            매개변수, *args, **kwargs 순으로 들어가야 한다.
    
    4. 키워드 인수
    + 힘수(키워드 = 값)
        호출 시 함수 변수에 들어갈 값을 지정하면 순서 상관없이 선언 가능
    
    5. 키워드 인수와 딕셔너리 언패킹 사용
    + 함수(**딕셔너리)
        *은 키 **은 값을 언패킹하며 함수 인자와 키 갯수와 이름이 같아야 한다.
    
    6. 키워드 인수를 사용한 가변 인수 함수
    + def 함수이름(**kwargs):
        for kw, args in kwargs.items():
            코드
    호출 시 함수(**딕셔너리) 또는 키워드인수를 사용

    7. 초깃값이 지정된 매개변수
    + def 함수이름(변수1, 변수2, 변수 = 초깃값)
        무조건 초깃값이 있는 매개변수가 뒤로 와야함    
"""
# 연습문제: 가장 높은 점수를 구하는 함수 만들기
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args):
    return max(*args)
max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수: ', max_score)

max_score = get_max_score(english, science)
print('높은 점수: ', max_score)

# 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
korean, english, mathematics, science = map(int, input().split())
def get_min_max_score(*args):
    return min(*args), max(*args)
def get_average(**args):
    return sum([i for i in args.values()]) / len([i for i in args.values()])
min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean = korean, english = english, mathematics = mathematics, science = science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
