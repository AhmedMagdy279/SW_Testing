import unittest
import sys

from TestCases.TC_LoginTest import LoginTest
from TestCases.TC_SignupTest import SignupTest
from TestCases.TC_AddToCartTest import AddToCartTest
from TestCases.TC_CheckOut import CheckoutTest

sys.path.append("./TestCases")

# Get all tests from LoginTest, SignupTest, AddToCartTest, GoToCheckoutTest
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
signup_tests = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
add_to_cart_tests = unittest.TestLoader().loadTestsFromTestCase(AddToCartTest)
go_to_checkout_tests = unittest.TestLoader().loadTestsFromTestCase(CheckoutTest)

# Create a test suite
SanityTest_suite = unittest.TestSuite([signup_tests, login_tests])
FunctionalTest_suite = unittest.TestSuite([add_to_cart_tests, go_to_checkout_tests])
MasterTest_suite = unittest.TestSuite([login_tests, signup_tests, add_to_cart_tests, go_to_checkout_tests])

# Run the test suite
unittest.TextTestRunner().run(SanityTest_suite)
# unittest.TextTestRunner().run(FunctionalTest_suite)
# unittest.TextTestRunner(verbosity=2).run(MasterTest_suite)

