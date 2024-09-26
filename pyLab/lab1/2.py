def trans(N):
    return round((1 / N), 1)


n = int(input())
prefix = [1.0]
for i in range(2, n + 1):
    prefix.append(prefix[i - 2] + trans(i))
print(prefix)
print(sum(prefix))