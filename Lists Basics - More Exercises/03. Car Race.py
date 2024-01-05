def final_time(racer_times):
    time_of_racer = 0
    for i in racer_times:
        if i > 0:
            time_of_racer += i
        else:
            time_of_racer *= 0.8
    return time_of_racer


times_list = [int(x) for x in input().split()]

length = len(times_list)//2

times_racer_one = times_list[:int(length)]
times_racer_two = times_list[:int(length): - 1]

if final_time(times_racer_one) < final_time(times_racer_two):
    print(f'The winner is left with total time: {final_time(times_racer_one):.1f}')
else:
    print(f'The winner is right with total time: {final_time(times_racer_two):.1f}')
