import module_a
import dis

print(module_a.test)
courses = ["Tělocvik", "Historie", "Matematika"]
index = module_a.find_index(courses, "Tělocvik")
print(index)  # Return 0