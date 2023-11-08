"""
    Unit 34 [클래스 사용하기]

    1. 클래스와 메서드
        1) 클래스와 메서드 생성
        - class 클래스 이름:
            def 메서드(self):
                코드
        - 인스턴스 = 클래스()
            클래스를 통해 객체(인스턴스) 생성
        
        2) 메서드 호출
        - 인스턴스.메서드()

        3) 빈 클래스 만들기
        - class 클래스 이름:
            pass
        
        4) 메서드 안에 메서드 호출
        - self.메서드()
            class 메서드 이름:
                def 메서드1(self):
                    ...
                def 메서드2(self):
                    self.메서드1()

        5) 특정 클래스의 인스턴스인지 확인
        - isinstance(인스턴스, 클래스)
            class 메서드1:
                pass
            변수 = 메서드1
            isinstance(변수, 메서드1)
        
    2. 속성 사용
        1) __init__
        - class 클래스이름():
            def __init__(self):
                self.속성 = 값
            __init__메서드는 인스턴스를 만들 때 호출되는 특별한 메서드
            앞뒤로 __가 붙은 메서드는 파이썬이 자동으로 호출해주는 스페셜 메서드
        
        2) self의 의미
        self는 인스턴스 자기 자신을 의미
    
        3) 인스턴스 생성 후 값 받기
        - class 클래스이름():
            def __init(self, 매개변수1, 매개변수2):
                self.속성1 = 매개변수1
                self.속성2 = 매개변수2
        
        4) 비공개 속성 사용
        - class 클래스이름:
            def __init__(self, 매개변수):
                self.__속성 = 값
        - class 클래스이름:
            def __메서드이름(self):
                ...
            앞에 __붙이면 비공개 속성
"""
# 연습문제: 게임 캐릭터 클래스 만들기
class knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def slash(self):
        print('베기')

x = knight(health = 542.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()

# 심사문제: 게임 캐릭터 클래스 만들기
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(self):
        deal = self.ability_power * 0.65 + 400
        print(f"티버: 피해량 {deal}")

health, mana, ability_power = map(float, input().split())

x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()