import coding
import characteristics


def write_probs(arr):
    str = ""
    for i in range(len(arr)):
        str += f"z{i+1} = {arr[i]}\n"
    str += "\n"
    return str


def input_array():
    n = 10

    probabilities = []

    for i in range(n):
        probabilities.append(float(input(f"Введите вероятность символа z{i + 1}: ")))

    print("Вероятности символов: ", probabilities)

    return probabilities


if __name__ == '__main__':
    probabilities = input_array()

    #probabilities = [0.223, 0.16, 0.115, 0.23, 0.07, 0.017, 0.031, 0.06, 0.014, 0.08]

    result = write_probs(probabilities)
    result += "q_i = q_i-1 + p_i-1\nσ_i = q_i + p_i/2\nl_i=⌈log2(p_i)⌉ + 1\n\n"

    str, l = coding.hilbert_moore(probabilities)
    result += str + "-----------------------------------\n"

    str, H = characteristics.binary_entropy(probabilities)
    result += str

    str, L = characteristics.code_length(l, probabilities)
    result += str

    result += characteristics.redundancy(H, L)

    with open("result.txt", "w", encoding='utf-8') as file:
         file.write(result)
