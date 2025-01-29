# Shopping Assistant

## Overview
The **Shopping Assistant** project is a web-based application designed to enhance online shopping experiences through web scraping, chatbot assistance, and wishlist management. Built using Django, Celery, Redis, and TailwindCSS, this project provides real-time price tracking, automated notifications, and a chatbot interface.

## Features
- **Web Scraper**: Extracts product details from various e-commerce platforms.
- **Chatbot Integration**: Assists users in finding and comparing products.
- **Wishlist Management**: Allows users to save and track favorite items.
- **Task Scheduling**: Uses Celery and Redis for background task processing.
- **Responsive UI**: Built with TailwindCSS for a modern look and feel.

## Frameworks & Technologies Used
- **Django**: Backend framework for handling web requests and database operations.
- **Celery & Redis**: Implements asynchronous task execution and job scheduling.
- **BeautifulSoup & Selenium**: Web scraping tools for extracting product details.
- **Gunicorn**: WSGI server for deploying the application.
- **TailwindCSS**: For styling and responsive design.

## Why It’s Useful
This project simplifies the online shopping experience by automating price tracking, providing chatbot assistance, and organizing user wishlists. It is beneficial for frequent shoppers, researchers, and businesses monitoring e-commerce trends.


## Installation & Setup
### Prerequisites
- Python 3.11+
- Redis (for Celery background tasks)
- Virtual environment (recommended)

### Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-repo/shopping-assistant.git
   cd shopping-assistant
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

6. **Start Celery worker** (Requires Redis running)
   ```sh
   celery -A webscrapper worker --loglevel=info
   ```

## Usage
- **Access the application**: Open `http://127.0.0.1:8000/` in your browser.
- **Use the chatbot**: Navigate to the chatbot page to get product suggestions.
- **Manage wishlists**: Save items for future tracking.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

