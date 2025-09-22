# scraper.py
# Loan Calculator Module for Conventional and Islamic Banks

def conventional_loan(principal, annual_rate, months):
    """
    Calculates EMI and total interest for conventional bank (reducing balance method)
    """
    r = annual_rate / 100 / 12  # monthly interest rate
    emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
    total_payment = emi * months
    total_interest = total_payment - principal
    return round(emi, 2), round(total_interest, 2)


def islamic_loan(principal, annual_rate, months, method='flat'):
    """
    Calculates EMI and total profit for Islamic bank
    method: 'flat' or 'diminishing'
    """
    years = months / 12
    if method == 'flat':
        total_profit = principal * annual_rate / 100 * years
        emi = (principal + total_profit) / months
    elif method == 'diminishing':
        # monthly reducing balance method
        r = annual_rate / 100 / 12
        emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
        total_payment = emi * months
        total_profit = total_payment - principal
    else:
        raise ValueError("Invalid method: choose 'flat' or 'diminishing'")
    
    return round(emi, 2), round(total_profit, 2)


# --------------------------
# Example Usage (for testing)
# --------------------------
if __name__ == "__main__":
    principal = 100000           # Loan amount
    months = 12                  # Loan tenure in months

    # Conventional Bank
    emi_conv, total_interest = conventional_loan(principal, 12, months)
    print("Conventional Bank Loan:")
    print(f"Monthly EMI: {emi_conv} | Total Interest: {total_interest}")

    # Islamic Bank - Flat Rate
    emi_flat, total_profit_flat = islamic_loan(principal, 10, months, method='flat')
    print("\nIslamic Bank Loan (Flat Rate):")
    print(f"Monthly EMI: {emi_flat} | Total Profit: {total_profit_flat}")

    # Islamic Bank - Diminishing Balance
    emi_dim, total_profit_dim = islamic_loan(principal, 10, months, method='diminishing')
    print("\nIslamic Bank Loan (Diminishing Balance):")
    print(f"Monthly EMI: {emi_dim} | Total Profit: {total_profit_dim}")
