</> Markdown
# Docker Images Management and Layer Analysis

## Project Overview

This project demonstrates practical hands-on experience with Docker image management using Docker CLI. The lab focused on understanding Docker images, working with image tags, inspecting image metadata, analyzing image layers, and applying image management best practices.

The exercises were performed in a Linux environment using Docker Engine and included interaction with Docker Hub, image lifecycle management, and storage optimization techniques commonly used in modern DevOps environments.

---

## Objectives

* Search Docker images from Docker Hub
* Pull and manage Docker images locally
* Understand image tags and versioning
* Run containers using specific image versions
* Create custom image tags
* Inspect image metadata
* Analyze Docker image layers
* Perform image cleanup and storage optimization
* Apply Docker image management best practices

---

## Technologies Used

* Docker Engine
* Docker Hub
* Ubuntu Linux
* Nginx
* Python Runtime Images
* Docker CLI

---

## Lab Activities Performed

### 1. Docker Hub Exploration

Searched and evaluated public images using:

docker search ubuntu
docker search nginx
docker search --limit 5 python

Key observations:

* Official images are maintained by trusted vendors
* Docker Hub provides version tags, documentation, and usage statistics
* Image selection impacts security, size, and maintainability


### 2. Pulling Docker Images

Downloaded multiple image versions and variants:

docker pull ubuntu
docker pull ubuntu:20.04
docker pull ubuntu:22.04
docker pull nginx:alpine
docker pull python:3.9-slim


Learned concepts:

* Image layers
* Layer caching
* Version-specific image pulls
* Lightweight image variants


### 3. Image Management

Listed and filtered locally stored images:


docker images
docker images -a
docker images -q


Used formatting options to improve readability:


docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"


### 4. Image Removal Operations

Removed images using:

docker rmi ubuntu:20.04
docker rmi IMAGE_ID
docker image prune


Practical understanding gained:

* Removing unused images
* Reclaiming storage space
* Dangling image cleanup

### 5. Running Version-Specific Containers

Executed containers using specific Ubuntu versions:


docker run -it ubuntu:22.04 /bin/bash

Verified operating system details:


cat /etc/os-release


This demonstrated version consistency across environments.



### 6. Custom Image Tagging

Created a custom production tag:


docker tag ubuntu:22.04 my-ubuntu:production


Verified tag creation:


docker images | grep my-ubuntu



### 7. Image Inspection

Collected detailed image metadata:


docker inspect ubuntu:22.04

Retrieved specific attributes:


docker inspect --format='{{.Architecture}}' ubuntu:22.04
docker inspect --format='{{.Created}}' ubuntu:22.04
docker inspect --format='{{.Size}}' ubuntu:22.04


### 8. Docker Layer Analysis

Investigated image build history:


docker history ubuntu:22.04


Key findings:

* Images are built in layers
* Layers improve storage efficiency
* Shared layers reduce download time
* Layer caching accelerates deployments


## Screenshots

| Screenshot | Description                 |
| ---------- | --------------------------- |
| 01         | Docker Hub image search     |
| 02         | Nginx repository search     |
| 03         | Pulling Ubuntu image        |
| 04         | Listing local images        |
| 05         | Formatted image output      |
| 06         | Running Ubuntu container    |
| 07         | Ubuntu version verification |
| 08         | Custom image tagging        |
| 09         | Docker inspect results      |
| 10         | Docker history output       |
| 11         | Layer analysis              |
| 12         | Cleanup operations          |

---

## Key Concepts Learned

* Docker Images
* Docker Hub
* Image Tags
* Official Images
* Image Layers
* Layer Caching
* Image Inspection
* Image History
* Storage Optimization
* Container Versioning
* Docker Cleanup
* Image Lifecycle Management


## Best Practices Applied

* Used explicit image tags instead of the latest
* Preferred lightweight image variants where applicable
* Inspected image metadata before usage
* Analyzed image layers for optimization awareness
* Regularly removed unused images
* Practiced image version consistency


## Outcome

Successfully demonstrated practical Docker image management skills, including image discovery, downloading, inspection, tagging, cleanup, and layer analysis. The lab strengthened foundational knowledge required for containerized application deployment, Docker administration, and DevOps engineering workflows.
