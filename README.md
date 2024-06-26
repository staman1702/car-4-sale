# Code Institute Portfolio Project 4

## Table of contents:
Theme, Epic and User Stories

Design and UX
- Wireframes
- Database model

Features

Future Features

Technologies

Testing

Debugging and known bugs

Deployment

Resources

Credits

Acknowledgements

Name: AutoHUB Exchange

Live link: https://pp4-django-project-ci-2fe170b1dfd9.herokuapp.com/

# Theme, Epic and User Stories
### Theme
The theme of our web page is an online marketplace that facilitates the buying and selling of used cars. Our platform aims to provide users with a convenient and efficient way to browse, buy, and sell pre-owned vehicles.

### Epic
The epic for our web page involves creating a comprehensive online marketplace for used cars. This encompasses building user-friendly interfaces for browsing listings, uploading vehicles for sale, and engaging in online discussions via comments. Key features of the epic include user authentication, enabling users to post their own sales listings, and fostering interaction through comment sections.

### User Stories
As a user, I want to:
- view a paginated list of sale posts 
- view individual sale post details
- view individual sale post comments
- register for an account
- login/logout
- add a sales post
- edit/update my sales posts 
- delete my sales posts
- add a comment
- edit/update my comments
- delete my comments
- send Site Owner collaboration request

As a site owner, I want to:
- view a paginated list of sale posts, including the not published posts
- view individual sale post details, including the not published posts
- view individual sale post comments, including the not approved comments
- edit/update/change status of all the sites posts
- edit/update/approve all the site's comments
- delete of any of the site's sale posts
- delete any of the comments

# Design and UX
The design of my webpage prioritizes user experience and accessibility. I've carefully crafted a visually appealing interface that enhances usability and navigation. By using a combination of dark text on a light background for key elements such as the navbar, footer, and landing page, I've created a striking yet easy-to-read layout. This choice ensures that users can seamlessly interact with the content without any visual strain, whether they're browsing listings, engaging in discussions, or exploring the site's features. Additionally, I've maintained consistency throughout the website by incorporating a unified color scheme, with dark and light options, to create a cohesive and polished look across all pages. With a focus on user-centric design principles, I aim to provide an immersive and enjoyable experience for all visitors to my platform.

## Wireframes
Home page

![home_page](static/images/readme_images/wireframe_1.png)


Sale Post detail

![sale_post_details](static/images/readme_images/wireframe_2.png)


New Sale Post form

![new_sale_post_form](static/images/readme_images/wireframe_4.png)


About page

![about_page](static/images/readme_images/wireframe_3.png)


Sign Up page

![sign_up](static/images/readme_images/wireframe_5.png)


## Database model
![erd](static/images/readme_images/erd.png)

# Features

Index page:
![index_page](static/images/readme_images/index.png)

Navbar:
![navbar](static/images/readme_images/navbar.png)


Index page in Mobile view:

![smaller_viewport](static/images/readme_images/smaller_viewport.png)


Also navbar in Mobile view with dropdown menu:

![navbar_small](static/images/readme_images/navbar_small.png)


Post details & comments section:

![detail_&_comments](static/images/readme_images/detail_&_comments.png)


Sign up form:

![sign_up](static/images/readme_images/sign_up.png)


Login:

![login](static/images/readme_images/login.png)


Logout:

![logout](static/images/readme_images/logout.png)


Collaboration request form:

![collaboration_request](static/images/readme_images/collaboration_request.png)


About page:

![about](static/images/readme_images/about.png)



# Future Features

- **Like and Dislike Buttons for Comments:**
Implement functionality to allow users to express their opinions on comments by adding Like and Dislike buttons. This feature will enhance user engagement and provide valuable feedback on the quality of comments.

- **Viewing the Site Owner collaboration requests:**
As a Site Owner, I want the ability to review collaboration requests without logging into the Django Admin panel.

# Technologies

Languages used:
- Python
- HTML5
- CSS
- Javascript

Frameworks, Libraries and Programs Used:
- Django/allauth (Python framework)
- Bootstrap 4
- Cloudinary -(hosting the images)
- PostgreSQL (database)
- GitHub (for hosting the site)
- Heroku (deployment of the site)
- Visual Studio Code (editing the files)

# Testing

## General
Regular testing was conducted throughout the course of this project, especially before commits to Github.

Responsive/Mobile-first design was tested using Chrome developer tools to ensure desired layout was achieved. As well as Chrome, and Firefox which successfully affirmed my project's responsiveness. To test responsiveness, the following mobiles were tested Galaxy S8+, Pixel 7, iPhone 14 Pro Max, iPad Pro. All successfully passed in mobile responsiveness of the page.

