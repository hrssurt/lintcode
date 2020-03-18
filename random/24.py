from itertools import permutations
from copy import deepcopy

signs = ["+", "-", "*", "/"]
def permutation(lst):
    if not lst: return lst
    if len(lst) == 1: return [lst]
    result = []
    for idx, item in enumerate(lst):
        next_permutations = permutation(lst[:idx] + lst[idx+1:])
        for p in next_permutations:
            result.append([item] + p)
    return result

def add_para(lst):
    for start in range(0, len(lst) - 1, 2):
        for end in range(start+2, len(lst)+2, 2):
            lst_cpy = deepcopy(lst)         
            lst_cpy.insert(start, "(")
            lst_cpy.insert(end, ")")
            try:
                if eval("".join(lst_cpy)) == 24:
                    return lst_cpy
                # else:
                #     for second_start in range(0,len(lst_cpy)):
                #         for second_end in range(second_start, len(lst_cpy)):
                            
                #             lst_cpy_2 = deepcopy(lst_cpy)
                #             lst_cpy_2.insert(second_start, "(")
                #             lst_cpy_2.insert(second_end, ")")
                #             print(lst_cpy_2)
                #             if eval("".join(lst_cpy_2)) == 24:
                #                 print(lst_cpy_2)
                                # return lst_cpy_2
            except Exception as e:
              # print(e)
              return None

    return None


def search(lst_of_num, cur_equation, idx):
    if idx >= len(lst_of_num):
        if eval("".join(cur_equation)) == 24:
            return cur_equation

        p_equation = add_para(cur_equation)
        if p_equation:
            return p_equation
        else:
            return None


    top_n = lst_of_num[idx]

    if not cur_equation:
        cur_equation.append(top_n)
        res = search(lst_of_num, cur_equation, idx+1)
        if res:
            return res
        else:
            return None
    else:
        for sign in signs:
            cur_equation.append(sign)
            cur_equation.append(top_n)
            res = search(lst_of_num, cur_equation, idx+1)
            if res:
                return res
            cur_equation.pop(-1)
            cur_equation.pop(-1)


if __name__ == '__main__':
    x = input("Please enter the input numbers seprated by space:\n")
    nums = x.strip().split(" ")
    nums = [n for n in nums if n]    # remove empty strings
    p_lst = permutations(nums)       # using import
    for p in p_lst:
        res = search(p, [], 0)
        if res:
            print(" ".join(res) + " = 24")
            exit()

    print("No soln found")

# add_para(res)
"""
1 + 1 + 3  + 5
"""





