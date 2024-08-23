# Amazon Website Testing Project

## Project Setup

1. **Create Virtual Environment**
   - Use Bash to create a virtual environment for Python 3.12:
     ```bash
     python3.12 -m venv venv
     ```

2. **Install Dependencies**
   - Install the necessary dependencies (pytest, selenium, openpyxl) within the virtual environment:
     ```bash
     source venv/bin/activate
     pip install pytest selenium openpyxl
     ```

3. **Set Up Project in PyCharm**
   - Open PyCharm IDE.
   - Create a new project in the directory using the virtual environment interpreter.

## Task 1: Test Scenarios

### Scenario 1: Search and Add to Cart

1. **Open Amazon Website**
   - Navigate to [Amazon](https://www.amazon.com/).

2. **Search for 'Car Accessories'**
   - Type "car accessories" in the search bar and press Enter.

3. **Select the First Item**
   - Click on the first item in the search results.

4. **Add Item to Cart**
   - Click on the "Add to Cart" button.

5. **Verify Item in Cart**
   - Go to the cart and check that the item is added successfully.

### Scenario 2: Filter and Add to Cart from Today's Deals

1. **Open Today's Deals**
   - Navigate to the "Today's Deals" section from the homepage.

2. **Apply Filters**
   - From the left side filters, select "Headphones" and "Grocery".
   - From the discount section, choose "10% off or more".

3. **Navigate to Fourth Page**
   - Go to the fourth page of the filtered results.

4. **Select and Add Item to Cart**
   - Select any item from the fourth page and add it to the cart.

## Test Cases

### Scenario 1

- **TC_01**: Search for 'car accessories' on the homepage.
- **TC_02**: Add the first item to the cart from the 'car accessories' search results.
- **TC_03**: Verify the item added from the 'car accessories' search results is the same as the one in the cart.

### Scenario 2

- **TC_01**: Navigate to the 'Today's Deals' page from the homepage.
- **TC_02**: Apply filters "Headphones", "Grocery", and "10% off or more" successfully.
- **TC_03**: In the 'Today's Deals' page, apply the filters and navigate to the fourth page, then select any item and add it to the cart.
