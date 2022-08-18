def implementAPI(logs: list[str]) -> list[str]:
    account = {}
    login = set()
    res = []

    for each in logs:
        commend = each.split()
        if commend[0] == "register":
            if commend[1] in account:
                res += ["Username already exists"]
            else:
                account[commend[1]] = commend[2]
                res += ["Registered Successfully"]
        elif commend[0] == "login":
            if commend[1] in account:
                if commend[1] in login:
                    res += ["Login Unsuccessfully"]
                else:
                    if commend[2] == account[commend[1]]:
                        login.add(commend[1])
                        res += ["Logged in Successfully"]
                    else:
                        res += ["Log in Unsuccessfully"]
            else:
                res += ["Log in Unsuccessfully"]
        elif commend[0] == "logout":
            if commend[1] in account:
                if commend[1] in login:
                    login.remove(commend[1])
                    res += ["Logged Out Successfully"]
                else:
                    res += ["Logout Unsuccessfully"]

            else:
                res += ["Logout Unsuccessfully"]
            
            
    return res


log = []
log += ["register david david123"]
log += ["register adam 1Adam1"]
log += ["login david david123"]
log += ["register adam david123"]
log += ["login adam 1adam1"]
log += ["login david david123"]
log += ["logout david"]
log += ["logout david"]
res = implementAPI(log)
print(res)
