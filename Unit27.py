"""
    Unit 27 [파일 사용]
    1. 파일에 문자열 쓰기
    open 함수로 파일을 열어 파일 객체를 얻은 뒤 write메서드를 사용
        파일객체 = open(파일이름, 파일모드)
        파일객체.write("문자열")
        파일객체.close()

    2. 파일에서 문자열 읽기
    open 함수로 파일을 열어 파일 객체를 얻은 뒤 read메서드 사용
        변수 = 파일객체.read()
    
    3. 자동으로 파일 객체 닫기
    + with open(파일이름, 파일모드) as 파일객체:
        코드
        with as 사용 시 파일 객체를 자동으로 닫아줌
    
    4. 여러줄 파일에 쓰기, 읽기
    1) 리스트에 들어있는 문자열 파일에 쓰기
    + 파일객체.writelines(문자열리스트)
    
    2) 파일의 내용 한줄 씩 리스트로 가져오기
    + 변수 = 파일객체.readlines()

    3) 파일 내용 한줄 씩 읽기
    + 변수 = 파일객체.readlines()
        readline을 사용할 때 while반복문을 사용해야한다.
        with open('text.txt', 'r') as file:
            line = None
            while line != '':
                line = file.readline()
                print(line.strip('\n'))
        line에 None을 넣어줘야 while에 들어가며 ''일 경우 애초에 거짓이므로 실행이 안됨
    
    4) for 반복문으로 파일 내용 줄 단위로 읽기
    for문은 파일에 내용을 줄 단위로 인식한다(파일 객체는 이터레이터 언패킹 가능)
        with open('text.txt', 'r') as file:
            for line in file:
                print(line.strip('\n'))
    
    5. 피클링
    파이썬 객체를 파일에 저장하는 과정을 피클링, 파일에서 객체를 읽어오는 과정을 언피클링이라고 함
    1) 파이썬 객체 파일에 저장하기
    import pickle
    name = 'james'
    age = 17
    address = '서울시 서초구 반포동'
    scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

    with open('james.p', 'wb') as file:
        pickle.dump(name, file)
        pickle.dump(age, file)
        pickle.dump(address, file)
        pickle.dump(scores, file)
    
    
    2) 파일에서 파이썬 객체 읽기
    import pickle
    with open('james.p', 'rb') as file:
        name = pickle.load(file)
        age = pickle.load(file)
        address = pickle.load(file)
        scroes = pickle.load(file)
        print(name)
        print(age)
        print(address)
        print(scores)
"""
# 연습문제: 파일에서 10자 이하인 단어 갯수 세기
with open('text.txt', 'r') as file:
    cnt = 0
    for line in file:
        if len(line.strip('\n')) <= 10:
            cnt += 1
    print(cnt)

# 심사문제: 특정 문자가 들어있는 단어 찾기
with open('text.txt', 'r') as file:
    text = file.readline()
    word = text.split()
    for w in word:
        if 'c' in w:
            print(w.strip(',.'))
     