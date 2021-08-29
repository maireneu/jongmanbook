import util
import karatsuba_mutiply


def fan_0(m, f):
    r = 0
    for i in range(0, len(f) - len(m) + 1):
        b = True
        for j in range(len(m)):
            if m[j] == "M" and f[j + i] == "M":
                b = False
                break
        if b:
            r += 1
    return r


def fan_1(m, f):
    m_list = []
    f_list = []
    for i in range(0, len(m)):
        m_list.append(0 if m[i] == 'F' else 1)
    for i in range(0, len(f)):
        f_list.append(0 if f[len(f)-i-1] == 'F' else 1)
    c = karatsuba_mutiply.karatsuba_multiply2(m_list, f_list)
    all_hugs = 0
    for i in range(len(m)-1, len(f)):
        if c[i] == 0:
            all_hugs += 1
    return all_hugs


def executor():
    input_list = util.readInput("fan_meeting.txt")
    for i in range(1, 1 + (int(input_list[0][0]) * 2), 2):
        members = input_list[i][0]
        fans = input_list[i + 1][0]
        print(members)
        print(fans)
        print(fan_0(members, fans))
        print(fan_1(members, fans))


if __name__ == '__main__':
    executor()
