

def eq_solver(line1, line2):
    line1n = [0, 0, 0]
    line2n = [0, 0, 0]
    if line1[0] != line2[0]:
        line1n[0] = line1[0]*line2[0]*(-1)
        line1n[1] = line1[1]*line2[0]*(-1)
        line1n[2] = line1[2]*line2[0]*(-1)
        line2n[0] = line2[0]*line1[0]
        line2n[1] = line2[1]*line1[0]
        line2n[2] = line2[2]*line1[0]
    else:
        line1n[0] = line1[0]*(-1)
        line1n[1] = line1[1]*(-1)
        line1n[2] = line1[2]*(-1)
        line2n[0] = line2[0]
        line2n[1] = line2[1]
        line2n[2] = line2[2]

    top = [line1n[0]+line2n[0], line1n[1]+line2n[1], line1n[2]+line2n[2]]

    y = top[2]/top[1]
    x = (line1n[2] - line1n[1]*y) / line1n[0]

    print("x = ",x, "\ny = ", y)

def eq_input():
    print("x and y are variables and a, b and c are constants where:\na1x + b1y = c1\na2x + b2y = c2\nTo solve this kind of equations;")
    print("please enter the constants of the first equation:")
    cons1 = []
    cons2 = []
    for x in range(3):
        a = int(input())
        cons1.append(a)
    
    print("please enter the constants of the second equation:")
    for x in range(3):
        b = int(input())
        cons2.append(b)
    
    eq_solver(cons1, cons2)

eq_input()
