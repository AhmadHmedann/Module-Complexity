/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
// export function hasPairWithSum2(numbers, target) {
//   for (let i = 0; i < numbers.length; i++) {
//     for (let j = i + 1; j < numbers.length; j++) {
//       if (numbers[i] + numbers[j] === target) {
//         return true;
//       }
//     }
//   }
//   return false;
// }
// Time Complexity: O(N^2)
// Space Complexity: O(1)
// Optimal Time Complexity: O(N)

export function hasPairWithSum(numbers, target) {
  const seen = new Set();
  for (const num of numbers) {
    const needed = target - num;
    if (seen.has(needed)) return true;

    seen.add(num);
  }

  return false;
}
// Original Time Complexity: O(n^2)
//two nested loop compare each number with remaining numbers

// Time Complexity: O(n)
// we iterate through the arr once and Set.has() for O(1) lookup

// Space Complexity: O(n)
// We may store up to n numbers in the Set.
// Optimal Time Complexity: O(n)
//we might need to inspect every number at least once.
