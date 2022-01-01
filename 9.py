a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
"""
한 줄에 하나의 정수가 들어올 때에는 a = int(input())

한 줄에 여러 정수가 들어오되, 그 개수가 정해져 있을 때에는 a, b = map(int, input().split())

한 줄에 여러 정수가 들어오되, 그 개수를 모를 때에는 a = list(map(int, input().split())) 으로 받고 a 리스트를 인덱싱하기

//는 정수만 돌려준다
"""