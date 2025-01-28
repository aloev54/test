// package main

// import (
// 	"lab_2/pkg/benchmark"
// 	"lab_2/pkg/prime"
// )

// func main() {
// 	// numbers := []uint64{1}
// 	for i := uint64(1); i <= 65537; i++ {
// 		baseTime := benchmark.Measure(prime.IsPrimeBase, i)
// 		millerTime := benchmark.Measure(prime.IsPrimeMiller, i)
// 		benchmark.AddResult(i, baseTime, millerTime)

// 	}

//		benchmark.SaveResults("lab_2/data/results.csv")
//	}
package main

import (
	"fmt"
	"lab_2/pkg/benchmark"
	"lab_2/pkg/prime"
)

func main() {
	for i := uint64(1); i <= 65537; i++ {
		baseTime := benchmark.Measure(prime.IsPrimeBase, i)
		millerTime := benchmark.Measure(prime.IsPrimeMiller, i)

		// Отладочный вывод
		fmt.Printf("Number: %d | Base Time: %v | Miller Time: %v\n", i, baseTime, millerTime)

		benchmark.AddResult(i, baseTime, millerTime)
	}

	// Сохранение результатов
	err := benchmark.SaveResults("/Users/aloevartyom/Documents/dev/test/lab_2/data/results.csv")
	if err != nil {
		fmt.Println("Error saving results:", err)
	} else {
		fmt.Println("Results saved successfully!")
	}

	for n := 16; n <= 32; n++ {
		min := uint64(1 << (n - 1))
		max := uint64((1 << n) + 1)
		for i := min; i <= max; i++ {
			baseTime := benchmark.Measure(prime.IsPrimeBase, i)
			millerTime := benchmark.Measure(prime.IsPrimeMiller, i)
		}

	}
}
