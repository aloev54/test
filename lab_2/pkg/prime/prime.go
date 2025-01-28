package prime

import "math/big"

func IsPrimeBase(n uint64) bool {
	if n < 2 {
		return false
	}
	for i := uint64(2); i*i < n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func IsPrimeMiller(n uint64) bool {
	bigN := big.NewInt(0).SetUint64(n)
	return bigN.ProbablyPrime(30)
}
