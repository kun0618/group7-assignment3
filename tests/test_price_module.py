import unittest
from app.price_module import PricingModule  

class TestPricingModule(unittest.TestCase):
    def test_initialization(self):
        """Test that the PricingModule can be instantiated."""
        pricing_module = PricingModule()
        self.assertIsInstance(pricing_module, PricingModule)

if __name__ == '__main__':
    unittest.main()
