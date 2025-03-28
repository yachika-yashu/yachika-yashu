
# Dockerized Flask Application 

## Overview
Application for Sentiment Analysis and Named Entity Recognition
This Flask application provides functionalities for user registration, login, sentiment analysis (SA), and named entity recognition (NER). It uses a database for storing user information and integrates with external APIs for performing SA and NER.

## Features

### User Authentication
- **Registration**: Users can register by providing their name, email, and password.
- **Login**: Registered users can log in using their email and password.
- **Session Management**: User sessions are managed to ensure secure access to protected routes.

### Sentiment Analysis (SA)
- **Perform Sentiment Analysis**: Users can input text to analyze its sentiment using an external API.
- **View Results**: The sentiment analysis results are displayed on the SA page.

### Named Entity Recognition (NER)
- **Perform Named Entity Recognition**: Users can input text to identify named entities using an external API.
- **View Results**: The NER results are displayed on the NER page.

## Routes

- `/`: Displays the login page.
- `/register`: Displays the registration page.
- `/perform_registration`: Handles user registration.
- `/perform_login`: Handles user login.
- `/profile`: Displays the user profile page (protected route).
- `/ner`: Displays the NER input page (protected route).
- `/perform_ner`: Handles NER requests and displays results (protected route).
- `/sa`: Displays the SA input page (protected route).
- `/perform_sa`: Handles SA requests and displays results (protected route).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t flask-app .
   ```

3. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 flask-app
   ```

## Configuration

- **Session Management**:
  ```python
  app.config['SESSION_TYPE'] = 'memcached'
  app.config['SECRET_KEY'] = 'super secret key'
  ```

## Usage

1. **Register**: Navigate to `/register` to create a new account.
2. **Login**: Navigate to `/` to log in with your credentials.
3. **Profile**: Access your profile at `/profile`.
4. **NER**: Navigate to `/ner` to perform named entity recognition.
5. **SA**: Navigate to `/sa` to perform sentiment analysis.

## Dependencies

- Flask
- Requests
- Database module (`db`)
- External API module (`api`)

