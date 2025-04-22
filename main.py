from pet import Pet

def main():
    # Creating a new pet instance
    my_pet = Pet("Buddy")
    print(f"Welcome to your new digital pet, {my_pet.name}!")
    
    # Testing basic functionality
    print(my_pet.get_status())
    print("\n" + my_pet.eat())
    print(my_pet.play())
    print(my_pet.sleep())
    
    # Check updated status
    print("\n" + my_pet.get_status())
    
    # Testing the bonus functionality
    print("\n" + my_pet.train("sit"))
    print(my_pet.train("roll over"))
    print(my_pet.train("fetch"))
    print(my_pet.show_tricks())
    
    # Pushing the pet's limits
    print("\nLet's play a lot and see what happens:")
    for _ in range(4):
        print(my_pet.play())
    
    print("\n" + my_pet.get_status())
    print(my_pet.train("jump"))  # Should fail due to low energy

if __name__ == "__main__":
    main()