# Django Event Management System

A web-based Event Management System developed using **Python and Django**. The application allows users to register, log in, manage their profiles through a dashboard, and upload CSV files related to different events.

## Features

- **User Registration:** New users can create an account.
- **User Login:** Secure login using username and password.
- **Dashboard:** Displays user information and uploaded event history.
- **Event Category Selection:** Choose from four event categories:
  - Hackathon
  - Workshop
  - Internship
  - Orientation
- **CSV File Upload:** Upload CSV files related to selected events.
- **Event Date:** Select the date of the event.
- **Upload History:** View previously uploaded event details.
- **File Validation:** Allows CSV files up to 5 MB and rejects empty or unsupported files.
- **User Authentication:** Only logged-in users can access the dashboard and upload functionality.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Web page structure |
| CSS3 | Styling and design |
| SQLite | Database |
| Git & GitHub | Version control |

## Project Structure

```text
Django-Event-Management/
│
├── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── events/
│   ├── migrations/
│   ├── templates/events/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── accounts/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/SayaliGangurde48/Django-Event-Management.git
```

### 2. Navigate to the Project Directory

```bash
cd Django-Event-Management
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and add your Django secret key:

```env
DJANGO_SECRET_KEY=your-secret-key
```

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

Visit:

```text
http://127.0.0.1:8000/
```

## Application Workflow

1. Open the website.
2. Register a new user account.
3. Log in using the registered credentials.
4. Access the user dashboard.
5. Select the **Upload Event** option.
6. Choose an event category.
7. Select the event date.
8. Upload the CSV file.
9. Submit the form.
10. View the uploaded event details in the dashboard.

## Future Enhancements

- CSV data preview before uploading.
- Download uploaded CSV files.
- Search and filter event records.
- Admin dashboard for managing user uploads.
- Improved data visualization and reporting.

## Author

**Sayali Gangurde**

B.Tech – Computer Science and Engineering

## GitHub Repository

[ Django Event Management System – GitHub](https://github.com/SayaliGangurde48/Django-Event-Management)

---

*Developed as a Django Web Development Project.*
