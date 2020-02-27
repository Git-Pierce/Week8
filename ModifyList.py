nums = []
user_input = input('Enter numbers: ')
while (user_input != 'exit'):

    nums.append(user_input)
    user_input = input('Enter numbers: ')
#tokens = user_input.split() # converts numbers to string

# # Convert strings to integers
# nums = []
# for token in tokens:
#      nums.append(token)
print(nums)
#
# # Print each position and number
print()
for pos, val in enumerate(nums):
    print('{}: {}'.format(pos, val))
#
# # Change negative values to 0
for pos in range(len(nums)):
   if int(nums[pos]) < 0:
         nums[pos] = 0

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' | ')
print()

nums1 = [50, 10, -5, -4, 6]

for i in range(len(nums1)):
    if nums1[i] < 0:
        nums1[i] = 0
print("nums1:", nums1)