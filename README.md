# Procedure Composer MVP

## Project Overview
The Procedure Composer MVP (Minimum Viable Product) project is designed to provide a streamlined interface for creating and managing procedural documents. This application allows users to compose procedures easily, ensuring compliance with standard practices and enhancing productivity.

## Setup Instructions
1. **Clone the Repository**  
   Run the following command to clone the repository:  
   ```bash  
   git clone https://github.com/Danmiller2117/RSO-Standard-Procedure-Developer-Application.git
   ```  

2. **Install Dependencies**  
   Navigate to the project directory and install the required dependencies:  
   ```bash  
   cd RSO-Standard-Procedure-Developer-Application  
   npm install  
   ```  

3. **Run the Application**  
   Start the application using the following command:  
   ```bash  
   npm start  
   ```  

## API Endpoint Examples
- **Create Procedure**  
  **Endpoint:** `POST /api/procedures`  
  **Request Body:**  
  ```json  
  {  
    "title": "New Procedure",  
    "description": "Description of the procedure to be created."  
  }
  ```  
  **Response:**  
  ```json  
  {  
    "id": "1234",  
    "title": "New Procedure",  
    "status": "created"  
  }
  ```  

- **Get Procedures**  
  **Endpoint:** `GET /api/procedures`  
  **Response:**  
  ```json  
  [  
    {  
      "id": "1234",  
      "title": "New Procedure",  
      "status": "active"  
    }  
  ]
  ```  

- **Update Procedure**  
  **Endpoint:** `PUT /api/procedures/{id}`  
  **Request Body:**  
  ```json  
  {  
    "title": "Updated Procedure Title"  
  }
  ```  
  **Response:**  
  ```json  
  {  
    "id": "1234",  
    "title": "Updated Procedure Title",  
    "status": "updated"  
  }
  ```  

---

For more information, please refer to the project documentation.