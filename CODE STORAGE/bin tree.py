class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def Print_in(self):
        if self.left:
            self.left.Print_in()
        print(self.value, end=' ')
        if self.right:
            self.right.Print_in()

    def Print_pre(self):
        print(self.value, end=' ')
        if self.left:
            self.left.Print_pre()
        if self.right:
            self.right.Print_pre()

    def Print_post(self):
        if self.left:
            self.left.Print_post()
        if self.right:
            self.right.Print_post()
        print(self.value, end=' ')

    def Add(self, num):
        while True:
            if num < self.value:
                if self.left:
                    self = self.left
                else:
                    self.left = Tree(num)
                    return

            elif num > self.value:
                if self.right:
                    self = self.right
                else:
                    self.right = Tree(num)
                    return
            else:
                return

    def Get_hight(self):
        if not self.left is None and not self.right is None:
            return 1 + max(self.left.Get_hight(), self.right.Get_hight())
        elif not self.left is None:
            return 1 + self.left.Get_hight()
        elif not self.right is None:
            return 1 + self.right.Get_hight()
        else:
            return 1

    def In_tree(self, num):
        while True:
            if num == self.value:
                print('Yes')
                return
            elif num < self.value:
                if self.left:
                    self = self.left
                else:
                    print('No')
                    return
            elif num > self.value:
                if self.right:
                    self = self.right
                else:
                    print('No')
                    return

    def Min(self):
        while self.left:
            self = self.left
        print(self.value)

    def Max(self):
        while self.right:
            self = self.right
        print(self.value)


a = [6, 8, 3, 6, 8, -99, 3, -12]
t = Tree(a[0])
for i in a[1:]:
    t.Add(i)

for i in a + [1, -1, 6, 4, 3, 5, 0]:
    t.In_tree(i)
t.Print_in()
print()
t.Print_pre()
print()
t.Print_post()

t.Max()
t.Min()
print(t.Get_hight())
