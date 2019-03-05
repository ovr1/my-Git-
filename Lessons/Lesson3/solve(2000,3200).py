solution = []
def solv():
    for i in range(2000,3200):
        if i % 7 == 0 and i % 5 != 0:
            solution.append(str(i))
            continue
    return solution
solv()
print('{0}'.format(solution))