'''Divide the string s into n/k substrings, each of length k.

For each substring:

Remove any duplicate characters, but keep the order of characters.

Print each resulting string on a new line.'''

def merge_tools(string,k):
        for i in range(0, len(string), k):
            substring = string[i:i+k]
            
            seen = []
            for char in substring:
                if char not in seen:
                    seen.append(char)
    
            print(''.join(seen))



if __name__ == '__main__':
    merge_tools("AABCAADEFF",3)
