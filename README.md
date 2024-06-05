Code Institute Portfolio Project 4

# Deployment Write-up

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
