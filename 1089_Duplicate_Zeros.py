class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)

        # Start checking the array from the first element
        i = 0

        # Traverse until the second-last position
        while i < n - 1:

            # Check if the current element is zero
            if arr[i] == 0:

                # Shift all elements one position to the right
                # Start from the last index to avoid overwriting elements
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]

                # Skip the duplicated zero
                i += 1

            # Move to the next element
            i += 1