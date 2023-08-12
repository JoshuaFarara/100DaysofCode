'''

Here we are going to see how we can rotate array
There are two types of array rotations, left and right. Each rotation type can have a rotation by a specific amount of position.
Essentially a rotation on the chosen axis of the array is the shift of the elements based on the position. 
Example:
    Left Roatation by 2:
    arr =   [1, 2, 3, 4, 5, 6]
    arrL =  [3, 4, 5, 6, 1, 2]

    Right Rotation by 2:
    arr =   [1, 2, 3, 4, 5, 6]
    arrR =  [5, 6, 1, 2, 3, 4]
'''

'''
When you're thinking about rotating an array and planning the design and structure of your program, here's a step-by-step approach to help you:

1.Understand the Problem:

Clearly understand the problem statement and requirements.
Are you rotating the array to the left or right? 
By how many positions? Is the rotation cyclic (meaning you might rotate multiple times)?

2. Choose a Rotation Strategy:

Decide on the rotation strategy you want to use: reversal, using extra space, or a combination of techniques. 
The given code snippet uses the reversal technique, which is efficient in terms of time complexity and doesn't require additional space.

3. Identify Sub-operations:

Break down the rotation process into sub-operations. 
For example, with the reversal technique, you'll reverse the entire array and then reverse individual sub-arrays based on the rotation count.

4. Write Pseudocode:

Write pseudocode outlining the steps of your algorithm. 
Focus on high-level logic and describe each sub-operation. 
This helps you organize your thoughts before diving into actual code.

5. Design Functions:

Design functions for each sub-operation.
In the given code snippet, there are two main functions: reverse(start, end, arr) and left_rotate_array(arr, size, d). 
These functions help modularize the code and make it more readable.

6. Plan for Indices and Looping:

Decide how you will handle array indices and looping. 
The reverse function in the code snippet uses index manipulation and a loop to reverse portions of the array. 
Make sure you understand how indices change during rotations.

7.Error Handling and Edge Cases:

Consider edge cases such as empty arrays, arrays with fewer elements than the rotation count, or when the rotation count is larger than the array size. 
Plan how your program will handle these cases.

8. Write Code Incrementally:

Start by implementing each function separately and testing it thoroughly. 
For example, first, implement the reverse function and test it with different inputs. 
Then, move on to the left_rotate_array function and test it with various rotation counts.

9. Test Extensively:

Test your solution with a variety of test cases, including normal cases, edge cases, and corner cases. 
Make sure your program produces the expected output for each test.

10.Optimize and Refactor:

After your program is working correctly, consider optimizing it for efficiency if needed. 
Look for ways to reduce redundancy or improve time/space complexity.

11. Document Your Code:

Add comments to your code explaining the purpose of each function and any complex logic. 
This makes your code more understandable to others (and to your future self).

12.Consider Time and Space Complexity:

Evaluate the time and space complexity of your solution. 
The reversal technique used in the given code snippet has a time complexity of O(n) and doesn't require extra space, which makes it efficient.

'''

def reverse(start , end, arr):

    # No of iterations needed for reversing the list
    no_of_reverse = end-start+1

    #
    count = 0
    while((no_of_reverse)) // 2 != count:
        pass


arr =   [1, 2, 3, 4, 5, 6]
print(arr)
arr.reverse()
print(arr)
