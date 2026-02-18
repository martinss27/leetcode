import "sort"

func twoSum(nums []int, target int) []int {
    type pair struct {
        value int
        index int
    }

    pairs := make([]pair, len(nums))

    for i, v := range nums {
        pairs[i] = pair{value: v, index: i}
    }

    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i].value < pairs[j].value
    })

    left := 0
    right := len(pairs) - 1

    for left < right {
        sum := pairs[left].value + pairs[right].value

        if sum == target {
            return []int{pairs[left].index, pairs[right].index}
        }

        if sum < target {
            left++
        } else {
            right--
        }
    }

    return nil
}
