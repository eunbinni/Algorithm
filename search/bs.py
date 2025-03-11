n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst)
def bs(start, end, target):
    mid = (start+end) // 2 # index
    if start > end:
        return
    if lst[mid] == target:
        return lst[mid]
    elif lst[mid] < target:
        return bs(mid+1, end, target)
    else:
        return bs(start, mid-1, target)

result = bs(0, len(lst)-1, m)
print(lst.index(result)+1)