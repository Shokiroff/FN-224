from os import system
system("clear")
def analyze_students_subjects(s1: set, s2: set) -> dict:
	a = sorted(list(s1.intersection(s2)))
	b = sorted(list(s1.difference(s2)))
	c = sorted(list(s2.difference(s1)))
	d = len(s1.union(s2))
	natija = {
		"umumiy": a,
		"faqat1": b,
		"faqat2": c,
		"umumiy_soni": d
	}
	return natija
set1 = {"Math", "Physics", "IT", "English"}
set2 = {"IT", "Biology", "Math"}
print("")
print(f"\n\t\t ----  Natija  ---- ")
res = analyze_students_subjects(set1, set2)
print("{")
print(f'  "umumiy": {res["umumiy"]}, ')
print(f'  "faqat1": {res["faqat1"]}, ')
print(f'  "faqat2": {res["faqat2"]}, ')
print(f'  "umumiy_soni": {res["umumiy_soni"]}, ')
print("}")