## Validator Testing
- Html was Validated using the [HTML Validator](https://validator.w3.org/).
- CSS was Validated using the [CSS Validator](https://jigsaw.w3.org/css-validator/).
- Python Validation was performed installing flake8 (command : pip install flake8) and using it (command : python -m flake8). No serious errors reported.

## Manual User Story Testing

- As a user, I want to view a paginated list of sale posts - Pass
- As a user, I want to view individual sale post details - Pass
- As a user, I want to view individual sale post comments - Pass
- As a user, I want to register for an account - Pass
- As a user, I want to login/logout - Pass
- As a user, I want to add a sales post - Pass
- As a user, I want to edit/update my sales posts - Pass
- As a user, I want to delete my sales posts - Pass
- As a user, I want to add a comment - Pass
- As a user, I want to edit/update my comments - Pass
- As a user, I want to delete my comments - Pass
- As a user, I want to send Site Owner collaboration request - Pass

- As a site owner, I want to view a paginated list of sale posts, including the not published posts - Pass
- As a site owner, I want to view individual sale post details, including the not published posts - Pass
- As a site owner, I want to view individual sale post comments, including the not approved comments - Pass
- As a site owner, I want to edit/update/change status of all of the sites posts - Pass
- As a site owner, I want to edit/update/approve all of the sites comments - Pass
- As a site owner, I want to delete of any of the sites sale posts - Pass
- As a site owner, I want to delete any of the comments - Pass

## Unit Testing
During the development of the project, I have written several unit tests for my forms and views to ensure their correctness and functionality. These tests are located in the following files:
- `sale/test_forms.py`
- `sale/test_views.py`
- `about/test_forms.py`
- `about/test_views.py`

To run the unit tests, navigate to your project directory in the terminal and execute the following command:
    ```bash
    python manage.py test
    ```
This command will run all the unit tests and provide the results. I'm pleased to report that all 23 unit tests have passed successfully.

# Debugging and known bugs

### Known Issues

#### Post Model - Car Make and Model Selection

**Issue Description:**
Initially, the desired functionality was to allow users to first choose the car's Make and then, depending on the selected Make, choose the Model of the car they are selling. However, Django does not natively support this feature in crispy forms, which made the implementation challenging.

**Original Approach:**
- The initial plan was to have the Make as a foreign key in the Post model.
- This would allow the Make to dynamically filter the available Models.

**Implemented Approach:**
- Due to the limitation in Django crispy forms, the approach was adjusted.
- Instead of using Make as a foreign key in the Post model, the Make was used as a foreign key in the Model.
- The Model was then used as a foreign key in the Post model.

**Steps to Reproduce the Issue:**
1. Attempt to create a form where the Model choices dynamically update based on the selected Make using Django crispy forms.
2. Observe that Django crispy forms do not support this functionality out-of-the-box.

**Expected Behavior:**
Users should be able to select a car Make, and based on that selection, the available car Models should be dynamically filtered and displayed.

**Impact:**
This limitation affects the user experience when using bigger database. Scrolling through numerous models to find the desired one might be exhausting for users.

**Workaround:**
By structuring the models such that:
- `Make` is a foreign key in the `Model` model.
- `Model` is then used as a foreign key in the `Post` model.

This setup ensures the relationship is maintained, albeit without the dynamic form behavior initially desired. The impact of this issue is minimized if the website focuses on the sale of only certain car makes (e.g., Japanese cars).

#### Updating Comments as Site Owner

**Bug Description:**
When editing comments as the Site Owner, the form does not prepopulate the "Approved" checkbox field. This issue means that even if a comment was previously approved, the checkbox appears unchecked when editing the comment. This can lead to accidental unapproval of comments if the checkbox is not manually checked again during the editing process.

**Steps to Reproduce:**
1. Log in as the Site Owner.
2. Navigate to the comments section.
3. Select a comment that has already been approved.
4. Click on the "Edit" button for the selected comment.
5. Observe that the "Approved" checkbox is not prepopulated (unchecked).

**Expected Behavior:**
The "Approved" checkbox should be prepopulated based on the current approval status of the comment. If the comment is already approved, the checkbox should be checked when the edit form loads.

**Impact:**
This bug can cause confusion and extra work for the Site Owner, as they must manually check the "Approved" box again for comments that were already approved. This may lead to unintentional unapproval of comments, affecting site content management.

**Workaround:**
Ensure that the "Approved" checkbox is checked manually when editing any comment that should remain approved.

# Deployment

## A. Setting Up Cloud Environments

### Heroku Setup

1. **Create a Heroku Account**:
    - Sign up for a free account on [Heroku](https://www.heroku.com/).

2. **Install Heroku CLI**:
    - Download and install the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).

3. **Log In to Heroku**:
    - Open a terminal and log in using the Heroku CLI:
    ```bash
    heroku login
    ```

4. **Create a New Heroku App**:
    - In the terminal, navigate to your project directory and create a new Heroku app:
    ```bash
    heroku create your-app-name
    ```

### Postgres Database Setup

1. **Add Heroku Postgres**:
    - Add a PostgreSQL database to your Heroku app:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```
    - Get the database URL by running:
    ```bash
    heroku config:get DATABASE_URL
    ```

### Cloudinary Setup

1. **Sign Up for Cloudinary**:
    - Sign up for a free account on [Cloudinary](https://cloudinary.com/).

2. **Get Cloudinary API Credentials**:
    - Obtain your Cloudinary API credentials from the Cloudinary dashboard.

3. **Set Cloudinary Environment Variables on Heroku**:
    - Set these credentials in your Heroku environment:
    ```bash
    heroku config:set CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dvidoipsh
    ```

### Environment Variables

1. **Set Up Other Necessary Environment Variables**:
    - Add any other necessary environment variables using the `heroku config:set` command, for example:
    ```bash
    heroku config:set SECRET_KEY=your-secret-key
    ```

### Deploying Your Application

1. **Push Your Code to Heroku**:
    - Ensure you are in the project directory and push your code to Heroku:
    ```bash
    git push heroku main
    ```

2. **Run Database Migrations** (if applicable):
    - For example, in a Django application:
    ```bash
    heroku run python manage.py migrate
    ```

## B. Getting the Code onto Your Computer

### Cloning the Repository

1. **Open a Terminal**:
    - Open a terminal or command prompt on your computer.

2. **Clone the Repository**:
    - Use the following command to clone the repository:
    ```bash
    git clone https://github.com/staman1702/car-4-sale.git
    ```
    - This will create a local copy of the repository on your computer.

### Forking the Repository

1. **Fork the Repository on GitHub**:
    - Go to the repository page on GitHub and click on the 'Fork' button. This will create a copy of the repository under your GitHub account.

2. **Clone Your Fork**:
    - Use the following command to clone your forked repository:
    ```bash
    git clone https://github.com/your-username/car-4-sale.git
    ```

### Making Updates

1. **Navigate to the Project Directory**:
    ```bash
    cd car-4-sale
    ```

2. **Create a New Branch** (optional but recommended):
    ```bash
    git checkout -b new-feature
    ```

3. **Make Your Changes**:
    -  Edit the files as needed.

### Committing and Pushing Updates

1. **Stage Changes**:
    ```bash
    git add .
    ```

2. **Commit Changes**:
    ```bash
    git commit -m "Description of the changes"
    ```

3. **Push Changes to GitHub**:
    -  If you are working on a new branch:
    ```bash
    git push origin new-feature
    ```
    -  If you are working on the main branch:
    ```bash
    git push origin main
    ```

### Additional Details on Cloning and Forking

1. Cloning:
    - When you clone a repository, your local copy is linked to the original repository.
    - Any changes you push will be submitted for approval via pull requests if you don't have direct push access to the repository.

2. Forking:
    - Forking creates a new repository under your GitHub account.
    - You can make changes independently of the original repository.
    - If the original repository updates, you can pull those changes into your fork.

## C. Automatic Deployment

- Any changes pushed to the `main` branch will automatically be deployed to the live site on Heroku.
- Ensure all changes are thoroughly tested and reviewed before merging into the `main` branch to maintain site stability.

By following these steps, you can maintain and update the site efficiently, ensuring that all necessary information is readily available for anyone who takes over the project in the future.

# Resources

- [Django 4.2 documentation](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap 4 documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Cloudinary documentation](https://cloudinary.com/documentation)
- ERD made with [Lucidchart](https://lucid.app/)
- Wireframes made with MockFlow [WireframePro](https://wireframepro.mockflow.com/)

# Credits

## Content
- Content was created and assessed by Matija Stankovic

## Media
- Images used in development are all from [Pexels](https://www.pexels.com/)

## Acknowledgments
- Completion of an app and it's features would not have been possible without the support and advice of my mentor Brian Macharia