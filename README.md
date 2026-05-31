# Second-Third-Laboratory-Activity

# Setup Instructions

## STEP 1 — Create GitHub Repository

Go to GitHub and create a repository named:

```text
distributed-voting-system
```

Create the following project structure:

```text
distributed-voting-system/

├── api/
│   ├── app.py
│   └── requirements.txt
│
├── worker/
│   ├── worker.py
│   └── requirements.txt
│
├── edge/
│   └── edge_node.py
│
├── database/
│   └── schema.sql
│
└── README.md
```
Upload all source code files to the repository.

---

## STEP 2 — Supabase (Database)

Go to Supabase and create a free account.

Click:

```text
New Project
```

Project Name:

```text
distributed-voting-system
```

After the project is created:

Open:

```text
SQL Editor
```

Run:

```sql
CREATE TABLE votes (
  doc_id TEXT PRIMARY KEY,
  user_id TEXT,
  poll_id TEXT,
  choice TEXT,
  timestamp FLOAT,
  edge_id TEXT,
  processed_at FLOAT
);

ALTER TABLE votes DISABLE ROW LEVEL SECURITY;
```

Navigate to:

```text
Settings → API
```

Copy:

```text
Project URL
Anon Public Key
```

Save both values.

---

## STEP 3 — CloudAMQP (RabbitMQ Queue)

Go to CloudAMQP and create an account.

Click:

```text
Create New Instance
```

Configuration:

```text
Name:
vote-queue

Plan:
Little Lemur (Free)
```

After creation:

Open the instance.

Copy the:

```text
AMQP URL
```
Example:

```text
amqps://username:password@host/vhost
```

Save this URL.

---

## STEP 4 — Deploy API Service on Render

Go to Render.

Click:

```text
New +
→ Web Service
```

Connect the GitHub repository.

Configure:

```text
Name:
voting-api

Root Directory:
api

Runtime:
Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app
```

Add Environment Variable:

```text
RABBITMQ_URL=<CloudAMQP URL>
```

using:

```text
Add from .env
```

---


## CURRENT PROJECT STATUS

The project has currently completed:

```text
✓ GitHub Repository Setup

✓ Supabase Database Setup

✓ CloudAMQP RabbitMQ Setup

✓ Render API Configuration

✓ Environment Variable Configuration
```

Current location:

```text
Render
→ voting-api
→ Environment Variables
```

The following variable has already been added:

```text
RABBITMQ_URL=<CloudAMQP URL>
```

Current issue:

```text
Render requires billing verification before deployment can continue.
```

Deployment is currently paused at:

```text
Create Web Service
```

---

## STEP 5 — Complete API Deployment

After billing verification is completed:

Click:

```text
Create Web Service
```

Wait for deployment.

Render will generate an API URL similar to:

```text
https://voting-api.onrender.com
```
Verify by opening the URL.

Expected output:

```json
{
  "status":"API Running"
}
```

---

## STEP 6 — Deploy Worker Service

Create another Render Web Service.

Use the same repository.

Configuration:

```text
Name:
voting-worker

Root Directory:
worker

Runtime:
Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn worker:app
```

Add Environment Variables:

```text
RABBITMQ_URL=<CloudAMQP URL>

SUPABASE_URL=<Supabase URL>

SUPABASE_KEY=<Supabase Anon Key>
```

Deploy the service.

Verify:

```json
{
  "status":"worker running",
  "processed":0
}
```

---


## STEP 7 — Run Edge Nodes

Install Python 3.

Install dependencies:

```bash
pip install requests
```

Set variables:

```powershell
$env:API_URL="https://your-api-url.onrender.com/vote"

$env:NODE_ID="node-1"
```

Run:

```bash
python edge_node.py
```

---
## STEP 8 — Verify System Operation

Check:

```text
API receives votes

RabbitMQ queues messages

Worker consumes messages

Supabase stores processed votes
```

Verify rows appear in:

```text
Supabase
→ Table Editor
→ votes
```

---

## STEP 9 — Fault Tolerance Testing

### Duplicate Message Test

Enable:

```python
run_edge_node(duplicate=True)
```

Expected Result:

```text
Duplicate votes generated

No duplicate rows stored

Idempotency maintained
```

### Worker Failure Test

Stop the worker service.

Expected Result:

```text
API continues accepting votes

RabbitMQ buffers messages

Supabase updates pause
```

### Recovery Test

Restart worker service.

Expected Result:

```text
RabbitMQ drains queued messages

Worker resumes processing

Supabase catches up automatically

No data loss
```

---

## STEP 10 — Record Demonstration Video

Demonstrate:

```text
Vote Generation

API Processing

RabbitMQ Queue Activity

Worker Processing
Supabase Updates

Fault Tolerance Testing
```

---

## STEP 11 — Final Submission

Submit:

```text
GitHub Repository

README.md

Architecture Diagram

Demonstration Video

Deployment URL
```




## REFLECTION 

### Ampuan Ayyah
This project provided valuable insight into the design and implementation of distributed systems. Before working on this activity, I had limited experience with cloud platforms and message queuing services. Through the project, I learned how different technologies such as Supabase, CloudAMQP, GitHub, and Render can be combined to create an event-driven architecture for processing data across multiple components.

One of the most significant challenges was working with limited resources. Some project tasks had to be completed using a cellphone, which made file management, deployment configuration, and service setup more complicated than expected. Small configuration errors often required additional troubleshooting because multiple services needed to be configured correctly. As a result, I developed a greater appreciation for the importance of planning, organization, and attention to detail when working with distributed applications.

Although the project was not fully completed and some deployment stages remained unfinished, I gained a much better understanding of distributed computing principles. I learned the purpose of message queues, cloud databases, and service-based architectures, as well as the challenges involved in connecting multiple systems together. Overall, this project strengthened my knowledge of distributed systems and provided practical experience that will be useful in future software development projects.

### Abdulkarim Hakima 
Working on this Distributed Voting System project was both challenging and educational. One of the biggest difficulties our group encountered was completing the project with limited resources. Much of the setup process had to be done using a mobile phone instead of a laptop, which made configuring cloud services and managing project files more difficult. Navigating between GitHub, Supabase, CloudAMQP, and Render on a small screen required additional time and effort, especially when entering configuration details and troubleshooting setup issues.

Throughout the project, I learned how distributed systems divide tasks among multiple components instead of handling everything in a single application. I gained experience creating a cloud database using Supabase, setting up a RabbitMQ message queue through CloudAMQP, organizing a project repository in GitHub, and preparing deployment configurations in Render. Although some deployment and testing stages were not completed, the setup process helped me understand how data would flow through a distributed architecture and how each component plays a specific role within the system.

Another challenge was learning unfamiliar technologies within a limited amount of time. Understanding how different services connect and communicate required careful reading of documentation and repeated troubleshooting. Despite these challenges, the project improved my understanding of distributed computing concepts and gave me practical experience with cloud-based tools and system architecture design.
