def extract_integer_sum(s, running_total, running):
    number = ''
    i = 0
    for char in s:
        
        if s[i:i+3].lower() == "off" and not running:
            running = True

        elif s[i:i+2].lower() == "on" and running:
            running = False

        if char == '=':
            print(running_total)
        elif char.isdigit() and not running:
            number += char
        elif number and not running:
            running_total += int(number)
            number = ''
        i += 1

    if number and not running:
        running_total += int(number)
        
    return running_total, running

running_total = 0
running = False

substrings = ["off", "on"]

user_input = input()

running_total, running = extract_integer_sum(user_input, running_total, running)
print(running_total)
