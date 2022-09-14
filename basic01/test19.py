'''
* 파이썬 다중 상속 주의점 *
- 파이썬은 클래스 / 메서드 탐색 순서는 MRO를 따른다.
- 다중 상속시, 부모 클래스를 나열할 때, 우선 순위는 왼쪽 > 오른쪽 순서로 높다.
- 동일 메서드가 둘 이상의 부모에 존재하면 왼쪽 클래스의 메서드가 실행된다.
- 클래스명.mro() 을 통해 순서 확인 가능
'''
class A:
    pass

# print(A.mro())

class B(A):
    pass

# print(B.mro())

class C(A):
    pass

# print(C.mro())

class D(B, C):
    pass

# print(D.mro())
# D > B > C > A > object

class E(C, B):
    pass

# print(E.mro())

# (D, E) 각자 자식 클래스들 우선 순위가 충돌남
class F(D, E):
    pass

print(F.mro())