string = input()
string_list = []
for i in range(len(string)):
    for j in range(i, len(string)):
        string_list.append(string[i:j+1])

print(len(set(string_list)))


print('----------')
# string = input()

string_list2 = []
for i in range(len(string)):
    for j in range(len(string)):
        string_list2.append(string[j:j+i])
print(len(set(string_list2)))
