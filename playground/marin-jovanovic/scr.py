class P:
    def r(self):
        print("not impl")

class A(P):

    def __str__(self):
        return "create single"

    def r(self):
        print("a call")

class B(P):

    def __str__(self):
        return "select username"

    def r(self):
        print("b call")


legal_actions = {
    "a": A(),
    "b": B()
}


legal_actions["a"].r()

config = 			{
    "create single":True,
    "select username":True,
}

print(config)



# t = legal_actions["a"]
# print("t", t)