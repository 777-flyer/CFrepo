number_of_statements = int(input())

x = 0

for i in range(number_of_statements):
    
    statement = input()
    statement_ascii = 0
    plus_statement = ord('X') + ord('+') + ord('+')
    minus_statement = ord('X') + ord('-') + ord('-')
    
    for a in range(len(statement)):
        
        statement_ascii += ord(statement[a])
        
    if statement_ascii == plus_statement:
        
        x += 1
        
    elif statement_ascii == minus_statement:
        
        x -= 1
        
print(x)