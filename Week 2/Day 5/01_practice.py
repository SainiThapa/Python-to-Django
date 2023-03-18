# Create a class c-2Dvector and use it to create another class representing a 3D vector
class C2dVector:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C3dVector(C2dVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

vec1=C2dVector(3,6)
vec2=C3dVector(3,6,9)
print(vec1)
print(vec2)