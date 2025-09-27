# DIY_dashboard
This project serves to repurpose old laptops into dashboards that can convey the necessary information to get you through the day.

## How to Run
1. Install dependencies:
```bash
cd dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Start server:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 5000
```

3. Open browser:
```
http://localhost:5000
```

4. (Optional) Kisosk mode on startup:
```bash
chromium --kiosk --app=http://localhost:5000
```
