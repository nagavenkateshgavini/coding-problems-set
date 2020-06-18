'''
Input:
2
7
2 3 10 6 4 8 1
6
7 9 5 6 3 2

Output:
8
2
'''
def find_maxdiff(arr):
    arr = [int(ele) for ele in arr if ele]
    max_diff = 0
    min_ele = arr[0]
    for curr_ele in arr[1:]:
        if curr_ele < min_ele:
            min_ele = curr_ele

        curr_diff = curr_ele - min_ele
        if curr_diff < 0:
            curr_diff = 0

        if curr_diff > max_diff:
            max_diff = curr_diff

    if max_diff == 0: max_diff = -1

    return max_diff

if __name__ == "__main__":
    tests = int(input())
    final_res = []
    for test in range(tests):
        no_of_ele = int(input())
        final_res.append(find_maxdiff(input().split(' ')))

    for res in final_res:
        print(res)
