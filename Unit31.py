"""
    Unit 31 [재귀 함수]
"""
 # 연습문제: 재귀호출로 회문 판뱔하기
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
print(is_palindrome('hello'))
print(is_palindrome('level'))

# 심사문제: 재귀호출로 피보나치 수 구하기
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2) 
n = int(input())
print(fib(n))