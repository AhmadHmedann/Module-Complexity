/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  for (const num of numbers) {
    sum += num;
     product *= num;
  }
   return {
    sum: sum,
    product: product,
  };
}
// Time Complexity: O(n)
// The original implementation also had O(n) time complexity,
// but it iterated through the array twice (approximately 2n operations).
// The refactored version calculates both the sum and product in one loop,
// so it only traverses the array once (approximately n iterations).
//
// Space Complexity: O(1)
// We only store two variables regardless of the size of the input.
// Optimal Time Complexity: O(n)
// We must iterate through every element at least once
// to calculate both the sum and the product.