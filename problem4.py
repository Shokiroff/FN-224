from os import system
import json
system("clear")
def sales_analysis():
	f = open("sales.json", "rt")
	mahsulotlar = json.load(f)
	f.close()

	jami = 0
	katta = 0
	kichik = 9999999999
	omadli = ""
	omadsiz = ""
	katta_mahsulotlar = []
	hisobot = []
	for m in mahsulotlar:
		nomi = m["product"]
		daromad = m["price"] * m["quantity"]

		hisobot.append(f"{nomi} - {daromad}")
		jami = jami + daromad

		if daromad > katta:
			katta = daromad
			omadli = nomi
		if daromad < kichik:
			kichik = daromad
			omadsiz = nomi
		if daromad >= 1000000:
			katta_mahsulotlar.append(nomi)

	natija = {
		"har_biri": hisobot,
		"kop_nomi": omadli,
		"kop_puli": katta,
		"kam_nomi": omadsiz,
		"kam_puli": kichik,
		"jami": jami,
		"katta_royxat": katta_mahsulotlar
	}
	return natija
res = sales_analysis()
for qator in res["har_biri"]:
	print(qator)
print("")
print(f"Eng ko'p daromad: {res['kop_nomi']} ({res['kop_puli']})")
print(f"Eng kam daromad: {res['kam_nomi']} ({res['kam_puli']})")
print("")
print(f"Umumiy savdo: {res['jami']}")
print("")
print("1000000 dan yuqori: ")
print(res["katta_royxat"])
