Projects
The projects are hosted on the web and you can access the links to the projects are provided below:

Cookie Tracker (Part 1)
Slideshow (Part 2)
Electic (Part 3)
Electic (Part 4)
Cookie Tracker (Part 1)
Description
Following is my description of the assignment project and requirements:

The task at hand is to develop a Python and Django web application that utilizes a persistent cookie to track the number of times a client's computer visits a specific page. Alongside the visit count, the application should also display the client computer's IP address and determine the time zone in which the client computer is located. By implementing these features, the application will effectively track visits, provide IP address information, and offer insights into the time zone of the client's computer.
Analysis and Design
Analysis:

The goal of the application is to track the number of times a client computer visits a page using a persistent cookie, display the IP address of the client computer, and determine the time zone of the client computer.
Design:

Backend (Django):
Set up a Django project and create an application within the project.
Define a Django view that handles the page the client visits.
Retrieve the client's IP address using the request object.
Check if a persistent cookie exists on the client's computer to track the number of visits.
If the cookie exists, retrieve the visit count; otherwise, set the visit count to 1 and create a new persistent cookie.
Update the visit count in the cookie and send it back to the client.
Frontend (JavaScript and Bootstrap):
Use JavaScript to retrieve the client's time zone abbreviation.
Format the time zone abbreviation and display it on the page.
Style the HTML elements using Bootstrap to enhance the visual appearance.
Templates (HTML):
Create an HTML template that renders the necessary information, including the visit count, IP address, and time zone.
Incorporate Bootstrap classes to style the elements and ensure a responsive design.
By following this analysis and design, you can develop a web application that tracks visits using a persistent cookie, displays the client's IP address, and captures the time zone of the client computer. The Django backend will handle the logic of managing the cookie, while JavaScript and Bootstrap will enhance the frontend experience.

