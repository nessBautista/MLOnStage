**Exercise 1: Container Communication Basics**

- **Objective:** Establish communication between two Docker containers.
- **Steps:**
1. Create a Docker network using the command docker network create <network_name>.**12**
2. Launch two containers (e.g., a web server like Nginx and a database like PostgreSQL) and attach them to the network you created.**123**
3. Configure the web server container to access the database container using the database container's name as the hostname within the network.**3**
4. Verify connectivity by accessing the web application and confirming its interaction with the database.