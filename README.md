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
This activity gave me a deeper understanding of distributed computing concepts and how multiple services work together to process data. Although the architecture appeared simple on paper, implementing and connecting all components required significant effort. Our group worked with limited resources, and some of the setup process had to be completed using a cellphone, which made deployment and configuration more challenging than expected. Tasks such as editing repository files, managing cloud service settings, and configuring deployment environments were more time-consuming due to the limitations of mobile devices.

During development, I noticed that distributed execution behaves differently from a traditional sequential program. Instead of processing votes immediately, the system used a queue to temporarily store messages before they were handled by the worker service. This design reduced the workload on the API and helped maintain system responsiveness. I also learned how message buffering contributes to fault tolerance because votes can still be accepted even when downstream services are temporarily unavailable.

One of the most difficult parts of the project was troubleshooting deployment and cloud configuration issues. Because several independent services were involved, identifying the cause of an error often required checking multiple platforms and verifying that credentials, URLs, and environment variables were configured correctly. However, overcoming these challenges improved my understanding of distributed architectures and cloud-based systems.

Overall, this activity demonstrated both the strengths and complexities of distributed computing. While the architecture improved reliability, scalability, and fault tolerance, it also introduced additional configuration and debugging challenges. Despite the limitations of working with a cellphone and limited resources, the experience helped me develop practical skills in cloud services, asynchronous processing, and distributed system design.
