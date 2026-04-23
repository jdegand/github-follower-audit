# GitHub Follower Audit

A small CLI Python tool (mostly AI‑generated, with manual debugging and glue work) that analyzes a GitHub user's followers and identifies:

- **Dead followers** — inactive or abandoned accounts  
- **Bot‑like followers** — accounts with suspicious patterns  

The project uses simple heuristics and scoring rules to classify each follower.

---

## Build the Docker Image

```bash
sudo docker build -t github-follower-audit .
```

If you want to force a clean rebuild:

```bash
sudo docker build --no-cache -t github-follower-audit .
```

---

## Running Without a GitHub Token (Not Recommended)

```bash
sudo docker run --rm \
  --entrypoint python \
  github-follower-audit \
  run.py username
```

**Warning:**  
Without a token, GitHub rate limits you to **60 requests/hour**, which is not enough for users with many followers.

---

## Running With a GitHub Token (Recommended)

Create a `.env` file:

```bash
GITHUB_TOKEN=ghp_your_token_here
```

The token only needs the **read:user** permission.

Run the audit:

```bash
sudo docker run --rm \
  --env-file .env \
  --entrypoint python \
  github-follower-audit \
  run.py jdegand
```

---

## Example Output

```json
{
  "username": "jdegand",
  "total_followers": 118,
  "dead_followers_pct": 2.54,
  "bot_followers_pct": 0.85,
  "dead_followers": [
    "CODECODEdz",
    "ashilaf",
    "rishi-soni"
  ],
  "bot_followers": [
    "The-force-bee-with-you"
  ]
}
```

---

## Notes

- The heuristics are intentionally simple and conservative.  
- A follower is only flagged if they exceed strict scoring thresholds.  
- This tool is meant for curiosity and exploration, not scientific accuracy.
- Sparked by an article examining how and why developers inflate GitHub star counts.
