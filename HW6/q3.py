def lfsr(seed, polynomial, num_bits):
    result = [0] * num_bits
    for i in range(num_bits):
        feedback = seed & 1
        result[i] = seed
        seed >>= 1
        if feedback:
            seed ^= polynomial
    return result

def generate_patterns(initial_value, polynomial, num_patterns, num_bits):
    patterns = []
    seed = initial_value
    for _ in range(num_patterns):
        result = lfsr(seed, polynomial, num_bits)
        patterns.append(result)
        seed = result[-1]
    return patterns

def format_output(patterns):
    output = ''
    for pattern in patterns:
        output += ''.join(str(bit) for bit in pattern[::-1]) + '\n'
    return output

# Parameters
initial_value = 0b00000001
polynomial = 0b100011011
num_patterns = 8
num_bits = 8

# Generate and print the first 8 pseudo-random patterns
patterns = generate_patterns(initial_value, polynomial, num_patterns, num_bits)
output = format_output(patterns)
print(output)
