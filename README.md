# Django Quiz Application

This is a simple quiz application built with Django that allows a single user to answer multiple-choice questions and view their results at the end of the quiz.

## Features

- Start a new quiz session
- Answer multiple-choice questions
- View results including total questions answered, correct answers, and incorrect answers

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package installer)
- Django 3.x or higher

## Installation

Follow these steps to install and run the application:

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/rupesh-singh02/quiz-app.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd quiz-app
   ```

3. **Set Up the Database**

   Run migrations to set up the database:

   ```bash
   python manage.py makemigrations quiz
   python manage.py migrate
   ```

4. **Create a Superuser**

   If you want to add questions through the Django admin interface, create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**

   Start the development server:

   ```bash
   python manage.py runserver
   ```

9. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000/quiz/start/` to start a new quiz session.

## Adding Questions

To add questions to the quiz, access the Django admin interface by navigating to `http://127.0.0.1:8000/admin` in your web browser. Log in with your superuser credentials and add questions under the "Questions" model.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation for guidance on building web applications.
- Inspiration from various online quiz platforms.