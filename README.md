# AWS Week 3 - Dockerized Flask App on EC2

## What I Built
A containerized Python Flask app deployed on AWS EC2 serverd through an Application Load Balancer (ALB)

## Architecture
Internet -> ALB (public subnets) -> EC2 + Docker -> Flask App

## Tech Stack
- Python + Flask
- Docker + Docker Hub
- AWS EC2, VPC, ALB, Auto Scaling Group

## How to Run Locally
```bash
dokcer pull bobbysmith0/week3-flask-app:lastest
dokcer run -p 5000:5000 bobbysmith0/week3-flask-app:lastest
```
Visit http://localhost:5000

## Docker Hub
https://hub.docker.com/r/bobbysmith0/week3-flask-app
