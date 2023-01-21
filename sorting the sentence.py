class Solution:
    def sortSentence(self, s: str) -> str:

        nums = ["1","2","3","4","5","6","7","8","9"]
        abc = ""
        xx = 0
        for x in range(len(s)):
            if (s[x-1] == " ") or (x == 0):
                xx += 1
                for y in range(x, len(s)):
                    if s[y] == "1":
                        one = s[x:y] 
                    elif s[y] == "3":
                        three = s[x:y]
                    elif s[y] == "4":
                        four = s[x:y]
                    elif s[y] == "5":
                        five = s[x:y]
                    elif s[y] == "6":
                        six = s[x:y]
                    elif s[y] == "7":
                        seven = s[x:y]
                    elif s[y] == "8":
                        eight = s[x:y]
                    elif s[y] == "9":
                        nine = s[x:y]
                    elif s[y] == "2":
                        two = s[x:y]
        if xx == 1:
            abc = str(one) 
        if xx == 2:
            abc = str(one) +" "+ str(two)
        if xx == 3:
            abc = str(one) +" "+ str(two) +" "+ str(three)
        if xx == 4:
            abc = str(one)  +" "+ str(two) +" "+ str(three) +" "+ str(four)
        if xx == 5:
            abc = str(one)  +" "+ str(two) +" "+ str(three) +" "+ str(four) +" "+ str(five)
        if xx == 6:
            abc = str(one)  +" "+ str(two) +" "+ str(three) +" "+ str(four) +" "+ str(five) +" "+ str(six)
        if xx == 7:
            abc = str(one)  +" "+ str(two) +" "+ str(three) +" "+ str(four) +" "+ str(five) +" "+ str(six) +" "+ str(seven)
        if xx == 8:
            abc = str(one)   +" "+ str(two) +" "+ str(three) +" "+ str(four) +" "+ str(five) +" "+ str(six) +" "+ str(seven) +" "+ str(eight) 
        if xx == 9:
            abc = str(one)  +" "+ str(two) +" "+ str(three) +" "+ str(four) +" "+ str(five) +" "+ str(six) +" "+ str(seven) +" "+ str(eight) +" "+ str(nine)
        return abc
