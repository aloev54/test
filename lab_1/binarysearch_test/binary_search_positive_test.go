package binarysearch_test

import (
	"lab_1/binarysearch"
	"testing"

	"github.com/ozontech/allure-go/pkg/framework/provider"
	"github.com/ozontech/allure-go/pkg/framework/runner"
)

func TestTarget(t *testing.T) {
	runner.Run(t, "TestTarget", func(t provider.T) {
		//Arrange
		arr := []int{1, 3, 6, 8, 9}
		searchNum := 6

		//Act
		result := binarysearch.BinarySearch(arr, searchNum)

		//Assert
		t.WithNewStep("Checking result", func(s provider.StepCtx) {
			if result != 2 {
				t.Errorf("expected 2, found %d", result)
			}
		})

		// allure.Description("Test for binary search")
		// allure.Label("test", "binarysearch")
	})
}
