# 🔥 BlueFlameSearch (MongoDB Edition)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

BlueFlameSearch is a professional, cloud-ready Information Retrieval (IR) Search Engine capable of indexing text documents and processing queries using the TF-IDF mathematical algorithm. This project serves as the comprehensive final project for Cloud Development, extending core search functionality with a modern web interface seamlessly integrated with a persistent **MongoDB** backend, all packaged cleanly within Docker containers.

## ✨ Key Features

*   **Information Retrieval Core:** Accurately evaluates and ranks documents based on the **Term Frequency-Inverse Document Frequency (TF-IDF)** algorithm.
*   **Persistent Data Store:** Powered by **MongoDB**, providing a responsive NoSQL data architecture for dynamic data persistence, moving away from static flat files.
*   **Full CRUD Support:** Documents can be **C**reate, **R**ead, **U**pdate, and **D**elete natively through the intuitive Web UI.
*   **Fully Containerized:** Utilizes **Docker** and `docker-compose` for isolating configurations and simplifying dependency management, ensuring consistency across environments.
*   **Cloud-Ready Deployment:** Engineered for seamless execution on **AWS EC2** or **AWS Elastic Beanstalk** infrastructure, demonstrating core cloud concepts.

## 🚀 Getting Started (Local Development)

Running the application locally is straightforward thanks to Docker. Ensure that [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) are successfully installed on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Blue-Flame-Team/Cloud-ProjectIR.git
cd Cloud-ProjectIR
```

### 2. Build & Launch Containers

Instruct Docker Compose to build the Flask REST-API and pull the MongoDB instance:

```bash
docker-compose up --build
```

> **Note:** To run as a background service, append the `-d` flag: `docker-compose up -d --build`.

### 3. Application Seeding

On its very first launch, the Python web backend will automatically crawl the local `Data/` directory and securely seed all default initial documents into MongoDB.

### 4. Access the Application

Launch your preferred web browser and navigate to:

🌍 **[http://localhost:5000](http://localhost:5000)**

You can immediately start feeding search queries to the engine or switch to the _Documents list_ view to manage CRUD configurations.

## ☁️ Deployment on AWS

The application is designed for harmonious operation within an AWS EC2 instance environment. For detailed deployment steps, please refer to the `Project_Report.md`.

### Quick Access Steps:

1.  Retrieve the **Public IPv4 address** or **Public DNS (IPv4)** from your AWS EC2 console.
2.  Ensure your EC2 instance's **Security Groups** are configured to publicly permit Custom TCP Inbound Connections on `Port 5000`.
3.  Open your browser and access the cloud endpoint via:
    
    ```
    http://<EC2_PUBLIC_IP_OR_DOMAIN>:5000
    ```
    
4.  The cloud-managed search engine and NoSQL layer will instantly initialize for the end-user.

## 📂 Project Structure

```
.
├── Core/               # TF-IDF computational algorithms & Document parsing logic
├── Data/               # Raw default seeding files (.txt)
├── templates/          # HTML frontend interfaces
├── static/             # CSS styling and static assets
├── app.py / server.py  # Primary Flask controllers and REST handlers
├── docker-compose.yml  # Multi-container orchestration payload
├── Dockerfile          # Configuration instructions for the web container
├── Project_Report.md   # Extensive Cloud Documentation (Objective & AWS Info)
└── README.md           # This document
```

## 👥 Team Members

*   Ahmed Ashraf Ibrahim Abdel Gwwad (241440964)
*   Mohamed Magdy Moustafa Kabary (241311555)
*   Abdelrahman walid ibrahim salim (241321331)
*   Youssef Abdelbadea Ezzat (241478384)
*   Nada Mohamed Mahmoud Mohamed (241414781)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (Assuming an MIT license, please adjust if different).
