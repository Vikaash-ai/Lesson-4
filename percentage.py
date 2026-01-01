maths = int(input("What is your maths score: "))
science = int(input("What is your science score: "))
coding = int(input("What is your coding score: "))
physics = int(input("What is your phiysics score: "))

# Add the sum
sum = maths+science+coding+physics

print(f"Thsi is you sum of score: {sum}")

# The Percentage
percent = (sum/400)*100

print(f"This is your percentage: {percent}")