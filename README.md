# Portfolio

Ross Mountjoy's personal portfolio website.
---
## Features

- Created in minutes using my personal Flask template
- Fully deployed on AWS using an ECS EC2 cluster
- Ready to go REST API with SwaggerUI Documentation
- Includes admin page for viewing/editing database records
- Ready to go for webpages with Bootstrap CSS
- Uses managed database from AWS RDS MySQL through SQLAlchemy
- Pull from Docker hub, build with docker, or run as a standalone python application
- Includes different deploy modes, ready for any deployment environment.
---

Want to run it locally?

## Installing

### (Option 1) Pull from Docker Hub:
```bash
docker create \
  --name=rossmountjoyportfolio \
  -p 5000:5000 \
  --restart unless-stopped \
  rmountjoy/portfolio:latest
```

### (Option 2) Build Using Docker:
Clone repository & navigate to it:

```bash
git clone https://github.com/rmountjoy92/Portfolio.git
cd Portfolio
```
Build and run using Docker:

```bash
docker build -t Portfolio .
docker run --publish 5000:5000 Portfolio
```

### (Option 3) Development Server:
Clone repository & navigate to it:

```bash
git clone https://github.com/rmountjoy92/Portfolio.git
cd Portfolio
```

Create virtual environment & activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Start the test server:
```bash
python3 run_test_server.py
 ```



Visit the following address in your browser:  
`http://localhost:5000/`

To view/test the rest API go to:  
`http://localhost:5000/api`

### Stack
- (optionally) Docker
- Flask (Python 3.8)
- SQLAlchemy
- HTML5/Jinja2
- Bootstrap CSS
- RestX, SwaggerUI
