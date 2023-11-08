"""
    Unit 32 [람다 표현식]
    1. 람다 표현식 함수
    - lambda 매개변수들: 식
        plus_ten = lambda x: x + 10
        plus_ten(1)
        단 람다 표현식 안에 변수를 쓸 수 없음
            lambda(x: y = 10; x + y)(1)
            syntax error 

    2. 람다 표현식 자체 호출
    - (lambda 매개변수들: 식)(인수들)
        (lambda x: x + 10)(1)
    
    3. 람다 표현식의 인수 사용 (map 활용)
    - map(람다 표현식, 인수들)
        list(map(lambda x: x + 10, [1, 2, 3]))
    
    4. 람다 표현식과 map, filter, reduce 함수 활용
        1) 람다 표현식과 조건부 표현식
        - lambda 매개변수들: 식1 if 조건식 else 식2
            a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            list(map(lambda x: str(x) if x % 3 == 0 else x))
            보통의 조건식과 달리 if는 조건식이 참일 때 else는 조건식이 거짓일 때 사용
            if가 있다면 else는 무조건 있어야 함

        2) map에 객체 여러 개 넣기
            a = [1, 2, 3, 4, 5]
            b = [2, 3, 4, 5, 6]
            c = list(map(lambda x, y: x * y, a, b))

        3) filter 사용
        filter은 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져옴
        함수 또는 람다표현식에서 반환값이 true인 요소만 가져옴
        - filter(함수, 반복가능한객체)
            def f(x):
                return x > 5 and x < 10
            a = [8, 3, 7, 10, 15, 9, 11]
            print(list(filter(f, a)))
            print(list(filter(lambda x: x > 5 and x < 10, a)))

        4) reduce 사용
        reduce는 반복 간으한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
        - from functools import reduce
        - reduce(함수, 반복가능한객체)
            def f(x, y):
                return x + y
            a = [1, 2, 3, 4, 5]
            from functools import reduce
            print(reduce(f, a))

            print(reduce(lambda x, y: x + y, a)) 
"""
# 연습문제: 이미지 파일만 가져오기
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))

# 심사문제: 파일 이름을 한꺼번에 바꾸기
#input 97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx
files = input().split()
print(list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1], files)))