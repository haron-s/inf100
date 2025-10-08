from pathlib import Path
import json
# This is a script that use Python to calculate monthly cost of a loan.

# Input
json_file = "loan_details.json"
content = Path(json_file).read_text(encoding="utf-8")
data = json.loads(content)

house_price = data["house_price"]
deductible = data["deductible"]
years = data["years"]
yearly_interest_rate_pct = data["yearly_interest_rate_pct"]
monthly_fee = data["monthly_fee"]


# Computation
loan = house_price - deductible
months = years * 12

yearly_rate = yearly_interest_rate_pct / 100
monthly_rate = yearly_rate / 12

discount_factor = (1 - (1 + monthly_rate) ** -months) / monthly_rate
monthly_term_amount = loan / discount_factor + monthly_fee
monthly_term_amount = round(monthly_term_amount, 2)


# Output
print(f'Monthly term amount: {monthly_term_amount}')
