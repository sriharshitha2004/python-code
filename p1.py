a=121
if str(a)==str(a)[::-1]:
	print(a,"is a palindrome")
else:
	print(a,"is not a palindrome")






positive_bucket = []
negative_bucket = []
zero = []

for num in range(-25, 26):
    if num > 0:
        positive_bucket.append(num)
    elif num < 0:
        negative_bucket.append(num)
    else:
        zero.append(num)

print("Positive Bucket:", positive_bucket)
print("Zero:", zero)
print("Negative Bucket:", negative_bucket)
