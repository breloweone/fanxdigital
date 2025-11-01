DEFAULT_WEIGHTS = {
    "WATCH": 1.0,      # video izleme
    "SHARE": 2.0,      # paylaşım / repost
    "MESSAGE": 1.2,    # mesaj / etkileşim
    "UPLOAD": 3.0,     # içerik yükleme
    "CREATE": 5.0,     # orijinal eser/NFT üretimi
    "EVENT": 4.0,      # canlı / etkinlik katılımı
    "INVITE": 2.0,     # davet
}

DEFAULT_PARAMS = {
    "daily_cap": 10000,
    "weekly_cap": 50000,
    "R_conv": 0.1,
    "users_active": 100000,

    "ratios": {
        "fan": 0.40,
        "creator": 0.30,
        "dao": 0.20,
        "platform": 0.10,
    },

    "cashout_limits": {
        "daily": 100,
        "weekly": 500,
        "monthly": 2000,
        "premium_monthly": 5000,
        "requires_ccs": 80,
    },

    "burn_rates": {
        "watch": 0.005,
        "share": 0.005,
        "message": 0.01,
        "upload": 0.02,
        "create": 0.03,
        "sponsor": 0.05,
        "cashout": 0.05,
    },
}
