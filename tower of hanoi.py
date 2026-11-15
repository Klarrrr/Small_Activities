def hanoi_solver(number):
    first_rod=[i for i in range(number,0,-1)]
    third_rod=[]
    second_rod=[]
    result = f'{first_rod} {second_rod} {third_rod}\n'
    def move(n,source,auxiliary,target):
        nonlocal result
        if n==1:
            a=source.pop()
            target.append(a)
            result += f'{first_rod} {second_rod} {third_rod}\n'
            return
        move(n-1,source,target,auxiliary)
        a=source.pop()
        target.append(a)
        result += f'{first_rod} {second_rod} {third_rod}\n'
        move(n-1,auxiliary,source,target)
    move(number,first_rod,second_rod,third_rod)
    return result.rstrip('\n') 

print(hanoi_solver(3))