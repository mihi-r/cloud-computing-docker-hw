# Cloud Computing Docker Homework
Running Docker with a short Python script. This project was created for the Cloud Computing class at University of Cincinnati.

# Usage Instructions
1. Build Docker image: `docker build --tag cc-hw:1.0 .`
2. Run Docker container: `docker run --volume "$(pwd)/sample-files:/home/data" --name cc-hw-container cc-hw:1.0`