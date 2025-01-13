#!python3

# Example of a class template and an instantiated object
import math

class argExample:
    l = 0
    w = 0
    
    def inputVals(self):
        try:
            tl = input("Enter a value for length:")
            self.l = float(tl)
            tw = input("Enter a value for width :")
            self.w = float(tw)
        except Exception as e:
            print("Those numbers are invalid. Try again.\n")
    
    def multipleArea(self,multiple):
        # generates area for a rectangle that is multiple x larger in each dimension
        temp_length = multiple * self.l
        temp_width = multiple * self.w
        temp_area = temp_length * temp_width
        return temp_area

    def __init__(self):
        self.inputVals()


if __name__ == "__main__":
    print("\n\n\n\n")
    example = argExample()
    
    multiple = 2
    print(f"The area for a rectangle that is \033[1;32;40m{multiple}\033[0;37;40m times larger in each dimension is \033[1;36;40m{example.multipleArea(multiple)}\033[0;37;40m")