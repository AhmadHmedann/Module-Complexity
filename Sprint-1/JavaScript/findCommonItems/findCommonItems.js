/**
 * Finds common items between two arrays.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems2 = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))), //O(N*M)
// ];
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray); //O(M)
  const commonSet = new Set();
  for (const item of firstArray) {
    //O(N)
    if (secondSet.has(item))
      //O(1) on Ave
      commonSet.add(item); //O(1)   On Ave
  }
  return [...commonSet]; //O(K)
};
// Time Complexity: O(n + m)
// We create a Set from secondArray and loop through firstArray once.

// Original Time Complexity: O(n * m)
// includes() may search all of secondArray for every item in firstArray.

// Space Complexity: O(m + n)
// We store secondArray in a Set and up to n common items.

// Original Space Complexity: O(n)
// filter() and Set create temporary collections of up to n items.

// Optimal Time Complexity: O(n + m)
// We need to inspect both arrays to find all common items.
