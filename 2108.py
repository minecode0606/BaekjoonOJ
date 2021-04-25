def add_all(ls:list):
    """
    This function adds up all the input list.
    """
    try:
        output = 0
        for i in ls:
            output += int(i)
        return output
    except:
        raise TypeError("Please input the right list")


def insertion_sort(data_list):
    """
    This function is sorting the list
    """
    for stand in range(len(data_list)):
        key = data_list[stand]
        for num in range(stand, 0, -1):
            if key < data_list[num - 1]:
                data_list[num - 1], data_list[num] = data_list[num], data_list[num - 1]
            else:
                break
    return data_list


class Statistics:
    def __init__(self, inputarray:list):
        """
        This function is input the input array
        """
        self.inputarray = inputarray
        self.sort = insertion_sort(self.inputarray)

    def mean(self):
        """
        This function returned the mean.
        """
        add = add_all(self.inputarray)
        output = add / int(len(self.inputarray))
        return round(output)

    def median(self):
        """
        This function is returned median
        """
        length = len(self.inputarray)
        if length % 2 == 0:
            index = length // 2
            output = (self.sort[index] + self.sort[index - 1]) / 2
            return output
        else:
            index = length // 2
            output = self.sort[index]
            return output

    def mode(self):
        try:
            input = self.sort
            max_input = max(input)
            my_list = [0] * max_input
            for i in input:
                my_list[i - 1] += 1
            return my_list.index(max(my_list)) + 1
        except:
            pass # continue
    def array_range(self):
        small = self.sort[0]
        big = self.sort[len(self.sort) - 1]
        output = big - small
        return output


if __name__ == '__main__':
    inputls = []
    inputlen = int(input(""))
    for _ in range(inputlen):
        inputint = int(input(""))
        inputls.append(inputint)
    st = Statistics(inputls)
    print(st.mean())
    print(st.median())
    print(st.mode())
    print(st.array_range())