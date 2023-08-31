courses = ['Science', 'Maths', 'History', 'Art']
courses_2 = ['Education']

# How many values are in out list
print(len(courses))

# Access first item
print(courses[0])

# Access last item
print(courses[-1])

# Access the first 2 items
print(courses[0:2])

# Access the last two
print(courses[2:])

# Add an item to the end
courses.append('Geography')
print(courses)

# Insert at a position 0
courses.insert(0, 'French')
print(courses)

# Extend a list
courses.extend(courses_2)
print(courses)

# Remove a value
courses.remove('Maths')
print(courses)

# Remove the last item by popping value
popped = courses.pop()
print(courses)
print(popped)

# Reverse a list 
courses.reverse()
print(courses)

# Sort a list 
courses.sort()
print(courses)

# Sort a list and then reverse
nums = [2,7,1,4,3,6,5]
nums.sort(reverse=True)
print(nums)

# Without mutation
courses = ['Science', 'Maths', 'History', 'Art']
sorted_courses = sorted(courses)
print(sorted_courses)

# Minimum number from a list
nums = [2,7,1,4,3,6,5]
print(min(nums))

# Max number from a list
nums = [2,7,1,4,3,6,5]
print(max(nums))

# Sum of all numbers
nums = [2,7,1,4,3,6,5]
print(sum(nums))

# Get index of an item in the list
courses = ['Science', 'Maths', 'History', 'Art']
print(courses.index('Art'))

# Check if Art is in the list
courses = ['Science', 'Maths', 'History', 'Art']
print('Art' in courses)

# Loop items
courses = ['Science', 'Maths', 'History', 'Art']

for item in courses:
    print(item)
    
# Loop items and get index
courses = ['Science', 'Maths', 'History', 'Art']

for index, item in enumerate(courses):
    print(index, item)
    
# List to strings
courses = ['Science', 'Maths', 'History', 'Art']

course_str = ', '.join(courses)
print(course_str)

# Back to a list
new_list = course_str.split(',')
print(new_list)