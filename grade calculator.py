print("===student grade calculator===")
name=input("enter your name: ")
marks=float(input("enter your marks out 0f 100: "))
if marks>=90:
    grade="A+"
elif 90>marks>=80:
    grade="A"
elif 80>grade>=70:
    grade="B"
elif 70>marks>=60:
    grade="C"
elif 60>marks>=50:
    grade="D"
else:
    grade="FAIL"

print(f"student name: {name}")
print(f"marks:{marks}")
print(f"grade:{grade}")
    
