def splitArray(nums, k):
    def countSubarrays(max_sum):
        count = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > max_sum:
                count += 1
                current_sum = num
            else:
                current_sum += num

        return count

    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = left + (right - left) // 2
        if countSubarrays(mid) <= k:
            right = mid
        else:
            left = mid + 1

    return left

# Exemplo 1
nums1 = [7, 2, 5, 10, 8]
k1 = 2
print(splitArray(nums1, k1))  # Saída: 18

# Exemplo 2
nums2 = [1, 2, 3, 4, 5]
k2 = 2
print(splitArray(nums2, k2))  # Saída: 9
