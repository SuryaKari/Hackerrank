# Enter your code here. Read input from STDIN. Print output to STDOUT
first = int(raw_input())
second = set(list(map(int,raw_input().split(" "))))
third = int(raw_input())
fourth = set(list(map(int,raw_input().split(" "))))

diff1 = list(second.difference(fourth))
diff2 = list(fourth.difference(second))

for i in diff2:
    diff1.append(i)

for i in sorted(diff1):
    print i