users = [
    {
        "id": 1,
        "total": 100,
        "coupons": "p20",
    },
    {
        "id": 3,
        "total": 1002,
        "coupons": "p202",
    },
    {
        "id": 2,
        "total": 1001,
        "coupons": "p201",
    },
]

discounts ={
    "p20":(0.2,0),
    "p201":(0.15,50),
    "p202":(0.1,100),
}

for user in users:
    percent,fixed =discounts.get(user["coupons"],(0,0))
    discount = user['total']*percent+fixed
    print(f"User ID: {user['id']} - Original Total: Rs.{user['total']} - Discount: Rs.{discount} - Final Total: Rs.{user['total']-discount}")