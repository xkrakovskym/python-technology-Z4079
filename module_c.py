# importovat celého modulu jako m_a
import module_a as m_a

print(m_a.test)
courses = ["Tělocvik", "Historie", "Matematika"]
index = m_a.find_index(courses, "Tělocvik")
print(index)  # Return 0