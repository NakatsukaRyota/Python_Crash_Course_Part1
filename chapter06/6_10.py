numbers = {"ryota": [2, 5],
        "yako": [7, 5],
        "coco": [8, 5],
        "reo": [1, 14],
        "admin": [10, 100],
}

for name, nums in numbers.items():
    print(f"{name.title()}の好きな数字")
    for num in nums:
        print(f"\t{num}")
