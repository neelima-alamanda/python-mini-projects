stack = []  # Initialize an empty stack for storing opening brackets
inputstring = input("Enter input: ")  # Take input string from the user
balanced = True  # Assume initially that the input string is balanced

# Loop through each character in the input string
for ch in inputstring:
    # If the character is an opening bracket, push it onto the stack
    if ch == '{' or ch == '[' or ch == '(':
        stack.append(ch)
    
    # If the character is a closing bracket, check for balance
    elif ch == '}' or ch == ']' or ch == ')':
        # If stack is empty, no matching opening bracket exists
        if len(stack) == 0:
            balanced = False
            break 
        
        top = stack.pop()  # Pop the top element from the stack
        
        # Check if the closing bracket corresponds to the correct opening bracket
        if ch == ')' and top != '(':
            balanced = False
            break
        if ch == ']' and top != '[':
            balanced = False
            break
        if ch == '}' and top != '{':
            balanced = False
            break

# If the stack is not empty or a mismatch was detected, the input is not balanced
if stack or not balanced:
    print("Not Balanced")  # Print not balanced if brackets don’t match
else:
    print("Balanced")  # Print balanced if all brackets match correctly