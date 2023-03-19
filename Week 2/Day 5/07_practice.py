# Override the __len__() method on vector of 05_practice to display the dimension of the vector.

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

    def __len__(self):
        return len(self.vec)

v1=Vector([1,2,3])
v2=Vector([4,5,6])
print(v1+v2)
print(v1*v2)
print(len(v1))