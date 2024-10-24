function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  [income] = income;
  [gdp] = gdp;
  [capita] = capita;

  return budget;
}
