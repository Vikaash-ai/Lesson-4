amount = int(input("Enter your number: "))

note_100 = amount//100
left_over = amount%100
note_50 = left_over//50
left_over = left_over%50
note_10 = left_over//10
left_over = left_over%10
note_5 = left_over//5
left_over = left_over%5
note_1 = left_over//1

print(f"The 100 notes are: {note_100}")
print(f"The 50 notes are: {note_50}")
print(f"The 10 notes are: {note_10}")
print(f"The 5 notes are: {note_5}")
print(f"The 1 notes are: {note_1}")