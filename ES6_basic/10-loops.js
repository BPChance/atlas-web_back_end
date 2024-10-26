export default function appendToEachArrayValue(array, appendString) {
  const NewArray = [];

  let i = 0;
  for (const value of array) {
    NewArray[i] = appendString + value;
    i += 1;
  }

  return NewArray;
}
