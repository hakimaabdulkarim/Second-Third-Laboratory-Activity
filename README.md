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
