#Multiplication table from 2 to 20 and save them in different files in a folder
for i in range(2,21):
    for j in range(1,11):
        with open(f"Tables/Multiplicationtable_of_{i}.txt","a") as f:
            f.write(f"{i} X {j} = {i*j} \n")
            

