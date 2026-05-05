# ☁️ Cloud Development Final Project Report
**Project Name:** BlueFlameSearch (MongoDB Edition)  
**Course:** Cloud Development  

---

## 📑 Table of Contents
1. [Project Overview & Objectives](#1-project-overview--objectives)
2. [Fulfillment of Functional Requirements](#2-fulfillment-of-functional-requirements)
3. [Cloud architecture & AWS Services Used](#3-cloud-architecture--aws-services-used)
4. [Containerization Strategy](#4-containerization-strategy)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Deployment Steps on AWS EC2](#6-deployment-steps-on-aws-ec2)

---

## 1. Project Overview & Objectives
**BlueFlameSearch** is a robust, cloud-native Information Retrieval (IR) Search Engine capable of evaluating, ranking, and retrieving text documents using the advanced TF-IDF algorithm. Adapted to modern cloud environments, this project extends core algorithmic logic by integrating **MongoDB** for seamless, persistent data storage.

### Objectives:
- Provide a responsive, real-world utility: allow end-users to search through massive text blocks and retrieve the most relevant documents instantly.
- Transition from static file-based storage to dynamic, cloud-ready NoSQL data persistence.
- Leverage containerization (Docker) to isolate the application, ensuring consistency across development, testing, and production phases.
- Achieve a highly available deployment on **AWS Elastic Compute Cloud (EC2)** infrastructure.

---

## 2. Fulfillment of Functional Requirements
Our system has been built from the ground up to satisfy all core criteria:

- **1. Clear real-world functionality:** Delivers an Information Retrieval Search Engine that efficiently helps users locate relevant documents based on search constraints.
- **2. User-facing interface:** A clean, interactive web frontend built using HTML/CSS/JS with a responsive UI.
- **3. Backend Service:** A RESTful architecture implemented using the Python **Flask** framework, processing queries and managing core IR operations.
- **4. Persistent Database:** Utilizes **MongoDB** (NoSQL), running within its own container, to maintain persistence across sessions.
- **5. Full CRUD Support:** The web interface and backend provide native support for:
  - **Create:** Adding new documents dynamically.
  - **Read:** Fetching and ranking documents via search queries.
  - **Update:** Modifying the content of existing documents.
  - **Delete:** Removing documents from the database and the active TF-IDF index.

---

## 3. Cloud Architecture & AWS Services Used
The architecture emphasizes modularity, ensuring the Flask application seamlessly integrates with the MongoDB datastore.

### AWS Integration:
- **Amazon EC2 (Elastic Compute Cloud):** A Linux-based `t2.micro` (Free Tier eligible) instance serves as the primary cloud host. The application is orchestrated directly on this instance utilizing Docker Compose, providing global availability.
- **AWS Security Groups:** Network firewall rules are established to securely expose the platform:
  - **Port 5000:5000** for direct web application traffic.
  - **Port 22/tcp** (SSH) scoped strictly to admin IPs for secure infrastructure access.

### System Architecture Diagram
```mermaid
graph TD
    Client(User Web Browser) -- "HTTP Traffic\nPort 5000" --> Flask[Flask Web Application\n(Docker Container: web)]
    
    Flask -- "Data Persistence\nport 27017" -.-> DB[(MongoDB Database\nDocker Container: mongodb)]
    
    Flask -- "Document Management\n(CRUD) Rebuilds Index" --> Mem[In-Memory TF-IDF Index]
    Flask -- "Search Queries" --> Mem
```

---

## 4. Containerization Strategy
To guarantee that the solution is reliable and environment-agnostic, the application has been fully containerized:
- **Dockerized Application:** A well-structured `Dockerfile` is provided for the Flask backend to encapsulate the Python runtime, dependencies (`requirements.txt`), and environment variables.
- **Multi-Container Orchestration:** A `docker-compose.yml` file is implemented to launch and link the Flask application container with the MongoDB container seamlessly.
- **Local Testing:** The entire suite can be spun up reliably on any local machine using a single unified command: `docker-compose up --build`.

---

## 5. Non-Functional Requirements
The system adheres to standard best practices:
- **Scalability:** By keeping the web application stateless (saving state in MongoDB), horizontal scaling can easily be achieved by adding a load balancer and multiple Flask frontends.
- **Reliability:** Docker's restart policies prevent complete downtime; the system inherently recovers from application-level faults.
- **Error Handling:** Robust try-catch blocks and structured responses ensure that database timeouts or parsing errors do not crash the user experience.
- **Code Quality:** Organized utilizing clear controllers (`server.py`) and centralized core logic (`TFIDF.py`, `data_loader.py`), promoting high maintainability.
- **Logging:** Flask's built-in application logger is heavily utilized to output backend debug messages and monitor container health statuses.

---

## 6. Deployment Steps on AWS EC2
Follow the steps precisely to replicate the cloud deployment.

### Step 1: Provision the EC2 Instance
1. Access the AWS Management Console and navigate to **EC2 > Instances > Launch Instance**.
2. Select the **Ubuntu Server 22.04 LTS** (or Amazon Linux 2023) AMI.
3. Select the **t2.micro** instance type.
4. Create and attach a new key pair (`.pem` file) for SSH access.
5. In the Network Settings, allow SSH traffic. Add a Custom TCP Rule for **Port 5000** with source set to `0.0.0.0/0`.
6. Launch the instance.

### Step 2: Establish SSH Connection and Install Dependencies
1. Connect via SSH:
   ```bash
   ssh -i "your-key.pem" ubuntu@<PUBLIC_IPv4_ADDRESS>
   ```
2. Update the package list and install Docker binaries:
   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose -y
   ```
3. Add the default user to the Docker group to avoid `sudo` execution overhead:
   ```bash
   sudo usermod -aG docker ubuntu
   ```
4. *Log out and log back in for the changes to take effect.*

### Step 3: Deploy Application Code and Launch
1. Transfer the project payload securely over SCP/Git directly into the Ubuntu instance.
2. Navigate to the project root directory where the `docker-compose.yml` resides:
   ```bash
   cd "IR Search Engine"
   ```
3. Spin up the cluster in detached mode:
   ```bash
   docker-compose up -d --build
   ```
   *Docker will pull the necessary MongoDB image, build the Flask container, and link them securely.*

### Step 4: Verification
1. Access a web browser and navigate directly to your cloud host URL:
   `http://<EC2-PUBLIC-IP>:5000`
2. The user interface will load appropriately, finalizing the successful cloud deployment.
