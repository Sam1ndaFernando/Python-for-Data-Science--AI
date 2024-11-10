arr1 = [-10, -18, 12, 5, 7, 12, -3]  
arr2 = [8, 4, -3, 9, 2, 11]          


arr2.extend(arr1)                    # Extend arr2 by adding elements of arr1 to it
print("Before list:", arr2)           
arr2.sort()                          
print("After list:", arr2)            

length = len(arr2)                    # Calculate the length of the list
print("Length is:", length)           

# Calculate and print the median (middle element in sorted list)
print("Middle element :", arr2[6])

# Calculate the first quartile (Q1), which is the element at 1/4th of the length
num = int(length / 4)
q1 = arr2[num]
print("Q1:", q1)

# Calculate the third quartile (Q3), which is the element at 3/4th of the length
q3 = 3 * int(length / 4)
print("Q3:", arr2[q3]) 
