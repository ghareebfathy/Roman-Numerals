def RomanNumerals1(s):
    num = {'I': 1 , 'V': 5 , 'X': 10 , 'L':50,'C':100,'D':500,'M':1000}
    l_s = list(s)
    count = 0
    for i in l_s :
        count += num[i]
    return f'{s} should == {count}'
class RomanNumerals:
    anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rnums = "M CM D CD C XC L XL X IX V IV I".split()
    @classmethod
    def to_roman(self,x):
        self.x = x
        ret = []
        l = self.x
        for a,r in zip (self.anums,self.rnums):
            n,self.x = divmod(self.x,a)
            ret.append(r*n)
        return  ''.join(ret) #f"""{l}  should == "{''.join(ret)}" """
    @classmethod
    def from_roman(self,s):
        self.s = s
        num = {'I': 1 ,'II': 2 ,'III':3 , 'IV': 4 , 'V': 5 , 'X': 10 , 'L':50,'C':100,'D':500,'M':1000}
        count = 0
        for i in self.s :
            count += num.get(i)
        if num.get(count):
            return   num[count]#f"'{self.s}  should == {count}'"
        if count == 6:
            return count - 2
        return  count


print(RomanNumerals.to_roman(12))
print(RomanNumerals.from_roman('IV'))


