## My Personal Sentimental Diary
This project is a fullstack diary application built with a React front-end and a Flask back-end. The back-end uses MongoDB Atlas for data storage.

## Description

This is a diary website that provides emotion and sentiment analysis based on the content written in the diary. It utilizes two pre-trained machine learning models to analyze the text and give feedback on the user's emotions and sentiments. The website also provides a calendar view to navigate through the diary entries.

## Prerequisites

- Python 3.x
- Node.js and npm
- MongoDB Atlas account

## Setting Up MongoDB Atlas

1. **Create a MongoDB Atlas Account:**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and sign up for a free account.

2. **Create a Cluster:**
   - After signing in, click on "Build a Cluster".
   - Choose the free tier and select your preferred cloud provider and region.
   - Click "Create Cluster".

3. **Create a Database User:**
   - Go to the "Database Access" tab.
   - Click "Add New Database User".
   - Enter a username and password. Make sure to save these credentials as you will need them later.
   - Assign the user "Atlas Admin" role.

4. **Get the Connection String:**
   - Go to the "Clusters" tab.
   - Click "Connect" on your cluster.
   - Choose "Connect your application".
   - Copy the connection string. It should look something like this:
     ```
     mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/test?retryWrites=true&w=majority
     ```

5. **Create a Database and Collection:**
   - Click on "Collections" in your cluster.
   - Click "Add My Own Data".
   - Enter "Diary" as the database name and "Daily Notes" as the collection name.

## Setting Up the Back-End

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Dark-Myth/diary-fullstack---react-app
   cd diary-fullstack---react-app
   ```

2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Navigate to the Back-End Directory:**
   ```sh
   cd mini-proj-2-backend
   ```

4. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables:**
   - Create a `local_config.py` file in the `server` directory with the following content:
     ```python
     MONGODB_CLUSTER = "<cluster-url>"
     MONGODB_USER = "<username>"
     MONGODB_PASSWORD = "<password>"
     APP_NAME = "DiaryApp"
     ```

5. **Run the Back-End Server:**
   ```sh
    python server.py
   ```

## Setting Up the Front-End

1. **Navigate to the Front-End Directory:**
   ```sh
   cd mini-proj-2-frontend
   ```

2. **Install Dependencies:**
   ```sh
   npm install
   ```

3. **Run the Front-End Development Server:**
   ```sh
   npm run dev
   ```

4. **Open your browser and navigate to** `http://localhost:3000`


