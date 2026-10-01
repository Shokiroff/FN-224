from os import system
system("clear")
def classify_words_by_vowels(words: list[str]) -> dict:
	unlilar = "euioa"
	kam = []
	orta = []
	kop = []
	for s in words:
		soni = 0
		for h in s.lower():
			if h in unlilar:
				soni = soni + 1
		if soni <= 1:
			kam.append(s)
		elif soni == 2 or soni == 3:
			orta.append(s)
		else:
			kop.append(s)
	natija = {
		"kam": kam,
		"o'rta": orta,
		"ko'p": kop
	}
	return natija
word_list = ["python", "an", "education", "sky", "developer"]
print("")
print(f"\n\t  ----  Natija  ----  ")
res = classify_words_by_vowels(word_list)
print("{")
print(f'    "kam": {res["kam"]}, ')
print(f'    "o\'rta": {res["o\'rta"]}, ')
print(f'    "ko\'p": {res["ko\'p"]}')
print("}")
