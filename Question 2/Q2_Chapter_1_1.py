import time
def generate_number():
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50

    if generated_number % 2 == 0:
        generated_number += 10
    
    print(generated_number)

    return generated_number

generate_number()

