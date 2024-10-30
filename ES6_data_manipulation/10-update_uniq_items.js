function updateUniqueItems(groceriesMap) {
  if (!(groceriesMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  groceriesMap.forEach((quantity, item) => {
    if (quantity === 1) {
      groceriesMap.set(item, 100);
    }
  });

  return groceriesMap;
}

export default updateUniqueItems;
