def average(array):
    # your code goes here
    pure_array = set(array)
    suM = sum(pure_array)
    length = len(pure_array)
    return suM / length
    # return format(answer, '.3f')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)