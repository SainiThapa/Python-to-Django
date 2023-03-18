#Write a class Vector representing a  vector of n dimension.
# Overload the + and * operator which calculates the sum and the dot product of them.
class Vector:
    def __init__(self,vec) -> None:
        self.vec=vec
    def __str__(self):
        str1=''
        index=0
        for i in self.vec:
            str1+=f"{i}v{index} + "
            index+=1
        return str1[:-2]
    
    def __add__(self,vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return Vector(newlist)

    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum+=(self.vec[i]*vec2.vec[i])
        return (sum)

v1=Vector([1,2,3])
v2=Vector([4,5,6])
print(v1+v2)
print(v1*v2)