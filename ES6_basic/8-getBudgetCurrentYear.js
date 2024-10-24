function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  [income] = income;
  [gdp] = gdp;
  [capita] = capita;

  return budget;
}
