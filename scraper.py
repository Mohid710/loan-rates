# scraper.py
# Simple and Accurate Loan Calculator for GitHub

def conventional_loan(principal, annual_rate, months):
    """
    Reducing balance method for conventional bank loans
    Returns EMI, total interest, and month-wise breakdown
    """
    r = annual_rate / 100 / 12  # monthly interest rate
    emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
    remaining = principal
    total_interest = 0
    breakdown = []

    for month in range(1, months + 1):
        interest_month = remaining * r
        principal_month = emi - interest_month
        remaining -= principal_month
        total_interest += interest_month
        breakdown.append({
            "Month": month,
            "Principal Paid": round(principal_month, 2),
            "Interest Paid": round(interest_month, 2),
            "Remaining Principal": round(max(remaining, 0), 2)
        })

    return round(emi, 2), round(total_interest, 2), breakdown


def islamic_loan_flat(principal, annual_rate, months):
    """
    Islamic bank - Flat Rate Loan
    """
    total_profit = principal * annual_rate / 100 * (months / 12)
    emi = (principal + total_profit) / months
    return round(emi, 2), round(total_profit, 2)


def islamic_loan_diminishing(principal, annual_rate, months):
    """
    Islamic bank - Diminishing Balance Loan
    """
    return conventional_loan(principal, annual_rate, months)


# --------------------------
# Example Usage
# --------------------------
if __name__ == "__main__":
    principal = 100000   # Loan amount
    months = 12          # Loan tenure

    # Conventional Loan
    emi_conv, total_interest, breakdown_conv = conventional_loan(principal, 12, months)
    print("Conventional Bank Loan:")
    print(f"Monthly EMI: {emi_conv} | Total Interest: {total_interest}")
    print("Month-wise Breakdown (first 3 months):", breakdown_conv[:3])

    # Islamic Loan - Flat
    emi_flat, total_profit_flat = islamic_loan_flat(principal, 10, months)
    print("\nIslamic Bank Loan (Flat Rate):")
    print(f"Monthly EMI: {emi_flat} | Total Profit: {total_profit_flat}")

    # Islamic Loan - Diminishing
    emi_dim, total_profit_dim, breakdown_dim = islamic_loan_diminishing(principal, 10, months)
    print("\nIslamic Bank Loan (Diminishing Balance):")
    print(f"Monthly EMI: {emi_dim} | Total Profit: {total_profit_dim}")
    print("Month-wise Breakdown (first 3 months):", breakdown_dim[:3])
