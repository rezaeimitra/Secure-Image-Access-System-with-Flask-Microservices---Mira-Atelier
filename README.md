# Secure Image Access System

Developed a secure, modular web application to manage and access user-uploaded images based on unique access codes. The system consists of a Flask-based gateway API, an independent image processing microservice, and a MySQL database for user validation. Designed with RESTful architecture, CORS management, and image handling, the project ensures isolated image directories per user, enabling privacy and secure download functionality. Technologies used include:
Flask, MySQL, HTML/CSS/JS, REST APIs, Microservice Architecture, Image Upload/Download Handling, and Access Code Authentication.

- Developed multi-tier Flask services for secure image access
- Implemented access-code authentication and image folder isolation
- Used REST API architecture for service communication
- Designed responsive HTML/CSS frontend for user interaction
- Deployed local microservice architecture using Flask & Requests
- Handled image upload/download via HTTP endpoints
- Integrated CORS for cross-origin frontend-backend requests

## Features

- Access code–based user validation
- Image upload/download with isolated user folders
- RESTful APIs built with Flask
-  Modular structure (Gateway + Image Service)
-  Dynamic image listing & secure direct access
-  CORS enabled for frontend/backend interaction
-  MySQL database integration for user access control

---

## Architecture

Frontend (HTML/JS)
│
▼
Gateway Service (Flask @ :5000)
│
├── /get-images?access_code=xxxx
└── /upload-image (POST)
│
▼
Image Service (Flask @ :5001)
├── /upload
├── /list-images
└── /images/<folder>/<filename>

----- 

## Tech Stack

- **Python 3.x**
- **Flask**
- **MySQL**
- **HTML / CSS / JavaScript**
- **Requests (HTTP client between services)**
- **Flask-CORS**

---

