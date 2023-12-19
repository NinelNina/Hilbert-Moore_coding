import math


def binary_entropy(p):
    n = len(p)
    str_res = 'H = '
    str_num = ''
    H_X = 0
    for i in range(n):
        # str_res += f'p(z{i}) * log(p(z{i}))'
        tmp = round(math.log2(p[i]), 4)
        H_X += round(p[i] * tmp, 4)
        str_num += f'{p[i]:.4f} * ({tmp:.4f})'
        if i < n - 1:
            # str_res += ' + '
            str_num += ' + '
    H_X *= (-1)
    H_X = round(H_X, 4)
    str_res += ' = -(' + str_num + ') = ' + str(H_X) + '\n'
    return str_res, H_X


def code_length(l, p):
    str_res = ""
    str_num = ""
    str_res += "L = "
    L = 0
    for i in range(len(l)):
        str_res += f"{l[i]} * {p[i]}"
        tmp = round(l[i] * p[i], 4)
        str_num += f"{tmp}"
        L += tmp
        if i < len(l) - 1:
            str_res += ' + '
            str_num += ' + '
    str_res += " = " + str_num
    str_res += f" = {L:.4f}\n"
    L = round(L, 4)
    return str_res, L


def redundancy(H, L):
    r = round(L - H, 4)
    str_res = f"r = L - H = {L} - {H} = " + str(r)
    return str_res