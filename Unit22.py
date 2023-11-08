"""
    Unit 22 [List and tuple]
    1. [ List ]
        변경, 수정, 삭제 가능

    1-1 리스트에 요소 추가
    + 갹채.append(요소)
        요소 하나 추가
    + 객체1.extend(객체2)
        리스트를 연결하여 확장
    + insert(인덱스, 요소)
        특정 인덱스에 요소 추가

    1.2 리스트에 요소 삭제
    + 객체.pop(인덱스)
        마지막 요소 또는 특정 인덱스의 요소 삭제
    + 객체.remove(값)
        특정 값을 찾아서 삭제
    + del 객체[인덱스]
        pop과 비슷하여 특정 인덱스의 요소 삭제

    1.3 리스트 요소의 인덱스 구하기
    + 객체.index(값)
        가장 맨 처음 찾은 값의 인덱스

    1.4 리스트 특정 값의 개수
    + 객체.count(값)
        특정값의 갯수를 구함

    1.5 리스트 순서 뒤집기
    + 객체.reverse()
        리스트의 순서를 뒤집음

    1.6 리스트 정렬
    + 객체.sort()
        오름차순 정렬
    + 객체 sort(reverse = True)
        내림차순 정렬
    + sorted(객체)
        정렬된 새 리스트 생성

    1.7 리스트 전체 요소 삭제
    + 객체.clear()
        리스트 모든 요소 삭제
    + del 객체[:]
        ''

    1.8 리스트 할당과 복사
    + 객체2 = 갹채1.copy()
        객체2 = 객체1는 메모리 할당
        객체2 = 갹채1.copy()는 요소 복사 메모리공유 X

    1.9 리스트와 for반복문
    + for 변수 in 리스트:
        반복할 코드
        (요소 하나씩 꺼내서 반복)
    + for 인덱스, 요소 in enumerate(리스트):
        반복할 코드
        (인덱스, 요소 둘다 하나씩 꺼내서 반복)

    1.10 리스트 요소 합계
    + sum(객체)
        객체 요소 전체 합계

    1.11 List Comprehension
    + 변수 = [변수 for 변수 in range(...)]
    + 변수 = list(변수 for 변수 in range(...))
    + 변수 = [변수 for 변수 in range(...) if ~]
    + 변수 = list(변수 for 변수 in range(...) if ~)

    1.12 리스트, 튜플 map
    + 변수 = list(map(함수, 리스트))
        리스트객체 요소를 지정된 함수 형태로 변환
    + 변수 = tuple(map(함수, 튜플))
        튜플객체 요소를 지정된 함수 형태로 변환

    1.13 map과 input().split()
    + 변수 = map(함수, input().split())
        a. input.split()으로 문자열 리스트 받기
        b. 변수에 지정된 함수형으로 변환
        c. map 객체는 이터레이터이므로 언패킹 가능 -> 여러개 저장 가능(기본적으로 list)

    2. [ Tuple ]
        수정 변경 삭제 불가(불변성)

    2.1 튜플 특정 요소 인덱스 구하기
    + 객체.index(값)
        요소의 인덱스 반환

    2.2 특정 요소 갯수 구하기
    + 객체.count(값)
        특정 요소의 갯수를 구함

    2.3 Tuple Comprehension
    + 변수 = tuple(변수 for 변수 in range(...))
    + 변수 = tuple(변수 for 변수 in range(...) if ~)

    2.4 tuple과 map
    + 변수 = tuple(map(int, 객체))

    2,5 튜플 최댓값, 최솟값, 합계
    + min(객체)
        최솟값
    + max(객체)
        최댓값
    + sum(객체)
        합계
"""
# 연습 문제: 리스트에서 특정 요소만 뽑기
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

# 심사 문제: 2의 거듭제곱 리스트 생성
a, b = map(int, input().split())
a = [2**i for i in range(a, b+1)]
print(a)