# method or func

# 3 types of method
# instance method(default)
# class method
# static method

class myclass:
    def instance_method(self,a,b):# instance method
        print(f"self:{self}")# self represent obj
        print("this is instance method", a,b)

    @classmethod
    def class_method(cls, a,b):
        print(f"cls:{cls}")# repr class name#<class '__main__.myclass'>
        print("this is class method", a,b)

    @staticmethod
    def static_method(a,b):
        print("this is static method",a,b)

########obj
# obj=myclass()
#