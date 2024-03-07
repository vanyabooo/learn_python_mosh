has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan!")

# and == both conditions are true
# or == at least one condition is true
# not == inverse any boolean value

if has_high_income or not has_good_credit:
    print("has high income or does not have good credit.")
    