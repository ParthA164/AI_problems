def water_jug_problem(jug1_capacity, jug2_capacity, jug3_capacity, target_amount):
    jug1_current = 0  # Initial amount of water in jug 1
    jug2_current = 0  # Initial amount of water in jug 2
    jug3_current = 0  # Initial amount of water in jug 3

    print(f"Initial State: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

    max_iterations = 1000  # Maximum number of iterations to prevent infinite loop
    iterations = 0

    while jug1_current != target_amount and jug2_current != target_amount and jug3_current != target_amount and iterations < max_iterations:
        iterations += 1

        # If jug 3 is full, empty it
        if jug3_current == jug3_capacity:
            jug3_current = 0
            print(f"Empty Jug 3: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

        # If jug 2 is full, empty it
        if jug2_current == jug2_capacity:
            jug2_current = 0
            print(f"Empty Jug 2: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

        # If jug 1 is empty, fill it
        if jug1_current == 0:
            jug1_current = jug1_capacity
            print(f"Fill Jug 1: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

        else:
            # Pour water from jug 1 to jug 2
            pour_amount = min(jug1_current, jug2_capacity - jug2_current)
            jug1_current -= pour_amount
            jug2_current += pour_amount
            print(f"Pour from Jug 1 to Jug 2: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

            # Pour water from jug 2 to jug 3
            pour_amount = min(jug2_current, jug3_capacity - jug3_current)
            jug2_current -= pour_amount
            jug3_current += pour_amount
            print(f"Pour from Jug 2 to Jug 3: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

            # Pour water from jug 3 to jug 1
            # pour_amount = min(jug3_current, jug1_capacity - jug1_current)
            # jug3_current -= pour_amount
            # jug1_current += pour_amount
            # print(f"Pour from Jug 3 to Jug 1: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

    if iterations >= max_iterations:
        print("Maximum iterations reached. Exiting loop.")
        
    if(iterations!=max_iterations):
        print("Target amount reached!")
        print(f"Final State: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}    Jug 3: {jug3_current}/{jug3_capacity}")

# Example usage:
water_jug_problem(7, 4, 5,6)
