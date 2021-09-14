base_1 = int(input())
n = input()
base_2 = int(input())


def to_base_10(s: str, b1: int = 1, res: int = 0) -> int:
    if s == '':
        return res
    mediate: str = s[len(s)-1]

    if '0' <= mediate <= '9':
        res += int(mediate) * b1
    else:
        res += (ord(mediate)-55) * b1

    return to_base_10(s[:-1], b1*base_1, res)


def from_base_10(num: int, res: str = '') -> str:
    if num == 0:
        return res[::-1]
    mediate: int = num % base_2
    if 0 <= mediate <= 9:
        res += str(mediate)
    else:
        res += chr(mediate + 55)
    return from_base_10(num // base_2, res)


def main(s) -> None:
    num: int = to_base_10(s)
    result: str = from_base_10(num)
    print(result)


main(n)
