city = 'Orlando'
temp = 85
count = 5
avg = 3.4563892382


print(f"It is {temp}\u00B0 in {city}")  # variables inserted into string
print("It is {}\u00B0 in {}".format(temp, city))  # prior to 3.6
print("It is %d\u00B0 in %s" % (temp, city))

# .2f means round a float to 2 decimal points
print(f"count is {count:03d} avg is {avg:.2f}")

print(f"2 + 2 is {2 + 2}")  # any expression is OK
