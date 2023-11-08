"""
    Unit25 [딕셔너리 응용]

    1. 딕셔너리 요소 추가
    + 딕셔너리객체.setdefault(키, 값)
        키=값 쌍을 추가
        키만 입력할 경우 값은 None이 됨
    + 딕셔너리객체.update(키 = 값, ...)
        키의 값 수정, 키가 없으면 키-값 쌍 추가
        키가 문자열일 때만 사용 가능
        여러개를 추가, 수정 가능
        1) 리스트와 튜플 활용
        - 딕셔너리객체.update([[키1, 값1], [키2, 값2]])
        - 딕셔너리객체.update(((키1, 값1), (키2, 값2)))
        2) update는 반복가능객체이므로 zip 사용 가능
        - 딕셔너리객체.update(zip([키1, 값1], [키2, 값2]))
    
    2. 딕셔너리 요소 삭제
    + 딕셔너리객체.pop(키, 기본값)
        키가 있을 경우 값을 반환하고 없으면 기본값을 반환
    + del 딕셔너리객체[키]

    3. 딕셔너리객체.popitem()
        3.6버전이상: 마지막 요소를 튜플로 반환
        3.7버전이상: 임의의 요소를 튜플로 반환

    4. 딕셔너리 모든 요소 삭제
    + 딕셔너리 객체.clear()
        모든 요소 삭제

    5. 딕셔너리 값 가져오기
    + 딕셔너리.get(키, 기본값)
        키의 값을 반환 없으면 기본값 반환
    
    6. 딕셔너리 모든 요소 가져오기
    + 딕셔너리객체.items()
        키-값 쌍 모두 가져옴
    + 딕셔너리객체.keys()
        키를 모두 가져옴
    + 딕셔너리객체.values()
        값을 모두 가져옴
    
    7. 리스트와 튜플로 딕셔너리 만들기
    + 딕셔너리변수 = dict.fromkeys(키리스트, 기본값)
        딕셔너리를 생성하며 기본값을 지정안했을 경우 None 했을 경우 모두 기본값으로 저장
    + defaultdict
        defaultdict를 설정하면 없는 키값을 호출했을 때 에러X
    '
        from collections import defaultdict
        딕셔너리객체 = defaultdict(기본값생성함수) ex) int
        딕셔너리객체[없는 키] -> 기본값으로 0반환
    '

    8. 반복문과 딕셔너리
    + for key value in 딕셔너리.items():
        반복할 코드
    + for key in 딕셔너리.keys():
        반복할 코드
    + for value in 딕셔너리.values():
        반복할 코드
    
    9. 딕셔너리 표현식
    + {키: 값 for 키, 값 in 딕셔너리}
    + dict({키: 값 for 키, 값 in 딕셔너리})
    '
        keys = ['a', 'b', 'c', 'd']
        x = {key: value for key, value in dict.fromkeys(keys).items()}

    '

    10. 딕셔너리 표현식과 조건문
    [딕셔너리는 for문으로 반복하여 키-값 쌍을 지울 수 없다 -> 크기가 바뀌기 때문]
    + {키:값 for 키, 값 in 딕셔너리 if 조건식}
    + dict({키:값 for zl, 값 in 딕셔너리 in 조건식})

    11. 중첩 딕셔너리
    + 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}
        계층형 데이터에 유용
        호출하기 위해서는 딕셔너리[키1][키A]로 해야한다.
    
    12. 딕셔너리 할당과 복사
    리스트와 마찬가지로 딕셔너리.copy()로 해야 별개의 딕셔너리가 된다

    13. 중첩 딕셔너리 할당과 복사
    중첩 리스트와 마찬가지로 딕셔너리.copy()해도 값은 공유하므로 deepcopy메소드를 써야함
    '
        import copy
        딕셔너리2 = copy.deepcopy(딕셔너리1)
    '
"""

# 연습문제: 평균 점수 구하기
maria = {'korean': 94, 'english': 91, 'matheamtics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)

# 심사문제: 딕셔너리에서 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))
x = {key: value for key, value in x.items() if key != 'delta' and value != 30}
print(x)
