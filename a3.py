math=int(input("enter math marks:"))
history=int(input("enter history marks:"))
science=int(input("enter science marks:"))
computer=int(input("enter computer marks:"))
sum_of_all=math+history+science+computer
avg=sum_of_all/4
if avg>90:
    print("grade A")
elif avg<90 and avg>80:
    print("grade B")    
elif avg<80 and avg>70:
    print("grade C")    
elif avg<70 and avg>60:
    print("grade D")    
elif avg<60 and avg>50:
    print("grade E")    
else:
    print("grade F .you are failed!!")    
