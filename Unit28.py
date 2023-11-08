"""
    Unit 28 [회문 판별과 N-gram 만들기]
    1. 회문 판별하기
    1) 반복문 사용
    2) 시퀀스 뒤집기 사용
    3) 리스트와 reversed 사용
    4) join 메서드와 reversed 사용

        # 반복문 사용
        word = input('[반복문 사용] 단어 입력 >>')
        isPalindrome = True
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - i - 1 ]:
                isPalindrome = False
                break
        print(isPalindrome)

        # 시퀀스 뒤집기 사용
        word = input('[시퀀스 뒤집기 사용] 단어 입력 >>')
        print(word == word[::-1])

        # 리스트와 reversed 사용
        word = input('[리스트와 reversed 사용] 단어 입력 >>')
        print(list(word) == list(reversed(word)))

        # 문자열의 join 메서드와 reversed 사용
        word = input('[문자열의 join 메서드와 reversed 사용] 단어 입력 >>')
        print(word == ''.join(reversed(word)))


    2. N-gram 만들기
    문자열에서 N개의 연속된 요소를 추출하는 방법
    1) 반복문 사용
    2) zip 사용
    3) zip과 리스트 표현식 사용

        # 반복문 사용
        text = 'hello'`
        for i in range(len(text) - 1):
            pritn(text[i], text[i + 1], sep = '')

        text = 'this is python script'
        words = text.split()
        for i in range(len(words) - 1):
            print(words[i], words[i + 1])

        # zip 사용
        text = 'hello'
        two_gram = zip(text, text[1:])  #하나가 밀린 상태로 튜플
        for i in two_gram:
            print(i[0], i[1], sep = '')

        # zip과 리스트 표현식 사용
        text = 'hello'
        list(zip(*[text[i:] for i in range(3)]))`
"""
# 연습문제: 단어 단위 N-gram 만들기
n = int(input())
text = input()
words = text.split()

if n > len(words):
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)

# 심사문제: 파일에서 회문인 단어 출력하기
with open('words.txt', 'r') as words:
    word = words.readlines()
    for w in word:
        w = w.strip('\n')
        if list(w) == list(reversed(w)):
            print(w)