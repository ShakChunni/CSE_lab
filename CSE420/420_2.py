from tabnanny import check
input_file = open('input2.txt', 'r')
input_file = input_file.read()
inp = input_file.split('\n')
website_keywords = ["w", "w", "w", "."]
email_keywords = ["@"]
valid_ending_keywords = ["."]
state = "q0"
for i in range(1, len(inp)):
    if state == "q0":
        if inp[i][0].isalpha():
            state = "q1"
        elif inp[i][0].isdigit():
            state = "q9"        
    if state == "q1":
        check = all(item in inp[i][:4] for item in website_keywords)
        if check:
            state = "q2"
        else:
            state = "q3"
    if state == "q2":
        for j in range(len(inp[i]) - 4, len(inp[i])):
            if inp[i][j].isdigit():
                state = "q9"
            elif inp[i][j] in valid_ending_keywords:
                state = "q4"   
    if state == "q3":
        for j in range(len(inp[i]) - 4, len(inp[i])):
            if inp[i][j].isdigit():
                state = "q9"
            elif inp[i][j] in valid_ending_keywords:              
                state = "q5"
    if state == "q4":
        print("Web,", i)
    if state == "q5":
        print("Email,", i)
    state = "q0"
