# Project Report
## Cloud Development Final Project

**Project Name:** BlueFlameSearch (MongoDB Edition)

### 1. Project Idea and Objectives
The objective of this project is to provide a robust Information Retrieval (IR) Search Engine capable of indexing text documents and performing queries using the TF-IDF algorithm. As part of adapting this project for a cloud environment, we've extended its core functionality by introducing persistent storage using **MongoDB**. This allows users to create, read, update, and delete (CRUD) documents dynamically directly from the interactive Web interface.

The main goals are:
- Provide a clear, real-world utility (Search Engine with Document Management).
- Ensure data is persistently stored rather than read on-the-fly from file systems.
- Containerize the solution for consistent testing and production deployment.
- Successfully deploy and run the system on AWS Cloud infrastructure.

### System Architecture Diagram
```mermaid
graph TD
    Client(User Web Browser) -- "HTTP Traffic\nPort 5000" --> Flask[Flask Web Application\n(Docker Container: web)]
    
    subid1 --- Flask
    
    Flask -- "Database Ops\nport 27017" -.-> DB[(MongoDB Database\nDocker Container: mongodb)]
    
    Flask -- "CRUD operations\nRebuilds Index" --> Mem[In-Memory TF-IDF Index]
    Flask -- "Search Queries" --> Mem
```

### 2. AWS Services Used
- **Amazon EC2 (Elastic Compute Cloud):** We are using a Linux-based EC2 instance to serve as the cloud host for our containerized application. The EC2 instance will run `Docker` and `Docker Compose` to orchestrate our application, making it highly available over the public web.
- **Security Groups:** Used to open up TCP ports `80` and `5000` to allow inbound traffic so users can access the web application interface publicly securely.

### 3. Deployment Steps on AWS EC2
1. **Provision EC2 Instance:**
   - Launch an AWS EC2 instance using the `Ubuntu Server` or `Amazon Linux 2` AMI.
   - Choose a `t2.micro` instance type (Free Tier eligible).
   - Configure the instance's Security Group to allow basic inbound traffic: `SSH` (Port 22) from your IP, and `Custom TCP` (Port 5000) for the Flask App.
2. **Setup Docker Environment:**
   - SSH into the instance using its Public IPv4 Address.
   - Install Docker (`sudo apt install docker.io`) and Docker Compose (`sudo apt install docker-compose`).
   - Add the default EC2 user to the `docker` group to execute commands without `sudo` (`sudo usermod -aG docker ubuntu`).
3. **Deploy Application Code:**
   - Clone the git repository containing this application or transfer the project files over SFTP/SCP.
   - Navigate to the project directory `/IR Search Engine`.
4. **Launch with Docker Compose:**
   - Run `docker-compose up -d --build`. This starts the Flask web service and the MongoDB database in detached mode.
5. **Validation:**
   - Open your web browser and visit `http://<EC2-PUBLIC-IP>:5000`. You will see the BlueFlameSearch interface.
