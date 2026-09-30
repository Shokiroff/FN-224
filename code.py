def show_digit(n):
  while n > 0:
      pritn(n% 10)
      n = n // 10

def isPrime(n):
	j = 2
	while j * j <= n:
		if n % j == 0:
			return False
		j += 1
	return True

if __name__ == "__main__":
    show_digit(36521)
