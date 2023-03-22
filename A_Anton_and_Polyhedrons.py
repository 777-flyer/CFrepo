numbers = int(input())

faces = 0

for i in range(numbers):

    string = input()
    
    if string == "Icosahedron":
        
        faces += 20
        
    elif string == "Dodecahedron":
        
        faces += 12
        
    elif string == "Octahedron":
        
        faces += 8
        
    elif string == "Cube":
        
        faces += 6
        
    elif string == "Tetrahedron":
        
        faces += 4
        
print(faces)