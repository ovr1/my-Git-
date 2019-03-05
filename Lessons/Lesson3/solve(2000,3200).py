solution = []
def solv(num1, num2):
    for i in range(num1, num2):
        if i % 7 == 0 and i % 5 != 0:
            solution.append(str(i))
            continue
    return solution
solv(2000,3200)
print('{0}'.format(solution))