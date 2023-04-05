def lengthOfLongestSubstring(s):
    n = len(s)
    # Create a dictionary to store the last index of each character
    last_index = {}
    # Initialize variables to keep track of the start and end of the substring
    start = 0
    end = 0
    # Initialize variable to keep track of the maximum length
    max_length = 0
    # Loop through the string
    while end < n:
        # Check if the current character has been seen before
        if s[end] in last_index and last_index[s[end]] >= start:
            # If the character has been seen, update the start of the substring
            start = last_index[s[end]] + 1
        # Update the last index of the current character
        last_index[s[end]] = end
        # Update the end of the substring
        end += 1
        # Update the maximum length
        max_length = max(max_length, end - start)
    return max_length

print(lengthOfLongestSubstring("nndNfdfdf"))