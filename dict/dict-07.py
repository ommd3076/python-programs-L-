scores = {
    "math": 78,
    "science": 84,
    "english": 72
}
sub = input("Enter a subject: ")
score = int(input("Enter the score: "))
scores[sub] = score
if sub in scores:
    print(scores)
else:
    print("Subject not found in the dictionary.")