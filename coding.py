import math
from conv_to_bin import float_to_bin_fixed


def calc_sigma(q, p):
    return round(q + p/2, 5)


def hilbert_moore(p):
    q = [0]
    sigma = [calc_sigma(q[0], p[0])]
    str_res = []
    str_res.append(f"z1 | p1 = {p[0]} | q1 = 0 | σ1 = {sigma[0]} | ")

    for i in range(1, len(p)):
        q.append(round(q[i - 1] + p[i - 1], 5))
        sigma.append(calc_sigma(q[i], p[i]))
        str_res.append(f"z{i + 1} | p{i + 1} = {p[i]} | q{i + 1} = {q[i]} | σ{i + 1} = {sigma[i]} | ")

    for i in range(len(p)):
        sigma[i] = float_to_bin_fixed(sigma[i])

    codes = []
    l = []

    for i in range(len(p)):
        tmp = get_code_len(p[i], i + 1)
        str_res[i] += tmp[0]
        l.append(tmp[1])
        str_res[i] += f"σ{i + 1} = {sigma[i][:20]} | "
        codes.append(sigma[i][2:l[i] + 2])
        str_res[i] += f"Код = {codes[i]} |\n"

    result = ""
    for i in range(len(str_res)):
        result += str_res[i]

    return result, l


def get_code_len(p, i):
    l = round(-math.log2(p), 5)
    str = f"-log_2({p}) = {l} | l{i} = ⌈{l}⌉ + 1 = "
    l = math.ceil(l) + 1
    str += f"{l} | "
    return str, l

