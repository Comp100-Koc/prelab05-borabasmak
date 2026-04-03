def longest_palindromic_substring(s):
    start = 0
    length = 0
    i = 0
    while i < len(s):
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            length =