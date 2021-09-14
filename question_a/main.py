# Assumptions: 
# A line can only overlap with another line iff one boundary of a line
# lies between another line's range. In other words, if a line "touches" 
# another line at a single point, we don't consider it to be overlapped.

# Given two lines, line1 and line2:
# There are two ways that line2 can overlap with line1
# Case 1:
#   The left boundary of line2 lies between the range of line1
# Case 2:
#   The right boundary of line2 lies between the range of line1
# Note: If a line2 is in between line1, we would've entered "Case 1" 

import sys

def main():
    if len(sys.argv) == 5:
        line1 = [sys.argv[1], sys.argv[2]]
        line2 = [sys.argv[3], sys.argv[4]]

        # Case 1: The left boundary of line2 lies between the range of line1
        if line2[0] > line1[0] and line2[0] < line1[1]:
            print("Overlap")

        # Case 2: The right boundary of line2 lies between the range of line1
        elif line2[1] > line1[0] and line2[1] < line1[1]:
            print("Overlap") 
        
        # Line 1 and line 2 do not overlap
        else:
            print("Does not overlap")

if __name__ == "__main__":
    main()
