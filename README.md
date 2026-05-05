# 🔥 BlueFlameSearch (MongoDB Edition)

![Docker Structure](https://img.shields.io/badge/docker-containerized-blue.svg?logo=docker)
![Cloud Deployment](https://img.shields.io/badge/AWS-EC2%20Deployed-orange.svg?logo=amazonaws)
![Python Backend](https://img.shields.io/badge/backend-Flask-green.svg?logo=python)
![Database](https://img.shields.io/badge/database-MongoDB-darkgreen.svg?logo=mongodb)

BlueFlameSearch is a professional, cloud-ready Information Retrieval (IR) Search Engine capable of indexing text documents and processing queries using the TF-IDF mathematical algorithm. 

This repository constitutes the comprehensive final project for Cloud Development. It extends the core search functionality by offering a modern web interface mapped seamlessly to a persistent **MongoDB** backend, packaged cleanly within Docker containers.

---

## 🌟 Key Features
- **Information Retrieval Core:** Accurately evaluates and ranks documents based on Term Frequency-Inverse Document Frequency (TF-IDF).
- **Persistent Data Store:** Powered by MongoDB. Moving away from static flat files to a responsive NoSQL data architecture. 
- **Full CRUD Support:** Documents can be created, read, updated, and deleted natively from the Web UI.
- **Fully Containerized:** Utilizing Docker and `docker-compose` to isolate configurations, simplifying the dependency footprint.
- **Cloud-Ready Deployment:** Engineered strictly for seamless execution on AWS EC2 or Elastic Beanstalk infrastructure.

---

## 🚀 How to Run Locally (Docker)

Running the application environment locally is incredibly straightforward thanks to Docker. Ensure that [Docker Engine](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) are successfully installed on your machine.

**1. Clone and Navigate**
Clone this repository to your local machine, and navigate into the root directory:
```bash
cd "IR Search Engine"
```

**2. Build & Launch Containers**
Instruct Docker Compose to build the Flask REST-API and pull the MongoDB instance:
```bash
docker-compose up --build
```
> **Note:** If executing it as a background service, simply append the `-d` flag: `docker-compose up -d --build`.

**3. Application Seeding**
On its very first launch, the Python web backend will automatically crawl the local `Data/` directory and securely seed all default initial documents into MongoDB natively.

**4. Access the Application**
Launch your preferred web browser and navigate to:  
🌍  **[`http://localhost:5000`](http://localhost:5000)**

You can immediately start feeding search queries to the engine, or switch to the *Documents list* view to manage CRUD configurations.

---

## ☁️ How to Access the Deployed App on AWS

The application is engineered to operate harmoniously within an AWS EC2 instance environment.

Assuming the deployment phase outlined meticulously inside the [`Project_Report.md`](Project_Report.md) has been concluded:

1. Retrieve the **Public IPv4 address** or the **Public DNS (IPv4)** from your AWS EC2 console.
2. Ensure you have appropriately updated the EC2 instance's **Security Groups** to publicly permit Custom TCP Inbound Connections on `Port 5000`.
3. Open your browser and access the cloud endpoint via:
   ```text
   http://<EC2_PUBLIC_IP_OR_DOMAIN>:5000
   ```
4. The cloud-managed search engine along with the NoSQL layer will instantly initialize for the end-user.

---

## 📂 Project Structure Snapshot
```text
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

---
*Built as the Final Project for Cloud Development*
