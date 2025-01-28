package benchmark

import (
	"math/rand"
	"time"
)

func Measure(function func(uint64) bool, n uint64) time.Duration {
	start := time.Now()
	function(n)
	return time.Since(start)
}

func RandomNum(min, max uint64) uint64 {
	rand.Seed(time.Now().UnixNano())
	return min + uint64(rand.Int63n(int64(max-min)))
}
