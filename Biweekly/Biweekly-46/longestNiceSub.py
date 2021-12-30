s = "YazaAay"

# brute

class solution:
    def longestNiceSubstring(s):
        ans = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                x = s[i:j+1]
                # print(x)
                if set(x) == set(x.swapcase()):
                    ans = max(ans, x, key=len)
        return ans
        # ans = ""
        # for i in range(len(s)):
        #     for ii in range(i+1, len(s)+1):
        #         if all(s[k].swapcase() in s[i:ii] for k in range(i, ii)):
        #             ans = max(ans, s[i:ii], key=len)
        # return ans

    # print(longestNiceSubstring(s))

#* o(n)

def longestNiceSubstring2(s):
    def divcon(s):
        # string with length 1 or less arent considered nice
        if len(s) < 2:
            return ""

        pivot = []
        # get every character that is not nice
        for i, ch in enumerate(s):
            if ch.isupper() and ch.lower() not in s:
                pivot.append(i)
            if ch.islower() and ch.upper() not in s:
                pivot.append(i)
    # if no such character return the string
        if not pivot:
            return s
    # divide the string in half excluding the char that makes the string not nice
        else:
            mid = (len(pivot)) // 2
            return max(divcon(s[:pivot[mid]]), divcon(s[pivot[mid]+1:]), key=len)

    return divcon(s)


# print(longestNiceSubstring2(s))

#* Recursive

def longestNiceSubstring3(s):
        chars = set(s); i = 0; ret = ''
        for j, c in enumerate(s):
            if c.swapcase() not in chars:
                ret = max(ret, longestNiceSubstring2(s[i:j]), key=len); i = j+1
        return max(ret, longestNiceSubstring2(s[i:]), key=len) if i else s