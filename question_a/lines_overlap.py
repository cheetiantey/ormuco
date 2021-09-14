# Assumptions: 
# A line can only overlap with another line iff one boundary of a line
# lies between another line's range. In other words, if a line "touches" 
# another line at a single point, we don't consider it to be overlapped.

# Approach:
# Given two lines, line1 and line2:
# There are two ways that line1 and line2 don't overlap
# Case 1:
#   line 1 lies to the left of line2. Hence, line1's right boundary
#   is smaller than line2's left boundary
# Case 2:
#   line 2 lies to the left of line1. Hence, line2's right boundary
#   is smaller than line1's left boundary
# If any of the two cases apply to the two lines, then they don't overlap
# Else, the two lines must overlap

import sys

# Returns True if the two lines overlap, otherwise return False
def overlap(a1, a2, b1, b2):
    line1 = [a1, a2]
    line2 = [b1, b2]

    # Case 1: line 1 lies to the left of line2
    if line1[1] <= line2[0]:
        return False

    # Case 2: line 2 lies to the left of line1
    elif line2[1] <= line1[0]:
        return False

    # The two lines must overlap
    else:
        return True

