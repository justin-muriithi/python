# name:Justin Muriithi
# adm:BSCIT-05-0071/2024

def save_and_display_gross(hours: int, rate: float, filename: str = 'output.txt'):
	"""Compute gross pay, write to `filename`, then print the file contents."""
	gross_pay = hours * rate
	with open(filename, 'w', encoding='utf-8') as f:
		f.write(f"Gross pay: {gross_pay}\n")
	with open(filename, 'r', encoding='utf-8') as f:
		print(f.read().strip())

if __name__ == "__main__":
	hours = int(input("Enter hours: "))
	rate = float(input("Enter rate per hour: "))
	save_and_display_gross(hours, rate)
