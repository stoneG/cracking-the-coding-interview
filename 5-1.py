# Strategy:
# First clear i-j in N
# Then set i-j in N to M

# 1s for >j
left = ~((1 << (j + 1)) - 1)

# 1s for <i
right = 1 << i - 1

# Clearing i-j in N
mask = left | right
cleared_N = N & mask

# Shift M so we can set it into N
shifted_M = M << i

# Set shifted_M into N
cleared_N | shifted_M
