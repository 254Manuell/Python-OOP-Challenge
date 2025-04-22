class Pet:
    def __init__(self, name):
        """Initialize a new pet with default attributes"""
        self.name = name
        self.hunger = 5     # Starting in the middle (0 = full, 10 = very hungry)
        self.energy = 5     # Starting in the middle (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting in the middle (0-10)
        self.tricks = []    # List to store learned tricks
        
    def eat(self):
        """Feed the pet to reduce hunger and increase happiness"""
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness but not above 10
        return f"{self.name} has eaten and is feeling better!"
        
    def sleep(self):
        """Let the pet sleep to restore energy"""
        self.energy = min(10, self.energy + 5)  # Increase energy but not above 10
        return f"{self.name} had a good nap and is now refreshed!"
        
    def play(self):
        """Play with the pet to increase happiness but consume energy and increase hunger"""
        if self.energy < 2:
            return f"{self.name} is too tired to play right now!"
        
        self.energy = max(0, self.energy - 2)  # Decrease energy but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger but not above 10
        return f"{self.name} had fun playing with you!"
        
    def get_status(self):
        """Display the current state of the pet"""
        # Define status descriptions based on attribute values
        hunger_status = "full" if self.hunger <= 2 else "hungry" if self.hunger >= 7 else "content"
        energy_status = "exhausted" if self.energy <= 2 else "energetic" if self.energy >= 7 else "normal"
        happiness_status = "sad" if self.happiness <= 2 else "ecstatic" if self.happiness >= 7 else "content"
        
        status = f"Status of {self.name}:\n"
        status += f"Hunger: {self.hunger}/10 ({hunger_status})\n"
        status += f"Energy: {self.energy}/10 ({energy_status})\n"
        status += f"Happiness: {self.happiness}/10 ({happiness_status})"
        return status
    
    def train(self, trick):
        """Teach the pet a new trick"""
        if trick in self.tricks:
            return f"{self.name} already knows how to {trick}!"
            
        if self.energy < 1 or self.happiness < 2:
            return f"{self.name} is too tired or unhappy to learn new tricks right now!"
            
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 1)  # Training takes a bit of energy
        self.happiness = min(10, self.happiness + 1)  # Learning is satisfying
        return f"{self.name} has learned to {trick}!"
        
    def show_tricks(self):
        """Display all tricks the pet has learned"""
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet!"
            
        tricks_list = ", ".join(self.tricks)
        return f"{self.name} knows the following tricks: {tricks_list}"