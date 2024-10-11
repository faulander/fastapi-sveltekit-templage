# Application Template

This project is a template for a web application consisting of a **FastAPI** backend and a **SvelteKit** frontend. It provides a user authentication system with email and password login, as well as token-based authentication. The frontend is styled using **TailwindCSS** and includes login and registration pages.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
    - [Backend](#backend)
    - [Frontend](#frontend)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Backend**:
  - User authentication with email and password.
  - Token-based authentication using JWT (JSON Web Tokens).
  - Database ORM with [PeeWee](https://github.com/coleifer/peewee)
  - CORS middleware setup to accept data from the Sveltekit Application.

- **Frontend**:
  - Login and registration pages.
  - Responsive design using TailwindCSS.

- **Database**:
  - SQLite Database which will be saved in /shared.

## Technologies

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Frontend**: [SvelteKit](https://kit.svelte.dev/) - A framework for building web applications using Svelte, with features for routing, server-side rendering, and more.
- **Styling**: [TailwindCSS](https://tailwindcss.com/) - A utility-first CSS framework for rapid UI development.

## Installation

Follow the steps below to download the template and set up the project for local development.

### Download the Project

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/faulander/fastapi-sveltekit-templage.git
   cd fastapi-sveltekit-template
   ```

2. Ensure you have [Python 3.12+](https://www.python.org/downloads/) and [Node.js 18+](https://nodejs.org/) installed on your computer.

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   (I highly recommend using uv instead of pip/poetry etc.)

4. Create a `.env` file in the backend directory and configure the following environment variables:
    ```SECRET_KEY=
    ACCESS_TOKEN_EXPIRE_MINUTES =
    ```

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

## Running the Application

### Start the Backend

From the backend directory, run the FastAPI application:
```bash
python main.py
```

- The application will be available at `http://localhost:8000`.

### Start the Frontend

From the frontend directory, start the SvelteKit application:
```bash
npm run dev
```

- The application will be available at `http://localhost:5173`.

## Usage

1. Navigate to the frontend URL in your browser (`http://localhost:5173`).
2. Use the login and registration pages to create accounts and log in.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests to enhance the application's functionality or improve the documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
