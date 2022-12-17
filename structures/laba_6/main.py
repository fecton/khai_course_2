from time import time

class Search:
    def __init__(self, STRING: str = "", SUB: str = "") -> None:
        self.string = STRING
        self.sub    = SUB

    def Linear(self):
        op = 0
        tmp = ""
        i = 0

        while i < len(self.string):
            if self.sub == tmp:
                return (True, op)
            if self.sub[0] == self.string[i]:
                j = 0
                tmp = ""
                while j < len(self.sub):
                    if self.sub[j] == self.string[i]:
                        tmp += self.sub[j]
                        j += 1
                        i += 1
                        op += 1
                    else:
                        break
            i += 1
            op += 1
        return (False, op)

    def PK(self):
        op = 0
        pattern = self.sub
        text    = self.string
        q = 2147483647
        d = 10

        m = len(pattern)
        n = len(text)
        p = 0
        t = 0
        h = 1
        i = 0
        j = 0

        for i in range(m-1):
            h = (h*d) % q
            op += 1

        # Calculate hash value for pattern and text
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q
            op += 1

        # Find the match
        for i in range(n-m+1):
            op += 1
            if p == t:
                for j in range(m):
                    op += 1
                    if text[i+j] != pattern[j]:
                        break

                j += 1
                if j == m:
                    # print("Pattern is found at position: " + str(i+1))
                    return (True, op)

            if i < n-m:
                t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

                if t < 0:
                    t = t+q
        return (False, op)
    
    def KMP(self):
        op = 0
        pat = self.sub
        txt = self.string

        M = len(pat)
        N = len(txt)
    
        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0]*M
        j = 0 # index for pat[]
    
        # Preprocess the pattern (calculate lps[] array)
        computeLPSArray(pat, M, lps)
    
        i = 0 # index for txt[]
        while i < N:
            op += 1
            if pat[j] == txt[i]:
                i += 1
                j += 1
    
            if j == M:
                # print ("Found pattern at index", str(i-j))
                return (True, op)
                j = lps[j-1]
    
            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return (False, op)
 
    def Internal(self):
        return (False, 0) if self.string.find(self.sub) == -1 else (True, 0)


def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1 


def Time(self, func):
    start = time()
    data = func(self)
    end = time() - start
    print("Runtime: ", round(end, 10))
    return data


def main():
    s = Search()

    strings = open("tests.txt").readlines()
    sub = strings[0]
    strings = strings[1:]
    s.sub = sub
    # N = 10, 50, 100, 150, 200, 250, 300, 400, 500
    
    
    for Method in (Search.Linear, Search.PK, Search.KMP, Search.Internal):
        print("Current method:\t", Method.__name__, end="\n\n")
        for string in strings:
            s.string    = string
            
            result = Time(s, Method)
            if result[0] == True:
                print("[+] Passed!")
                print("[+] Operation Count : ", result[1])
            else:
                print("[-] FAILED!!!")
                print("Expected (%s) got %s" % (True, result[0]))
            print()
        print("\n")
        
    print("<<< SUBS >>>")
    print("="*40)

    # N = 10, 50, 100, 150, 200, 250, 300, 400, 500
    subs = [x.replace("\n", "") for x in open("subs.txt").readlines()]
    string = subs[0]
    s.string = string
    subs = subs[1:]

    for Method in (Search.Linear, Search.PK, Search.KMP, Search.Internal):
        print("Current method:\t", Method.__name__, end="\n\n")
        for sub in subs:
            s.sub = sub
            
            result = Time(s, Method)
            if result[0] == True:
                print("[+] Passed!")
                print("[+] Operation Count : ", result[1])
            else:
                print("[-] FAILED!!!")
                print("Expected (%s) got %s" % (True, result[0]))
            print()
        print("\n")
        
main()
