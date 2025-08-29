class BusinessTycoon:
    """A class representing a business tycoon with various attributes and methods."""
    
    def __init__(self, name, industry, net_worth, companies_owned=[]):
        # Public attributes
        self.name = name
        self.industry = industry
        
        # Protected attribute (convention: single underscore)
        self._companies_owned = companies_owned
        
        # Private attribute (name mangling: double underscore)
        self.__net_worth = net_worth
        self.__secret_wealth = net_worth * 0.1  # Hidden wealth not shown publicly
    
    # Public method
    def display_profile(self):
        """Display the tycoon's public profile"""
        print(f"\n=== {self.name} ===")
        print(f"Industry: {self.industry}")
        print(f"Net Worth: ${self.__net_worth:,.2f}")
        print(f"Companies Owned: {', '.join(self._companies_owned) if self._companies_owned else 'None'}")
    
    # Protected method
    def _acquire_company(self, company_name, acquisition_cost):
        """Acquire a new company (internal business operation)"""
        self._companies_owned.append(company_name)
        self.__net_worth -= acquisition_cost
        print(f"{self.name} acquired {company_name} for ${acquisition_cost:,.2f}")
    
    # Private method
    def __calculate_taxes(self):
        """Calculate taxes (private financial matter)"""
        return self.__net_orth * 0.15
    
    # Getter method for encapsulated attribute
    def get_net_worth(self):
        """Get the current net worth"""
        return self.__net_worth
    
    # Setter method for encapsulated attribute
    def set_net_worth(self, value):
        """Set net worth with validation"""
        if value >= 0:
            self.__net_worth = value
        else:
            print("Net worth cannot be negative!")
    
    # Property for encapsulated access
    @property
    def secret_wealth(self):
        """Read-only property for secret wealth"""
        return self.__secret_wealth
    
    def make_business_deal(self, deal_amount, success_probability=0.8):
        """Simulate a business deal with chance of success"""
        import random
        if random.random() < success_probability:
            self.__net_worth += deal_amount
            print(f"✅ Deal successful! Gained ${deal_amount:,.2f}")
            return True
        else:
            self.__net_worth -= deal_amount * 0.5
            print(f"❌ Deal failed! Lost ${deal_amount * 0.5:,.2f}")
            return False


# Inheritance: Tech Tycoon specializes Business Tycoon
class TechTycoon(BusinessTycoon):
    """A specialized tycoon in the technology industry"""
    
    def __init__(self, name, net_worth, companies_owned=[], tech_specialty="Software"):
        # Call parent constructor
        super().__init__(name, "Technology", net_worth, companies_owned)
        self.tech_specialty = tech_specialty
        self.__patents = []  # Private to TechTycoon
    
    # Polymorphism: Override display method
    def display_profile(self):
        """Display tech tycoon's specialized profile"""
        super().display_profile()
        print(f"Tech Specialty: {self.tech_specialty}")
        print(f"Patents Held: {len(self.__patents)}")
    
    # Unique method for TechTycoon
    def file_patent(self, patent_name, cost):
        """File a new patent"""
        if cost <= self.get_net_worth():
            self.__patents.append(patent_name)
            self.set_net_worth(self.get_net_worth() - cost)
            print(f"📝 Patent filed: {patent_name}")
        else:
            print("Insufficient funds to file patent!")
    
    def innovate(self):
        """Tech tycoon's special innovation ability"""
        innovation_value = self.get_net_worth() * 0.05
        self.set_net_worth(self.get_net_worth() + innovation_value)
        print(f"💡 Innovation boosted net worth by ${innovation_value:,.2f}")


# Inheritance: RealEstateTycoon specializes BusinessTycoon
class RealEstateTycoon(BusinessTycoon):
    """A specialized tycoon in real estate"""
    
    def __init__(self, name, net_worth, companies_owned=[]):
        super().__init__(name, "Real Estate", net_worth, companies_owned)
        self.__properties_owned = []  # Private to RealEstateTycoon
    
    # Polymorphism: Override display method
    def display_profile(self):
        """Display real estate tycoon's specialized profile"""
        super().display_profile()
        print(f"Properties Owned: {len(self.__properties_owned)}")
    
    # Unique method for RealEstateTycoon
    def purchase_property(self, property_name, property_value):
        """Purchase a new property"""
        if property_value <= self.get_net_worth():
            self.__properties_owned.append(property_name)
            self.set_net_worth(self.get_net_worth() - property_value)
            print(f"🏢 Purchased {property_name} for ${property_value:,.2f}")
        else:
            print("Insufficient funds to purchase property!")
    
    def market_boom(self):
        """Real estate market boom effect"""
        boom_value = self.get_net_worth() * 0.15
        self.set_net_worth(self.get_net_worth() + boom_value)
        print(f"📈 Market boom! Net worth increased by ${boom_value:,.2f}")


# Demonstration
if __name__ == "__main__":
    print("=== BUSINESS TYCOON SIMULATION ===\n")
    
    # Create different types of tycoons
    elon = TechTycoon("Elon Musk", 200000000000, ["Tesla", "SpaceX", "Twitter"], "Space Technology")
    donald = RealEstateTycoon("Donald Trump", 3200000000, ["The Trump Organization"])
    
    # Display initial profiles
    elon.display_profile()
    donald.display_profile()
    
    # Demonstrate unique abilities
    print("\n--- Business Activities ---")
    elon.innovate()
    elon.file_patent("Neural Interface", 50000000)
    
    donald.purchase_property("Trump Tower", 500000000)
    donald.market_boom()
    
    # Make business deals
    print("\n--- Business Deals ---")
    elon.make_business_deal(1000000000, 0.7)
    donald.make_business_deal(500000000, 0.6)
    
    # Show updated profiles
    print("\n--- Updated Profiles ---")
    elon.display_profile()
    donald.display_profile()
    
    # Demonstrate encapsulation - trying to access private attributes
    print(f"\nElon's public net worth: ${elon.get_net_worth():,.2f}")
    # print(elon.__net_worth)  # This would cause an AttributeError
    print(f"Elon's secret wealth: ${elon.secret_wealth:,.2f} (read-only property)")