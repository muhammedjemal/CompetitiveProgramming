class Solution:
    def numberToWords(self, num: int) -> str:
        pairs={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand",1000000:"Million",1000000000:"Billion"
    }
        if num==0:
            return pairs[num]
        result=[]
        def ones(n):
            if n==0: 
                return
            result.append(pairs[n])
        def tens(n):
            t = n//10 
                
            if t==1: 
                result.append(pairs[n])
            else:
                result.append(pairs[10*t])
                o = n%10 
                ones(o)
        def hundred(n):
        
            h = n//100 # Extract the hundred place digit
            result.append(pairs[h])
            result.append(pairs[100]) 
        
            if n%100>=10:
                tens(n%100)
            else:
                ones(n%100)
         
        div = 10**9
        while(num!=0):
        
            n = num//div 
                            
            if n>=100:
                hundred(n)
            elif n>=10:
                tens(n)
            else:
                ones(n)
        
            if div!=1 and n!=0: 
                result.append(pairs[div])
            
            num = num%div 
            div=div//1000
        return ' '.join(result)
