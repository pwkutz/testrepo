def maxDistance(s):
    n = len(s)
    max_dist = -1
    i = 0

    while i < n:
        # If current character is '1'
        if s[i] == '1':
            j = i + 1

            # Find the next '1'
            while j < n:
                if s[j] == '1':
                    # Calculate the distance between current and next '1'
                    dist = j - i

                    # Update the maximum distance and break
                    max_dist = max(max_dist, dist)
                    break
                j += 1

            i = j
        else:
            i += 1

    # Return the maximum distance
    return max_dist -1


# Main function
if __name__ == "__main__":
    S = "101010"

    # Function call
    print(maxDistance(S))