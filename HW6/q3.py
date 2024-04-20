def lfsr_update(state, polynomial):
    feedback_bit = state & polynomial
    feedback_bit ^= (state & 1)  # Include the rightmost bit in the feedback
    feedback_bit ^= (feedback_bit >> 4)  # For x^8+x^4+x^3+x^2+1, the XOR taps are at bit positions 8, 4, 3, and 2
    new_bit = feedback_bit & 1
    state = (state >> 1) | (new_bit << 7)  # Shift right and add new bit at the leftmost position
    return state

def generate_pseudo_random_patterns(initial_state, polynomial, num_patterns):
    patterns = []
    state = initial_state
    for _ in range(num_patterns):
        patterns.append(state)
        state = lfsr_update(state, polynomial)
    return patterns

def main():
    polynomial = 0b110010011  # The primitive polynomial x^8+x^4+x^3+x^2+1 represented in binary
    initial_state = 0b00000001  # Initial state with only the rightmost bit set to 1
    num_patterns = 8

    patterns = generate_pseudo_random_patterns(initial_state, polynomial, num_patterns)
    print("First 8 pseudo-random patterns:")
    for pattern in patterns:
        print(bin(pattern)[2:].zfill(8))  # Convert to binary and ensure it's 8 bits

if __name__ == "__main__":
    main()
