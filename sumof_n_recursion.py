def calc_sum(n):
    if n == 1:
        return 1
    else:
        return n + calc_sum(n-1)


output = calc_sum(5)        
print(output)