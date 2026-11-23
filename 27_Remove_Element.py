class Solution(object):
    def removeElement(self, arr, val):
        # Initialize j to keep track of valid elements
        j = 0

        # Traverse through the array
        for i in range(0, len(arr), 1):

            # Check if the current element is not equal to val
            if(arr[i] != val):

                # Swap the current element with the element at index j
                arr[i], arr[j] = arr[j], arr[i]

                # Move j to the next position
                j += 1

        # Return the count of elements that are not equal to val
        return j