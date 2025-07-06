## OOPs
"""
Obejct oriented programming
"""


# Inheritance
"""
Code Reuseability
"""


class Parent:
    color = "black"
    blood = "O+"


class Child(Parent):  # Child inherit parent
    blood = "A+"  # Overriding
    pass


class Parent:
    def __init__(self):
        self.color = "black"
        self.blood = "O+"


class Child(Parent):  # Child inherit parent
    # here the init method override the parent class and the color varible we cannt aces from instance
    def __init__(self):
        super().__init__()  # Super user to access the parent class
        self.blood = "A+"  # Overriding


class Parent:
    def __init__(self):
        self.color = "black"
        self.blood = "O+"


class sibling:
    def __init__(self):
        self.color = "black"
        self.blood = "O+"


class Child(Parent, sibling):  # Multiple inheritance
    def __init__(self):
        super().__init__()  # Super user to access the parent class
        self.blood = "A+"  # Overriding


Parent.blood
Child.blood  # no property in child still accessing for variable because extends


# Polymorphism
"""
Many forms
Same function name but differnt apprach
"""


class Parent:
    def __init__(self):
        self.color = "black"
        self.blood = "O+"

    def move(args):
        "Moving fast"


class Child(Parent):
    def __init__(self):
        self.blood = "A+"

    # Execute same function in both class with differnt features
    def move(args):
        "Moving slowly"


Parent.move()  # moveing fast
Child.move()  # moving slowly

# Encapsulation
"""
Wrapping data into single unit
class is an example
Acces modiifer to use hide data 
    -> private , Public , Protected

    private only acesbel in the class
    public from any where 
    protected from. class and subclasses

"""


class Parent:
    def __init__(self):
        self.__color = "black"  # __ means its a private property cant access outside
        self._blood = "O+"  # _ means its a protected class

    def move(args):
        "Moving fast"


class Child(Parent):
    def __init__(self):
        self.blood = "A+"

    def move(args):
        "Moving slowly"
