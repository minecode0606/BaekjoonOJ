# 함수 내부,외부에서 정의한 변수와 겍체의 식별 번호를 출력하기

n = 1
def put_id():
    x = 1
    print(f"id(x) = {id(x)}")
    
print(f"id(i) = {id(1)}")
print(f"id(n) = {id(n)}")
put_id()
