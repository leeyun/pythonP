class MergeSort:
    def mergeSort(self, arr: list[int])->list[int]:
        if len(arr) <= 1:
            return arr
        