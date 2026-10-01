from os import system
system("clear")
def clean_and_format_emails(emails: list[str]) -> list[str]:
	yangi = []
	for i in emails:
		toza = i.strip().lower()
		yangi.append(toza)
	saralangan = sorted(list(set(yangi)))
	return saralangan
emails_list = ["  USER@gmail.com", "admin@mail.com", "User@gmail.com", "test@site.com"]
print(f"\n\t\t  ----  Natija  ----  ")
print(clean_and_format_emails(emails_list))
