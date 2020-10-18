def is_ok(num):
    if num[:3] == "555":
        return "YES"
    else:
        return "NO"


n = input()
print(is_ok(n))