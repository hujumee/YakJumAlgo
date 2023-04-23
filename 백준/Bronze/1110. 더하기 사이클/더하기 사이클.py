n = int(input())
cnt, n_sum, n_new = 0, 0, 0

n_init = n

while n_new != n_init:
    units = n % 10
    tens = n // 10
    n_sum = tens + units
    if (n_sum > 9):
        n_sum = n_sum % 10
    n_new = units * 10 + n_sum
    n = n_new
    cnt = cnt + 1
    
if (cnt == 0):
    cnt = 1
print(cnt)