n = int(input())

x = y = z = 0

forces = []

for i in range(n):
    
    force = input().split(" ")
    
    for j in range(3):
        
        force[j] = int(force[j])
        
    forces.append(force)
    
for force in forces:
    
    x += force[0]
    y += force[1]
    z += force[2]       
   
if x == 0 and y == 0 and z == 0:
    print('YES')
    
else:
    print('NO')