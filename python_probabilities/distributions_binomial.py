from decimal import Decimal
import math

def BinomialPD_validate(k: object, n: object, p: object) -> None:
	if not isinstance(k, int) or k < 0:
		raise TypeError("Input value x must be positive integer")
	if not isinstance(n, int) or n < 0:
		raise TypeError("Input value n must be positive integer")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a positive decimal precentage")

def BinomialPD_calculate(k: int, n: int, p: Decimal) -> Decimal:
	return math.comb(n, k) * (p ** k)  * ((1 - p) ** (n - k))

def BinomialPD(kInput: int, nInput: int, pInput: float) -> Decimal:
	BinomialPD_validate(kInput, nInput, pInput)
	return BinomialPD_calculate(kInput, nInput, Decimal(str(pInput)))



def BinomialCD_calculate(k: int, n: int, p: Decimal) -> Decimal:
	return sum([BinomialPD_calculate(i, n, p) for i in range(k + 1)])

def BinomialCD(kInput: int, nInput: int, pInput: float) -> Decimal:
	BinomialPD_validate(kInput, nInput, pInput)
	return BinomialCD_calculate(kInput, nInput, Decimal(str(pInput)))



def InvBinomialCD_validate(x: object, n: object, p: object) -> None:
	if not isinstance(x, float) or x < 0:
		raise TypeError("Input value x must be a positive decimal precentage")
	if not isinstance(n, int) or n < 0:
		raise TypeError("Input value n must be positive integer")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a positive decimal precentage")

def InvBinomialCD_calculate(x: Decimal, n: int, p: Decimal) -> int:
	for i in range(n + 1):
		if BinomialCD_calculate(i, n, p) == x:
			return i

	for i in range(n + 1):
		tempX = BinomialCD_calculate(i, n, p)
		if tempX > x:
			upper_k_bound: int = i
			upper_diff: Decimal = abs(x - tempX)
			break
	for i in reversed(range(n)):
		tempX = BinomialCD_calculate(i, n, p)
		if tempX < x:
			lower_k_bound: int = i
			lower_diff: Decimal = abs(x - tempX)
			break

	if upper_diff < lower_diff:
		return upper_k_bound
	return lower_k_bound

def InvBinomialCD(xInput: float, nInput: int, pInput: float | int) -> int:
	InvBinomialCD_validate(xInput, nInput, pInput)
	return InvBinomialCD_calculate(
		Decimal(str(xInput)),
		nInput,
		Decimal(str(pInput))
	)