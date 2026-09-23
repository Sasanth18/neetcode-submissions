class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for i in details:
            ten=ord(i[11])-ord("0")    #starts at 1st number ord(0)= 48 and adding +1 for ord(n) n=0,1,2,3,...
            one=ord(i[12])-ord("0")
            age=one+10*ten   # by using slicing age = int(i[11:13])
            if age>60:
                res+=1
        return res

