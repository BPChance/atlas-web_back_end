export default function appendToEachArrayValue(array, appendString) {
  const NewArray = [];

  for (const value of array) {
    NewArray[i] = appendString + value;
    i += 1;
  }

  return array;
}
