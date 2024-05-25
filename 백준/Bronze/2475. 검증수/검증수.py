def test_num(arr):
    sm = 0
    for i in range(5):
        sm+=arr[i]*arr[i]
    result = sm%10
    return result

arr = list(map(int, input().split()))
print(test_num(arr))