import sys

def card_conv(x : int, r : int) -> str:
    """
    정숫값 x를 r진수로 변환한뒤 그 수를 나타내는 문자열을 반환
    :param x:
    :param r:
    :return d:
    """
    d = ""
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$'
    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        inputint = int(sys.stdin.readline())
        count = 2
        while count <= 64:
            newst = str(card_conv(inputint, count))
            newreversest = "".join(reversed(str(newst)))
            if newst == newreversest:
                print("1")
                break
            count += 1
        else:
            print("0")