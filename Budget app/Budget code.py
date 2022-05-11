class Category:

def create_spend_chart(categories):
  def truncate(n)
      multiplier = 10
      return int(n * multiplier) / multiplier

  def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
      breakdown.append(category.get_withdrawals())
  rounded = list(map(lambda x: truncate(x/total), breakdown))
  return rounded

def create_spend_chart(categories):
  """
    create_spend_chart that takes a list of categories as an         argument. It should return a string that is a bar chart
    """
    res = "percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
          cat_spaces = " "
          for total in totals:
              if total * 100 >= i:
                cat spaces += "0 "
              else:
                cat_spaces += " "
           res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
           i-=10
  dashes = "-" + 