# Lab 1

# Leader Array
def findLeaders(arr):
  leaders = []
  max_right = arr[-1]

  for i in range(len(arr)-1, -1, -1):
    if arr[i] >= max_right:
      leaders.append(arr[i])
      max_right = arr[i]

  return leaders[::-1]  

# Alternating Sort  
def alternateSort(arr):
  arr.sort()
  
  result = []
  left, right = 0, len(arr)-1
  
  while left <= right:
    result.append(arr[left])
    left += 1
    
    if left <= right:
      result.append(arr[right])
      right -= 1

  return result

# Lab 2 

# Triplet Sum
def tripletSum(arr, target):
  triplets = []
  arr.sort()

  for i in range(len(arr)-2):
    left, right = i+1, len(arr)-1
    
    while left < right:
      curr_sum = arr[i] + arr[left] + arr[right]
      if curr_sum == target:
        triplets.append([arr[i], arr[left], arr[right]])
        left += 1
        right -= 1
      elif curr_sum < target:
        left += 1  
      else:
        right -= 1
        
  return triplets

# Sort Array
def sortArray(arr):
  count = [0] * (max(arr)+1)

  for el in arr:
    count[el] += 1

  output = []
  for num in range(len(count)):
    output.extend([num] * count[num])

  return output

# Lab 3

# Remove Duplicates
def removeDuplicates(head):
  curr = head
  while curr:
    while curr.next and curr.val == curr.next.val:
      curr.next = curr.next.next      
    curr = curr.next
  return head

# Check Loop
def hasLoop(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  
  return False

# Maximum Sum Subarray
import sys
def maxSubArraySum(arr):
  max_so_far = -sys.maxsize
  max_ending_here = 0

  for num in arr:
    max_ending_here += num
    max_so_far = max(max_so_far, max_ending_here) 
    if max_ending_here < 0:
      max_ending_here = 0  

  return max_so_far

# Lab 4

# Diagonal Interchange
def diagonalInterchange(mat):
  n = len(mat)

  for i in range(n):
    mat[i][i], mat[n-1-i][i] = mat[n-1-i][i], mat[i][i]

  return mat

# Index Finder  
def findIndices(arr, x):
  indices = []
  for i in range(len(arr)):
    if arr[i] == x:
      indices.append(i)

  return indices

# Lab 5

# Rows with Max 1s
def maxOnesRows(mat):
  max_count, max_rows = 0, []

  for row in mat:
    ones_count = row.count(1)
    if ones_count > max_count:
      max_count = ones_count
      max_rows = [row]
    elif ones_count == max_count:
      max_rows.append(row)

  return max_rows

# Middle Row/Col Sum  
def findMiddleSum(mat):
  n = len(mat)

  mid_row = mat[n//2]
  row_sum = sum(mid_row)

  col_sum = 0
  for i in range(n):
    col_sum += mat[i][n//2]

  return (row_sum, col_sum)

# Lab 6

# Matrix Sort
def sortMatrix(mat):
  return sorted(mat, key=lambda row: sorted(row))

# Diagonal Replace  
def replaceDiagonal(mat):
  n = len(mat)

  for i in range(n):
    for j in range(n):
      if i == j or i == n-j-1:
        mat[i][j] = 0

  return mat

# Lab 7

# BST Search
def searchBST(root, val):
  if not root or root.val == val:
    return root
  
  if val < root.val:
    return searchBST(root.left, val)
  else: 
    return searchBST(root.right, val)

# Leaf Nodes Sum 
def leafSum(root):
  if not root:
    return 0
  if not root.left and not root.right:
    return root.val
  
  return leafSum(root.left) + leafSum(root.right)
  
# Zigzag Traversal
def zigzagTraversal(root):
  result = []
  queue = [root]
  leftToRight = True

  while queue:
    currLevel = []
    for i in range(len(queue)):
      node = queue.pop(0)
      currLevel.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    if not leftToRight:
      currLevel.reverse()
    result.append(currLevel)
    leftToRight = not leftToRight

  return result
