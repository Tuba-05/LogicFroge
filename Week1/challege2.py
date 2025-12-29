# ****** Password Recovery Window ******

def function(log, pattern):
    """ function that takes two strings log and pattern and returns the minimum window substring 
    of log. If no valid window exists, return an empty string. """
    if len(log) < len(pattern):
        return ""
    
    s = "" 
    for ch in log:
        s += ch
        if pattern in s:
            pass
    return     

log = ""
pattern = ""
print(function(log, pattern))

#  **Example 1**
# Input:  log = "ADOBECODEBANC", pattern = "ABC"
# Output: "BANC"

# **Example 2**
# Input:  log = "a", pattern = "a"
# Output: "a"

# **Example 3**
# Input:  log = "a", pattern = "aa"
# Output: ""