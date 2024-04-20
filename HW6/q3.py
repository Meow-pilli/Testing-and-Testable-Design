def lfsr(seed, taps):
    while True:
        yield seed & 1
        feedback = sum((seed >> tap) & 1 for tap in taps) % 2
        seed = (seed >> 1) | (feedback << 7)

def generate_patterns(initial_value, num_patterns):
    taps = [8, 4, 3, 2]
    lfsr_gen = lfsr(initial_value, taps)
    patterns = []
    for _ in range(num_patterns):
        pattern = next(lfsr_gen)
        patterns.append(pattern)
    return patterns

def format_output(patterns):
    output = ''
    for pattern in patterns:
        output += format(pattern, '08b') + '\n'
    return output

# Initial value of LFSR
initial_value = 0b00000001

# Generate and print the first 8 pseudo-random patterns
patterns = generate_patterns(initial_value, 8)
output = format_output(patterns)
print(output)
