# Backend and API Automation testing project

*Project not finished yet*

Project progress:
1) using bash to create virtual environment for both python 3.12 & python 2.7.
2) install dependancies that we're gonna use in the project (requests, pytest, pymysql) for both venv.
3) use PyCharm IDE to create our project in this directory using our venv interpreter.
4) I wanna use WordPress to create a dummy store website to test it. To do so we need to test on a local server and to manage the database where our WordPress site's data.
5) for local server environment I had two choices: MAMP and Local WP. I am going to use Local WP.
	- Create new site named 'Store project'. 
	- Use Database credentials from the project in the next step.
6) for database management I am going to use MySQL Workbench.
	- Use Local WP database credentials to create and test a new connection.
	- Create new schema
7) install and activate woocommerce plugin through clicking on WP admin in Local WP.
8) add samples to the store using either WP importer (xml files) or WooCommerce products (CSV files)