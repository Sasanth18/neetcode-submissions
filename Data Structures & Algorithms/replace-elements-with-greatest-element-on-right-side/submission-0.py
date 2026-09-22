class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a=-1 #at greatest value
        for i in range(len(arr)-1,-1,-1):   #reverse order
            new=max(a,arr[i]) #newvalue=max(oldvalue,arr[value])
            arr[i]=a 
            a=new # a becomes greatest value
        return arr
               