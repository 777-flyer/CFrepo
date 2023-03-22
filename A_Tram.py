stops = int(input())

pass_list = []
total_passenger = 0
pass_history = []

for i in range(stops):
    
    exiting, entering = input().split(' ')
    exiting = int(exiting)
    entering = int(entering)
    
    total_passenger -= exiting
    pass_history.append(total_passenger)
    total_passenger += entering
    pass_history.append(total_passenger)

max = 0
 
for i in pass_history:
    
    if i > max:
        max = i
    else:
        pass
    
print(max)