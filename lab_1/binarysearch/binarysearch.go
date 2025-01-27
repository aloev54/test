package binarysearch

func BinarySearch(a []int, searchNum int) int {
	left, right := 0, len(a)-1

	for left <= right {
		mid := (left + right) / 2

		if a[mid] == searchNum {
			return mid
		} else if a[mid] < searchNum {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1

}
