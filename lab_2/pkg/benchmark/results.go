package benchmark

import (
	"encoding/csv"
	"fmt"
	"os"
	"time"
)

type Result struct {
	Number uint64
	Base   time.Duration
	Miller time.Duration
}

var results []Result

func AddResult(n uint64, baseTime, millerTime time.Duration) {
	results = append(results, Result{n, baseTime, millerTime})
}

func SaveResults(filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"Number", "Base ms", "Miller ms"})
	for _, result := range results {
		writer.Write([]string{
			fmt.Sprintf("%d", result.Number),
			fmt.Sprintf("%f", result.Base.Seconds()*1000),
			fmt.Sprintf("%f", result.Miller.Seconds()*1000),
		})
	}

	return nil
}

// package benchmark

// import (
// 	"encoding/csv"
// 	"fmt"
// 	"os"
// 	"time"
// )

// type Result struct {
// 	Number uint64
// 	Base   time.Duration
// 	Miller time.Duration
// }

// var results []Result

// // AddResult добавляет результат в срез
// func AddResult(n uint64, baseTime, millerTime time.Duration) {
// 	results = append(results, Result{n, baseTime, millerTime})
// }

// // SaveResults сохраняет результаты в CSV файл
// func SaveResults(filename string) error {
// 	// Проверка наличия директории
// 	if _, err := os.Stat("lab_2/data"); os.IsNotExist(err) {
// 		err := os.MkdirAll("lab_2/data", os.ModePerm)
// 		if err != nil {
// 			return fmt.Errorf("failed to create directory: %v", err)
// 		}
// 	}

// 	file, err := os.Create(filename)
// 	if err != nil {
// 		return err
// 	}
// 	defer file.Close()

// 	writer := csv.NewWriter(file)
// 	defer writer.Flush()

// 	writer.Write([]string{"Number", "Base ms", "Miller ms"})
// 	for _, result := range results {
// 		writer.Write([]string{
// 			fmt.Sprintf("%d", result.Number),
// 			fmt.Sprintf("%f", result.Base.Seconds()*1000),
// 			fmt.Sprintf("%f", result.Miller.Seconds()*1000),
// 		})
// 	}

// 	return nil
// }
