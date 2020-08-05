docker system prune -a
docker build -t my_docker:latest .
docker run -d -p 5001:5001 my_docker:latest