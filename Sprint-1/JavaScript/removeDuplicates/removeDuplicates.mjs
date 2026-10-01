/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
// export function removeDuplicates(inputSequence) {
//   const uniqueItems = [];

//   for (
//     let currentIndex = 0;
//     currentIndex < inputSequence.length;
//     currentIndex++
//   ) {
//     let isDuplicate = false;
//     for (
//       let compareIndex = 0;
//       compareIndex < uniqueItems.length;
//       compareIndex++
//     ) {
//       if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
//         isDuplicate = true;
//         break;
//       }
//     }
//     if (!isDuplicate) {
//       uniqueItems.push(inputSequence[currentIndex]);
//     }
//   }

//   return uniqueItems;
// }

export function removeDuplicates(inputSequence) {

  return [...new Set(inputSequence)];  //O(N+N)
}

// Original Time Complexity: O(n * k), worst case O(n^2)
// For each item, the code may scan all uniqueItems to check for duplicates.

// Time Complexity: O(n)
// Creating the Set processes each item once, and spreading it back to an array is also O(n).

// Space Complexity: O(n)
// The Set and returned array can store up to n unique items.

// Optimal Time Complexity: O(n)
// We must inspect every element at least once to remove duplicates.