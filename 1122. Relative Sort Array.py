class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        elements_which_not_in_arr2 = sorted([i for i in arr1 if i not in arr2])
        d = {i:arr1.count(i) for i in arr2}
        arr3 = []
        for k,v in d.items():
            arr3.extend(
                [k for i in range(v)]
            )
        arr3 = arr3 + elements_which_not_in_arr2
        return arr3
