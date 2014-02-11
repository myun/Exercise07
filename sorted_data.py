# Create an empty dictionary.
# Open file.
# Read file line by line.
# Process each line, use a while loop.
# print sorted dictionary with text to make readable.

restaurants = {}
f = open("scores.txt")

line = f.readline()
while line:
    templist = line.split(":")
    templist[1] = templist[1].strip()
    restaurants[templist[0]] = templist[1]
    line = f.readline()

for restaurant in sorted(restaurants):
    print "Restaurant", restaurant, "is rated at", restaurants[restaurant] + "."

f.close()