# BlueFlameSearch - Containerized Application

BlueFlameSearch is a Flask-based Search Engine using TF-IDF for evaluating and ranking documents. It includes a frontend to perform search queries and manage indexed documents seamlessly by incorporating an integrated **MongoDB** data store.

## How to Run Locally (Docker)

This project has been thoroughly containerized for ease of execution using `docker-compose`. Ensure you have Docker and Docker Compose installed on your system before beginning.

1. **Navigate to the core project directory:**
   ```bash
   cd "IR Search Engine"
   ```

2. **Run Docker Compose:**
   Build and spin up the containers with:
   ```bash
   docker-compose up --build
   ```

3. **Database Seeding:**
   If this is your first time bringing up the application, the backend will automatically seed the initial document collection from the `Data/` folder into the underlying MongoDB instance.

4. **Access the application locally:**
   Navigate in your web browser to:
   http://localhost:5000
   
   From there, you can submit search queries or visit the **Documents** tab to explicitly manage (Add/Edit/Delete) the indexed documents.

## How to Access the Deployed App on AWS

Once deployed to AWS EC2 (see the complete step-by-step in `Project_Report.md`):

1. Your App will be available over the public IP or domain of your EC2 instance.
2. Ensure you have properly opened the necessary TCP ports (Port 5000 for standard testing, or mapped to Port 80 for normal HTTP access in `docker-compose.yml`) within the Security Group associated with your instance.
3. Access URL: `http://<EC2_PUBLIC_IP_OR_DOMAIN>:5000/`
