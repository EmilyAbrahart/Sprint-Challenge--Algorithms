#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
The time complexity of the outer loop is O(n^3) whilst the inner function increases a by n^2 each time. We can therefore divide O(n^3) by O(n^2) which gives us an overall runtime complexity of O(n).

b) O(n log n)
The outer loop has a runtime complexity of O(n) as it cycles through all of the n items. The inner loop has a time complexity of O(log n) as the value of j is doubled each time.
The overall runtime complexity would therefore be O(n) \* O(log n) which is O(n log n).

c) O(n)
This has a runtime of O(n) as the function recurses through the number of bunnies (n), reducing by 1 each time until the base case of 0 is met.

## Exercise II

Goal: To find the lowest floor at which eggs break, f.

Using a binary search, you would test by initially dropping the egg from the middle floor (n // 2).

- If the egg breaks, check the floor below to determine whether or not the egg breaks there. If it does not, you have found floor f.

  - If an egg dropped from the floor below breaks, you know that floor if is in the lower half of the building and would then find the middle floor in the lower half ((n - (n // 2)) // 2) and continue this method until you find floor f.

- If the egg does not break from the first floor tried, you know that floor f must be in the upper half of the building and so would find the middle floor of the upper half (n - (n // 4)) and repeat this process until you find floor f.

The runtime of the search would be O(log n) because you are halving the range of n each time.
