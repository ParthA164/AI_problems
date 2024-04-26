def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    jug1_current = 0  # Initial amount of water in jug 1
    jug2_current = 0  # Initial amount of water in jug 2

    print(f"Initial State: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}")

    while jug1_current != target_amount and jug2_current != target_amount:
        # If jug 2 is full, empty it
        if jug2_current == jug2_capacity:
            jug2_current = 0
            print(f"Empty Jug 2: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}")

        # If jug 1 is empty, fill it
        if jug1_current == 0:
            jug1_current = jug1_capacity
            print(f"Fill Jug 1: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}")
        else:
            # Pour water from jug 1 to jug 2
            pour_amount = min(jug1_current, jug2_capacity - jug2_current)
            jug1_current -= pour_amount
            jug2_current += pour_amount
            print(f"Pour from Jug 1 to Jug 2: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}")

    print("Target amount reached!")
    print(f"Final State: Jug 1: {jug1_current}/{jug1_capacity}    Jug 2: {jug2_current}/{jug2_capacity}")

# Example usage:
water_jug_problem(4, 3, 2)