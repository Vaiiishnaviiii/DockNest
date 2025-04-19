# Docker Bridge Networking: Demonstrating Container Isolation and Communication

## 🧠 Overview

This project demonstrates how Docker containers communicate when placed on the same **custom bridge network**, while remaining **isolated** when on different networks. It showcases the importance of Docker networking in microservices and containerized applications, highlighting security, isolation, and performance.

---

## 🎯 Objective

The goal of this project is to:

- ✅ Create a custom bridge network for Docker containers.
- 🔄 Demonstrate communication between containers on the same network.
- 🚫 Show network isolation between containers on different networks.

---

## 🛠 Prerequisites

Before starting, ensure you have:

- Docker installed on your system.
- A basic understanding of Docker concepts such as containers, images, and networks.

---

## 🌐 Docker Networking Overview

Docker provides several networking options for containers:

- **Bridge Network (default)** – Allows communication between containers using internal IPs.
- **Custom Bridge Network** – Offers DNS-based service discovery and better isolation.
- **Host Network** – Container uses the host's networking stack.
- **Overlay Network** – Enables communication across multiple Docker hosts (used in Swarm).
- **Macvlan Network** – Assigns a MAC address to containers.
- **None Network** – Disables networking completely.

This project focuses on the **Custom Bridge Network**.

---

## ⚙️ Steps to Setup and Test Docker Networking

### Create a Custom Bridge Network

Run the following command to create a custom bridge network:

```bash
docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 vaishnavi-bridge
2️⃣ Launch Docker Containers
Launch a Redis container and a BusyBox container on the same custom network:

bash
Copy
Edit
docker run -itd --net=vaishnavi-bridge --name=vaishnavi-database redis
docker run -itd --net=vaishnavi-bridge --name=vaishnavi-server-A busybox
3️⃣ Inspect the Network
Inspect the network to check IP addresses assigned to the containers:

bash
Copy
Edit
docker network inspect vaishnavi-bridge
4️⃣ Test Connectivity Between Containers
Ping from one container to another using:

bash
Copy
Edit
docker exec -it vaishnavi-server-A ping 172.20.240.1
Press Ctrl + C to stop the ping.

5️⃣ Verifying BusyBox as a Testing Tool
You can run another container and test connectivity from it:

bash
Copy
Edit
docker run -itd --net=vaishnavi-bridge --name=vaishnavi-ping busybox
docker exec -it vaishnavi-ping ping 172.20.240.1
6️⃣ Stop and Remove Containers and Network (Cleanup)
To clean up your Docker environment after the experiment:

bash
Copy
Edit
docker stop vaishnavi-database vaishnavi-server-A vaishnavi-ping
docker rm vaishnavi-database vaishnavi-server-A vaishnavi-ping
docker network rm vaishnavi-bridge
✅ Conclusion
This project demonstrates how Docker's custom bridge networks enable secure container-to-container communication while maintaining isolation. Understanding networking is essential when designing and deploying microservices-based systems.
