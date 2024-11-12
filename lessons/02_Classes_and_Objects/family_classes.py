# Run Me!

class Person:
    """Person represents a person in our system."""

     # This is the initializer, it gets run when we create a new object
    def __init__(self, first_name: str, last_name: str, age: int):
        """Initializes a new Person object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        print(f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old. {message}")
        
        
class Parent(Person):
    """Parent represents a parent in our system."""

    def __init__(self, first_name: str, last_name: str, age: int, spouse=None, children: list = None):
        """Initializes a new Parent object."""
        super().__init__(first_name, last_name, age) # Call Person.__init__ to initialize the name and age attributes
        self.children = []
        
        # Set our spouse but also set the spouse's spouse to us
        if spouse:
            self.spouse = spouse
            spouse.spouse = self
        else:
            self.spouse = None

    def add_child(self, child: Person):
        """Adds a child to the parent's list of children."""
        self.children.append(child)
        

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        
        super().say_hello(message)
        if self.spouse:
            print(f"My spouse is {self.spouse.first_name}")
            
        print(f"I have {len(self.children)} children.")

        if len(self.children) > 0:
            print("Their names are:")
            for child in self.children:
                print(f"  {child.first_name} {child.age}")
                
                
class Child(Person):
    """Child represents a child in our system."""

    def __init__(self, first_name: str, last_name: str, age: int, parents: list = None):
        """Initializes a new Child object."""
        super().__init__(first_name, last_name, age)  # Call Person.__init__ to initialize the name and age attributes
        self.parents = parents if parents is not None else []
        
        # Automatically add this child to each parent's list of children
        for parent in self.parents:
            parent.add_child(self)

    # def __init__(self, first_name: str, last_name: str, age: int, parents: list = None):
    #     """Initializes a new Child object."""
    #     super().__init__(first_name, last_name, age)  # Call Person.__init__ to initialize the name and age attributes
    #     #self.parents = parents
    #     if parents:
    #         self.parents = parents
    #         parents.append(self)
    #         Parent.children.append(self)

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        super().say_hello(message)
        print(f"My parents are {', '.join([parent.first_name for parent in self.parents])}")



       
        
        
# Now lets make a family
mom = Parent("Alice","Stumpf", 35)
dad = Parent("Bob","Stumpf", 40, mom)

charlie = Child("Charlie","Stumpf", 10, [mom, dad])
dahlia = Child("Dahlia","Stumpf", 8, [mom, dad])

# Connect the children to the parents
# mom.add_child(charlie)
# mom.add_child(dahlia)
# dad.add_child(charlie)
# dad.add_child(dahlia)


mom.say_hello("Hello!") # Call the say_hello method of the mom object
print()
dahlia.say_hello("Yo!")