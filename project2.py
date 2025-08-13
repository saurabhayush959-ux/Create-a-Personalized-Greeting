
def greet_user():
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    
    full_name = first_name + " " + last_name
    
   
    print(f"Hello, {full_name}! Welcome!")


if __name__ == "__main__":
    greet_user()
