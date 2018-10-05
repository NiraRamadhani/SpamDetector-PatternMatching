class KMP :

    def __init__(self, pattern) :
        self.pattern = pattern
        self.border = self.compute_border()

    def get_pattern(self) :
        return self.pattern

    def get_border(self) :
        return self.border

    def compute_border(self) :
        border = [0]
        prefix = 0

        i = 1
        j = 0

        while(i < len(self.pattern)) :
            if(self.pattern[i] == self.pattern[j]) :
                prefix = j + 1
                j += 1
                i += 1

            else :
                while(j > 0 and self.pattern[i] != self.pattern[j]) :
                    j = border[j-1]
                    prefix = j

                if(self.pattern[i] == self.pattern[j]) :
                    prefix += 1

            border.append(prefix)
            i += 1

        return border

    def is_match(self, text) :
        i = 0
        j = 0

        while(i < len(text)) :
            if(self.pattern[j] != text[i]) :
                if(j > 0) :
                    j = self.border[j-1]

            if(self.pattern[j] == text[i]) :
                j += 1

            if(j == len(self.pattern)) :
                return True

            i += 1
        return False