File structure and details
manage.py: This file is the command-line utility for managing the Django project. It allows you to run development servers, perform database migrations, and execute other administrative tasks.
part1/: This directory is the Django application package. It contains the main files and configuration for the application.
__init__.py: This empty file marks the 'part2' directory as a Python package.
settings.py: This file contains the configuration settings for the Django project, including database settings, static and media file locations, installed applications, and more.
urls.py: This file defines the URL routing for the Django project. It maps URL patterns to views in the application.
views.py: This file contains the views (logic) for the application. It defines functions or classes that handle HTTP requests and return HTTP responses.
templates/: This directory contains HTML template files used for rendering the views. In this case, the 'part1/' subdirectory contains the 'cookie.html' template file, which represents the main page of the application.
./shared This file contains the main.css which contains the styling for this page
Guide to run the app:
Prerequisites:
Ensure you have Python installed on your machine. You can download it from the official Python website (https://www.python.org/downloads/) and follow the installation instructions.
Setup:
Download or clone the project files to your local machine.
Open a terminal or command prompt and navigate to the project's directory.
Installation:
Create a virtual environment by running the command: python -m venv venv
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install the required dependencies by running: pip install -r requirements.txt
Run database migrations by executing: python manage.py migrate
Running the Application:
Start the Django development server by running the command: python manage.py runserver
Open a web browser and visit http://localhost:8000 to access the web application.
Using the Application:
Upon accessing the web application, you will see the "Cookie Tracker" page.
The page will display the number of visits, IP address, and time zone of the client computer.
Each time you refresh the page, the visit count will increase, and the information will be updated.
The time zone will be automatically detected based on the client computer's settings.
Additional Information:
To stop the development server, press Ctrl + C in the terminal or command prompt where the server is running.
Remember to deactivate the virtual environment once you are finished using the application by running the command deactivate.
That's it! You have now set up, run, and can use the web application. The application will track the number of visits using a persistent cookie, display the client's IP address, and show the time zone of the client computer. Enjoy exploring the functionality of the web application!

Slideshow (Part 2)
Description
Following is my description of the assignment project and requirements:

The app requires the development of a slideshow using Django and JavaScript. It needs to display a collection of images along with their descriptions. Users should be able to navigate through the images, control the slideshow's progression, and switch between random and sequential modes. The app should provide an engaging and interactive user experience while showcasing the images and their accompanying information.
Analysis and Design
Analysis:

The app is a slideshow that displays images stored in a database along with their descriptions.
The slideshow has features like forward and back navigation, random and sequential modes, and start/stop functionality.
The app needs to fetch image data from the Django backend and update the slideshow dynamically using JavaScript.
Design:

Frontend:
The frontend will be implemented using HTML, CSS, and JavaScript.
The main HTML file, let's call it "slideshow.html," will contain the slideshow container, image element, and control buttons.
CSS will be used for styling the page, including the layout, colors, and animations.
JavaScript will handle the dynamic behavior of the slideshow, such as fetching image data, updating the display, and responding to user interactions.
Django Backend:
The backend will be implemented using Django, a Python web framework.
The app will have a Django model for storing image details like name, URL, description, and ID.
The model will be connected to a database, such as SQLite or PostgreSQL, to persist the image data.
Django views and URLs will be set up to handle requests for image data and download endpoints.
The backend will provide an API to fetch image metadata and download the image blob.
JavaScript Implementation:
JavaScript will be used to fetch image metadata and download the image blob from the Django backend.
The JavaScript code will use Fetch API or Axios library to make HTTP requests to the backend API endpoints.
The response data will be processed and used to update the slideshow display.
Event listeners will be set up to handle user interactions, such as button clicks for navigation and mode switching.
JavaScript will handle the slideshow logic, including transitioning between images, starting/stopping the slideshow, and switching between random and sequential modes.
Integration:
The Django app will serve the "slideshow.html" file as a template, rendering the dynamic parts using Django's template engine.
The JavaScript code will be included in the HTML file or linked externally using a <script> tag.
The Django backend API endpoints will be called from JavaScript to fetch image data.
By following this analysis and design, you can implement a Django app with a slideshow functionality that fetches image data from the backend and displays it using JavaScript.

File structure and details
manage.py: This file is the command-line utility for managing the Django project. It allows you to run development servers, perform database migrations, and execute other administrative tasks.
part2/: This directory is the Django application package. It contains the main files and configuration for the application.
__init__.py: This empty file marks the 'part2' directory as a Python package.
settings.py: This file contains the configuration settings for the Django project, including database settings, static and media file locations, installed applications, and more.
urls.py: This file defines the URL routing for the Django project. It maps URL patterns to views in the application.
views.py: This file contains the views (logic) for the application. It defines functions or classes that handle HTTP requests and return HTTP responses.
templates/: This directory contains HTML template files used for rendering the views. In this case, the 'part2/' subdirectory contains the 'slideshow.html' template file, which represents the main page of the application.
models.py: This files contains the database setup with all the info on the table and its elements.
./shared This file contains the main.css which contains the styling for this page
Database Design
The models.py code defines a Django app with a single model called Image. This model represents an image stored in the database and has the following fields:

name (CharField): Stores the name of the image with a maximum length of 500 characters.
url (URLField): Stores the URL of the image with a maximum length of 500 characters.
description (CharField): Stores the description of the image with a maximum length of 500 characters.
The Image model also includes a __str__ method, which returns a string representation of the image object in the format "name: {name}, url: {url}, description: {description}".

This database design allows for the storage of multiple images, each with a unique name, URL, and description.


Guide to run the app:
Prerequisites:
Ensure you have Python installed on your machine. You can download it from the official Python website (https://www.python.org/downloads/) and follow the installation instructions.
Setup:
Download or clone the project files to your local machine.
Open a terminal or command prompt and navigate to the project's directory.
Installation:
Create a virtual environment by running the command: python -m venv venv
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install the required dependencies by running: pip install -r requirements.txt
Run database migrations by executing: python manage.py migrate
Running the Application:
Start the Django development server by running the command: python manage.py runserver
Open a web browser and visit http://localhost:8000 to access the web application.
Using the Application:
Upon accessing the web application, you will see the "Cookie Tracker" page.
The page will display the number of visits, IP address, and time zone of the client computer.
Each time you refresh the page, the visit count will increase, and the information will be updated.
The time zone will be automatically detected based on the client computer's settings.
Additional Information:
To stop the development server, press Ctrl + C in the terminal or command prompt where the server is running.
Remember to deactivate the virtual environment once you are finished using the application by running the command deactivate.
That's it! You have now set up, run, and can use the web application. The application will track the number of visits using a persistent cookie, display the client's IP address, and show the time zone of the client computer. Enjoy exploring the functionality of the web application!

Dataflow
In this dataflow diagram, the user interacts with the slideshow controls on the user interface (HTML page).
The JavaScript code running in the browser receives the user's actions and sends HTTP requests to the Django backend API.
The Django backend receives the HTTP requests and processes them. It fetches the required image data from the database, which stores the images' information.
The backend then generates the appropriate response, which contains the image data or any other necessary information.
The response is sent back to the JavaScript code, which receives and processes it. The JavaScript code updates the user interface accordingly, displaying the requested image or performing any other required actions.
The dataflow shows the flow of data and interactions between the different components of the slideshow app, including the user interface, JavaScript, Django backend, and the database.

Electic (Part 3)
Remarks
I talked to Professor Harris and showed him my medical report approved by the accessibility and he said that I can be accomodated on this assignment. We discussed that I will complete Part 3 and submit as is because I was on a deadline by my home university and my medical condition doesnt allow me to spend extensive amount of time on this. I have already spent a lot of time on this assignment. I am writing my final exam on monday so i had to submit this before that. I did complete some of part 4 stuff in part3 such as implementing a database and fetching all the components and PCs from the database to show that I did know the content.
Description
Following is my description of the assignment project and requirements:

This app requires us to create a platform like Canada Computers or Apple. Users should be able to view all the different components available to build thier PCs or they can choose from already built PCs. The users have the option to change the components on the builtin PCs and the price should be adjusted accordingly. The website should have a proper logo, welcome page, about section, contact page and feedback form. The users should be able to buy the PCs and we have to show proper order summary and order pages. Proper images should be used to display items.
Store Findings
Here are my store findings:

I looked at the Apple and Canada Computers websites. These two websites guided me to create this app. The inspirations I took from canada computers were about how to separately display the components of the computers and the computers separately. The components had a whole different section where we can browse whatever components we like from a specific category. We can look at their pictures and their prices and all the information regarding them. On the other hand, the Apple website guided me on how to create the computer section. When you select a laptop on Apple website, you can literally replace each component with a more upgraded option or you can even downgrade. The price of the laptop changes accordingly. SO combining these two ideas, I will create an app with components listed separately from the computers and once we select a computer, we can customize its components and then buy it. I have attached screenshots of Canada computers and Apple website.
   
Interface designs
   
Analysis and Design
Note: To make up for part 4, I have already implemented a databse which contains, component information and computer information. All the PC components and computers can be added or editted from the database directly. The database also takes care of the cart items. Items are added to the cart and once the order is processed the items are displayed on the screen.

Analysis:
Users should be able to browse and view a wide range of computer components available for building their own PCs.
Users should have the option to choose from pre-built PCs and customize the components according to their preferences.
The website should have a professional logo and a visually appealing design.
Users should be able to access information about the company through the About section.
A contact page should be available for users to reach out for inquiries or support.
A feedback form should be provided to gather user feedback and improve the platform.
Users should be able to add components or pre-built PCs to a cart for later purchase.
The website should display proper order summaries with the selected components.
Design:
Architecture:
The app will follow a client-server architecture.
The client-side will be implemented as a web application using HTML, CSS, JavaScript, and Bootstrap for UI components.
The server-side will be developed using Django, a Python web framework, to handle routing, data management, and user authentication.
The server-side will utilize Django's ORM for interacting with the database.
A database management system like SQLite or PostgreSQL will be used to store component data, user information, and order details.
User Interface Design:
The website will have a clean and responsive user interface using Bootstrap components for consistency and responsiveness.
The homepage will feature the company logo and a visually appealing layout.
Navigation menus will be provided for easy access to different sections of the website.
Components and pre-built PCs will be displayed with proper images, names, descriptions, and prices. All of this will be fetched from the database.
Users will be able to filter components based on categories, brands, and other relevant criteria.
Pre-built PCs will be showcased with detailed specifications and the option to customize components.
Users will be able to add components or pre-built PCs to a cart for later purchase.
The cart page will display the selected components and provide an order summary.
Backend Development:
The server-side will be developed using Django, a Python web framework.
Django's built-in authentication system will be utilized for user registration, login, and user account management.
Django models will be created to represent components, pre-built PCs, user carts, and order summaries.
Views and URL routing will be implemented to handle requests and render appropriate templates.
Data from the database will be retrieved using Django's ORM and passed to the templates for rendering.
Frontend Development:
HTML templates will be created using Django's template engine, integrating with Bootstrap for consistent styling and responsiveness.
CSS and JavaScript will be used to enhance the user interface and provide interactive features.
Forms will be implemented for user input, such as the feedback form and customization options for pre-built PCs.
AJAX or JavaScript will be used to handle dynamic interactions like adding components to the cart without refreshing the page.
Order Management:
An order management system will be implemented on the server-side using Django models.
When a user proceeds to checkout, an order summary will be created and stored in the database.
Users can view their order summaries on the website.
Email notifications can be sent to users with the order details for confirmation.
Testing and Deployment:
Thorough testing will be conducted to ensure the functionality and usability of the platform.
Automated testing frameworks like Django's testing tools can be used for unit testing.
The app will be deployed on a web server using a suitable hosting service or a self-hosted environment.
Deployment considerations will include configuring the web server, setting up the production database, and ensuring proper security measures are in place.
By following this analysis and design, the Electic Platform will provide users with a user-friendly interface for browsing components, customizing pre-built PCs, and adding items to a cart. The platform will enable users to create order summaries and facilitate efficient order management.

Database Design
Component Model:
The Component model represents a computer component.
It has the following fields:
name (CharField): The name of the component (max length: 100 characters).
category (CharField): The category of the component. It uses choices defined in the CATEGORY_CHOICES list.
price (DecimalField): The price of the component (max digits: 8, decimal places: 2, default: 0.00).
image_url (URLField): The URL of the component's image (default: a Google image URL).
This model does not have any primary key defined explicitly. Django will automatically create an id field as the primary key.
The Component model has a __str__ method that returns the name of the component.
Computer Model:
The Computer model represents a pre-built computer.
It has the following fields:
name (CharField): The name of the computer (max length: 100 characters).
components (ManyToManyField): A many-to-many relationship with the Component model. It allows a computer to have multiple components and a component to be used in multiple computers.
image_url (URLField): The URL of the computer's image (default: a Google image URL).
This model does not have any primary key defined explicitly. Django will automatically create an id field as the primary key.
The Computer model has a total_price property that calculates the total price of the computer by summing the prices of its components and adding 200.
The Computer model also has a __str__ method that returns the name of the computer.
CartItem Model:
The CartItem model represents an item in the user's cart.
It has the following fields:
computer (ForeignKey): A foreign key relationship with the Computer model. It specifies that a cart item is associated with a specific computer.
user (ForeignKey): A foreign key relationship with the Django's built-in User model. It specifies that a cart item is associated with a specific user.
created_at (DateTimeField): The date and time when the cart item was created (auto-generated when the cart item is created).
This model does not have any primary key defined explicitly. Django will automatically create an id field as the primary key.
The CartItem model has a __str__ method that returns a string representation of the cart item containing the username of the user and the name of the computer.
Overall, these models define the structure of the database tables needed for the computer component e-commerce platform. The Component and Computer models represent the components and pre-built computers, respectively, while the CartItem model represents the items in the user's cart. The relationships between the models are established using foreign keys and many-to-many relationships.


Guide to run the app
Prerequisites:
Ensure you have Python installed on your machine. You can download it from the official Python website (https://www.python.org/downloads/) and follow the installation instructions.
Setup:
Download or clone the project files to your local machine.
Open a terminal or command prompt and navigate to the project's directory.
Installation:
Create a virtual environment by running the command: python -m venv venv
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install the required dependencies by running: pip install -r requirements.txt
Run database migrations by executing: python manage.py migrate
Running the Application:
Start the Django development server by running the command: python manage.py runserver
Open a web browser and visit http://localhost:8000 to access the web application.
Using the Application:
Upon accessing the web application, you will see the "Cookie Tracker" page.
The page will display the number of visits, IP address, and time zone of the client computer.
Each time you refresh the page, the visit count will increase, and the information will be updated.
The time zone will be automatically detected based on the client computer's settings.
Additional Information:
To stop the development server, press Ctrl + C in the terminal or command prompt where the server is running.
Remember to deactivate the virtual environment once you are finished using the application by running the command deactivate.
That's it! You have now set up, run, and can use the web application. The application will track the number of visits using a persistent cookie, display the client's IP address, and show the time zone of the client computer. Enjoy exploring the functionality of the web application!

Dataflow
Right now I dont have the User registration feature implemented as mentioned earlier that I will not be doing Part 4 after discussing with Professor Harris. The Dataflow right now would be like this:

SQL Statements
The proper way to add data to this database would be using django commands but the Sql Statements for the Computer, Component model are as follows:

Django Commands
Import the necessary models and any other dependencies:
from myapp.models import Component, Computer
Create a new instance of the model with the desired data:
Create a new Component instance
component1 = Component(name='Hard Drive', category='HDD', price=100.00, image_url='https://example.com/hdd_image.jpg')
component2 = Component(name='Memory', category='RAM', price=50.00, image_url='https://example.com/ram_image.jpg')
Create a new Computer instance
computer = Computer(name='Gaming PC', image_url='https://example.com/gaming_pc_image.jpg')
Save the instances to the database using the save() method:
Save the Component instances
component1.save()
component2.save()
Save the Computer instance
computer.save()
If you have a many-to-many relationship between models, you can add related objects using the related field:
Assuming component1 and component2 are already saved in the database
computer.components.add(component1, component2)
Optionally, you can access and modify related objects through the reverse relationship:
Assuming a computer instance with ID 1
components = computer.component_set.all() # Retrieve all components associated with the computer
Modify the related objects
for component in components:
component.price += 10 # Increase the price of each component by 10
component.save()
File structure and details
manage.py: This file is the command-line utility for managing the Django project. It allows you to run development servers, perform database migrations, and execute other administrative tasks.
part3/: This directory is the Django application package. It contains the main files and configuration for the application.
__init__.py: This empty file marks the 'part2' directory as a Python package.
settings.py: This file contains the configuration settings for the Django project, including database settings, static and media file locations, installed applications, and more.
urls.py: This file defines the URL routing for the Django project. It maps URL patterns to views in the application.
views.py: This file contains the views (logic) for the application. It defines functions or classes that handle HTTP requests and return HTTP responses.
templates/: This directory contains HTML template files used for rendering the views. In this case, the 'part2/' subdirectory contains the 'slideshow.html' template file, which represents the main page of the application.
models.py: This files contains the database setup with all the info on the table and its elements.
./shared This file contains the main.css which contains the styling for this page
