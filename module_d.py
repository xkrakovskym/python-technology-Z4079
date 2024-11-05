# importovat pouze find_index funkce

from module_a import find_index, test

print(test)
courses = ["Tělocvik", "Historie", "Matematika"]
index = find_index(courses, "Tělocvik")
print(index)  # Return 0