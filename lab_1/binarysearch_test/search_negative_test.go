package binarysearch_test

import (
	"lab_1/binarysearch"
	"testing"

	"github.com/ozontech/allure-go/pkg/framework/provider"
	"github.com/ozontech/allure-go/pkg/framework/runner"
)

func TestTargetNotInList(t *testing.T) {
	runner.Run(t, "TestTargetNotInList", func(t provider.T) {
		//Arrange
		arr := []int{1, 3, 6, 8, 9}
		searchNum := 4

		//Act
		result := binarysearch.BinarySearch(arr, searchNum)

		//Accert
		t.WithNewStep("Checking result", func(s provider.StepCtx) {
			if result != -1 {
				t.Errorf("expected -1, found %d", result)
			}
		})
	})
}
