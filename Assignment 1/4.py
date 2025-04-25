
# 4. Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
# numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
# classes should be the original set/list.]

numbers = range(1, 10001)

equivalence_classes = {i: [] for i in range(5)}
 
for num in numbers:
    remainder = num % 5
    equivalence_classes[remainder].append(num)

# Validate equivalence classes by checking if their union forms the original set
union_of_classes = set()
for eq_class in equivalence_classes.values():
    union_of_classes.update(eq_class)

validity = set(numbers) == union_of_classes

# Print the equivalence classes and validation result
for remainder, eq_class in equivalence_classes.items():
    print(f"Equivalence class for modulo 5 = {remainder}: {eq_class[:10]}...")  # Print first 10 numbers  
print(f"\nAre the equivalence classes valid? {'Yes' if validity else 'No'}")