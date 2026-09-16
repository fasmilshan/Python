def outer():
    def inner():
        print("Helloo You are In!")
    print("Heeeyyy Its Out!")
    inner()

outer()