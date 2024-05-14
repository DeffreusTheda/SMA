class CapitalExpenditure {
  class BalanceSheet {
    Asset asset;
    Liability liability;
    Equity equity;
  }
}

class RevenueExpenditure {
  /* Expenses is similar to 'gaji' */
  Profit profit;
  class IncomeStatement {
    abstract CostOfGoods {
      COGS costOfGoodsSold;
      COGM costOfGoodsManufacturing;
    }
    Expenses expenses;
  }
}

Type classify(int usageSpanInYear, Asset asset) {
  if (usageSpanInYear >= 1 && asset.isFixed()) {
    return CapitalExpenditure
  } else if (usageSpanInYear < 1) {
    return RevenueExpenditure
  O
}

