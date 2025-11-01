from core.economics import check_cashout_eligibility

def format_currency(val):
    return f"${val:,.4f}"

def format_num(val):
    return f"{val:,.2f}"

def check_cashout(credit_amount, ccs_score, cashout_limits, request_amount, is_premium=False):
    ok, reason = check_cashout_eligibility(
        credit_amount,
        ccs_score,
        cashout_limits,
        request_amount,
        is_premium=is_premium
    )
    return ok, reason
