"""
    Unit26 [set]

    1. 세트 요소 확인
    + 값 in set
        set에 값이 있으면 True 아니면 False
    + 값 not in set
        setdp 값이 있으면 False 아니면 True
    
    2. set메소드로 set만들기
    + set(반복가능한객체) ex) range, 문자열

    3. frozen set
    + 변수 = frozenset(반복가능한객체)
        추가, 삭제 불가능 set 안에 set를 넣을 때 사용
    
    4. set 연산
        1) 합집합(union)
        + set1 | set2
        + set.union(set1, set2)

        2) 교집합(intersection)
        + set1 & set2
        + set.intersection(세트1, 세트2)

        3) 차집합(difference)
        + set1 - set2
        + set.difference(set1, set2)

        4) 대칭차집합(symmetric diffrence)
        + set1 & set2
        + set.symmetric_diffrence(set1, set2)
    5. 집합 연산 후 할당 연산자
        1) 합집합 연산 후 할당
        + set 1 |= set2
        + set1.update(set2)

        2) 교집합 연산 후 할당
        + set1 &= set2
        + set1.intersection_update(set2)

        3) 차집합 연산 후 할당
        + set1 -= set2
        + set1.difference_update(set2)

        4) 대칭차집합 연산 후 할당
        + set1 ^= set2
        + set1.symmetric_diffrence_update(set2)
    
    6. 부분집합과 상위집합
        1) 부분집합
        + set1 <= set2
        + set1.issubset(set2)

        2) 진부분집합
        + set1 < set2
        
        3) 상위집합
        + set1 >= set2
        + set1.issuperset(set2)

        4) 진상위집합
        + set1 > set2

    7. 세트 비교
    + set1 == set2
        같은지 확인
    + set1 != set2
        안 같은지 확인
    + set1.isdisjoint(set2)
        겹치지 않는지 확인
    
    8. 세트 조작
        1) 요소 추가
        + set1.add(값)

        2) 요소 삭제
        + set1.remove(값)
            값이 없으면 에러 발생
        + set1.discard(값)
            값이 없으면 그냥 넘어감
        + set1.pop()
            임의의 요소 삭제
        + set1.clear()
            모든 요소 삭제
        
        3) 요소 갯수 세기
        + len(set1)

    9. 세트의 할당과 복사
    리스트, 튜플과 마찬기지로 할당과 복사가 다르다.

    10. 세트 표현식 사용
    + {식 for 변수 in 반복가능한객체}
    + set(식 for 변수 in 반복가능한 객체)

    11. 세트 표현식과 조건문
    + {식 for 변수 in 세트 if 조건식}
    + set(식 for 변수 in 세트 if 조건식)

"""

# 연습문제: 공배수 구하기
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}
print(a & b)

# 심사문제: 공약수 구하기
num1, num2 = map(int, input().split())
a = {i for i in range(1, num1+1) if num1 % i == 0}
b = {i for i in range(1, num1+1) if num2 % i == 0}
divisor = a & b
result = 0
if type(divisor) == set:
    result = sum(divisor)
print(result)