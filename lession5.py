class a:
    num = 1


class b:
    num = 2


class c(a, b):
    name = "c"


class d(b, a):
    name = "d"


print(c().num)
print(d().num)


# 类多重继承时的重名属性继承原则：就近原则

class atm:
    """
    atm类
    """

    info = """
请输入数字执行对应的功能：
1——查询余额
2——存款
3——取款
4——退出    
"""

    def __init__(self, left=0):
        self.left = left

    def menu(self):
        while True:
            cmd = self.input_cmd()
            if cmd == 1:
                self.query_left()
            elif cmd == 2:
                self.deposit()
            elif cmd == 3:
                self.withdraw()
            elif cmd == 4:
                print("退出成功")
                break
            else:
                print("请输入合法指令")

    def query_left(self):
        # 查询余额
        print("余额为：{}".format(self.left))

    def deposit(self):
        # 存款
        money = self.input_money(True)
        if money <= 0:
            print("数额必须大于0")
        else:
            self.left += money
            print("存款成功，余额为：{}".format(self.left))

    def withdraw(self):
        # 取款
        money = self.input_money(False)
        if money <= 0:
            print("数额必须大于0")
        elif money > self.left:
            print("余额不足")
        else:
            self.left -= money
            print(f"取款成功，余额为{self.left}")

    @staticmethod
    def input_cmd():
        # 输入指令：是合法数字则返回其值，否则返回-1
        try:
            cmd = int(input(atm.info))
            return cmd
        except Exception:
            print("请输入正确的数字格式")
            return -1

    @staticmethod
    def input_money(is_deposit):
        # 输入金额，是有效数字则返回其值，否则返回-1
        action = "取款"
        if is_deposit:
            action = "存款"
        try:
            money = int(input(f"请输入{action}数额:"))
            return money
        except Exception:
            print("请输入正确的数字格式", Exception.args)
            return -1


# atm test code
atm(1000).menu()


class Lijing:
    """李靖类"""

    def __init__(self, name, weapons=[], power=10):
        self.name = name
        self.weapons = weapons
        self.power = power

    def count_fight(self, weapon, weapon_power):
        self.weapons.append(weapon)
        self.power += weapon_power


class nezha(Lijing):
    """哪吒类"""

    def __init__(self, name, weapons=["混天绫", "乾坤圈"], power=50):
        Lijing.__init__(self, name, weapons, power)

    def resetWeapons(self, weapons=[], power=10):
        self.weapons = weapons
        self.power = power

    def __str__(self):
        return repr(self.weapons) + "---" + str(self.power)


lijing = Lijing("李靖")
print(lijing.weapons)
lijing.count_fight("七宝玲珑塔", 50)
print(lijing.power)

nezha = nezha("哪吒")
print(nezha)
nezha.resetWeapons(["金箍棒"], 1000)
print(nezha)
