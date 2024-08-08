# In this case, we use the _ because we know we're not going to use the "last" variable. We can use _ anytime we know we're not going to use the variable
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
