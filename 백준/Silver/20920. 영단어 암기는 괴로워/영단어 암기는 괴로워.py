import sys
ipt = sys.stdin.readline
n, m = map(int, ipt().split())

word_list = []
for _ in range(n):
    word = ipt().strip()

    if len(word) >= m:
        word_list.append(word)
# ['apple', 'sand', 'apple', 'append', 'sand', 'sand']

# 등장 횟수 > 길이 > 사전순
word_list.sort()

word_dict = {}
for i in range(len(word_list)):
    if word_list[i] not in word_dict.keys():
        word_dict[word_list[i]] = [1, len(word_list[i]), i]
    else:
        value = word_dict[word_list[i]]
        word_dict[word_list[i]] = [value[0] + 1, value[1], value[2]]

word_sorted = sorted(word_dict.items(),key=lambda x:(-x[1][0], -x[1][1], x[1][2]))


for word in word_sorted:

    print(word[0])
