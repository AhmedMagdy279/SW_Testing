import unittest
import sys
# Package1
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
# Package2
from Package2.TC_AddToCartTest import AddToCartTest
from Package2.TC_CheckOut import CheckoutTest

sys.path.append("./Package1")
sys.path.append("./Package2")
sys.path.append("./TestBase")

# Get all tests from LoginTest, SignupTest, AddToCartTest, GoToCheckoutTest
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
signup_tests = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
add_to_cart_tests = unittest.TestLoader().loadTestsFromTestCase(AddToCartTest)
go_to_checkout_tests = unittest.TestLoader().loadTestsFromTestCase(CheckoutTest)

# Create a test suite
SanityTest_suite = unittest.TestSuite([login_tests, signup_tests])
FunctionalTest_suite = unittest.TestSuite([add_to_cart_tests, go_to_checkout_tests])
MasterTest_suite = unittest.TestSuite([login_tests, signup_tests, add_to_cart_tests, go_to_checkout_tests])

# Run the test suite
unittest.TextTestRunner().run(SanityTest_suite)
# unittest.TextTestRunner().run(FunctionalTest_suite)
# unittest.TextTestRunner(verbosity=2).run(MasterTest_suite)

