def input_elenemt():
    outls = []
    for _ in range(10):
        inputelemint = int(input(""))
        outls.append(inputelemint)
    return outls

def compare_and_devices(input_ls : list):
    remainder_ls = []
    for i in input_ls:
        remainder_ls.append(i % 42)
    return len(set(remainder_ls))

if __name__ == '__main__':
    inputls = input_elenemt()
    print(compare_and_devices(inputls))