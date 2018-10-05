import math
class BM :
    def __init__(self, pattern) :
        self.pattern = pattern
        self.last_occ = self.compute_last_occ()

    def get_pattern(self) :
        return self.pattern

    def get_last_occ(self) :
        return self.last_occ

    def compute_last_occ(self) :
        i = 0
        last_occ = []

        while i < 256 :
            last_occ.append(-1)
            i = i + 1

        i = 0
        while i < len(self.pattern) :
            last_occ[ord(self.pattern[i])] = i
            i += 1

        return last_occ

    def is_match(self, text) :

        if len(self.pattern) > len(text) :
            return False
        else :
            i = len(self.pattern) - 1
            j = i

            while True :
                if self.pattern[j] == text[i] :
                    if j == 0 :
                        return True
                    else :
                        i -= 1
                        j -= 1
                else :
                    if(ord(text[i])) < 256 :
                        lo = self.last_occ[ord(text[i])]
                    else :
                        lo = -1
                    i = i + len(self.pattern) - min(j, 1+lo)
                    j = len(self.pattern) - 1

                if i >= len(text) :
                    return False

