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
        if self.left and self.right:
            return 1 + max(self.left.Get_hight(), self.right.Get_hight())
        elif self.left:
            return 1 + self.left.Get_hight()
        elif self.right:
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

    def Sec_max(self):
        if self.right:
            while self.right.right:
                self = self.right
            if self.right.left:
                self = self.right.left
                while self.right:
                    self = self.right

            print(self.value)
        else:
            self = self.left
            while self.right:
                self = self.right
            print(self.value)

    def Count_elements(self):
        if self.left and self.right:
            return 1 + self.left.Count_elements() + self.right.Count_elements()
        elif self.left:
            return 1 + self.left.Count_elements()
        elif self.right:
            return 1 + self.right.Count_elements()
        else:
            return 1

    def All_leaves(self):
        if self.left and self.right:
            return self.left.All_leaves() + self.right.All_leaves()
        elif self.left:
            return self.left.All_leaves()
        elif self.right:
            return self.right.All_leaves()
        else:
            return f'{self.value}\n'

    def Is_ballansed(self):
        if self.left and self.right:
            is_true = abs(self.left.Get_hight() - self.right.Get_hight()) <= 1
            is_true = is_true and self.left.Is_ballansed() and self.right.Is_ballansed()
        elif self.left:
            is_true = self.left.Get_hight() <= 1
        elif self.right:
            is_true = self.right.Get_hight() <= 1
        else:
            is_true = True
        return is_true


