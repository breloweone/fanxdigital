def legal_flags(
    transferable=False,
    kyc_enabled=True,
    cashout_limits_active=True,
    cashout_requires_contribution=True,
    creator_keeps_rights=True,
    fan_gets_license_only=True,
):
    """Basit hukuki etiket seti döndürür."""
    return {
        "SPK": "kapsam dışı" if cashout_requires_contribution else "riskli",
        "MASAK": "uyumlu" if (kyc_enabled and cashout_limits_active) else "riskli",
        "MiCA": "non-transferable utility credit" if not transferable else "transferable / risk",
        "FSEK": "Creator mali hak sahibi, fan lisanslı kullanıcı"
                if (creator_keeps_rights and fan_gets_license_only)
                else "riskli",
        "TBK_393": "cashout = hizmet bedeli iadesi",
    }
