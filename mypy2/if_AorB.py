
import random as r

n = r.randint(0,100)


if n <= 10 or n >= 100:
    print("n은 10보다 작거나 100보다 큽니다")
elif n >= 11 and n <= 50:
    print("n은 11보다 크고 50보다는 작습니다")
elif n >= 51 and n <= 98:
    print("n은 51보다 크고 98보다 작습니다")
else:
    print("n은 99입니다")

print(n)
print("정답은?")
ans = int(input())


if ans == n:
    print("정답!", n)
else:
    print("땡!")