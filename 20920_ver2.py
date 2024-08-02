"""
정렬, 다시풀기 1회

1. pop을 하면 dict(list)의 크기가 지속적으로 바뀌어서 for문 사용 불가
2. dict를 value 값을 기준으로 정렬 하는 방법 : key = lambda x: x[1]
    - x는 (key, value)를 나타냄
3. reverse = True를 사용하지 않고 -를 이용해서 오름차순/내림차순을 자유롭게 사용 가능
    - reverse를 사용하면 전체를 전부 오름/내림차순으로 컨트롤만 할 수 있음

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

words_list = [input().strip() for _ in range(n)]

words_dict = {}
for word in words_list:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1

# 길이가 m 이하인 단어들만 뽑기
remove_word = [word for word in words_dict if len(word) < m]
for key in remove_word:
    words_dict.pop(key)

# dict 정렬
sorted_words_dict = dict(sorted(words_dict.items(), key = lambda x: (-x[1], -len(x[0]), x[0])))
# print(sorted_words_dict)
for word in sorted_words_dict:
    print(word)