# To-Do List Application

A simple and intuitive to-do list application that helps users organize their tasks. Built with React for the frontend, FastAPI for the backend, and MongoDB for persistent data storage. The app is containerized using Docker for seamless deployment.

# Video
Here is a link to the YouTube video of the project: https://youtu.be/fK5rb5suwLM

# Usage
Once the app is running, you can access the following functionalities in port 8000:

Create a To-Do List: Add new to-do lists to manage tasks.
Add Tasks: Add tasks to each to-do list.
Complete Tasks: Mark tasks as completed.
Delete Tasks: Delete tasks from the list.
Delete To-Do Lists: Remove to-do lists.

# Architecture
The application follows a typical three-tier architecture:

Frontend (React): Handles the user interface, displaying to-do lists, tasks, and enabling interactions.
Backend (FastAPI): Exposes API endpoints to interact with the frontend and manage to-do list data.
Database (MongoDB): Stores all the to-do lists and tasks persistently.

# Technologies Used
Frontend: React, React Router
Backend: FastAPI, Python
Database: MongoDB
Docker: For containerization
Styling: CSS, custom styling

## Installation

Follow these steps to get the project up and running on your local machine.

### Clone the repository
First, clone this repository to your local machine:

```bash
git clone git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-VI/RoyRizelFinalProject.git
cd RoyRizelFinalProject
```
Then open the folder using VS manually or code . in bash and use docker-compose up --build in the VS terminal. reach port 8000 once setup is done to create your ToDo lists.
