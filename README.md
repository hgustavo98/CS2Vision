# CS2Vision Repository

## Overview
CS2Vision is an innovative project aimed at analyzing and visualizing Counter-Strike 2 (CS2) match data. This repository combines modern web development, backend processing, and machine learning to deliver an end-to-end demo analysis platform.

### Key Features:
- Upload CS2 demo files and process them using a robust backend service.
- Visualize results interactively through a React-based frontend.
- Utilize ML models to detect movement patterns and strategies.

---

## Core Components

### Frontend
- Built with React.
- Now includes:
  - An `UploadComponent` for user interactivity.
  - Interactive responses based on backend API status.

### Backend
- Built with FastAPI.
- Key Routes:
  - `/upload`: Accepts demo files.
  - `/predict`: Integrates ML model functionality.

### ML Backend
- Example TensorFlow model in `ml/model.py`
- Ready interface via `ml_routes.py`

---

## Local Setup

### Requirements
- Python 3.10+
- Node.js 16+

### Steps:
1. **Backend:**
   - Navigate to `backend/`.
   - Install dependencies: `pip install -r requirements.txt`
   - Run with `uvicorn app:app --reload`
2. **Frontend:**
   - Navigate to `frontend/`.
   - Install dependencies: `npm install`
   - Run with `npm start`
3. Access via browser at `http://localhost:3000`.

---

## Contribution
- Ensure your branch is updated with `origin/master`.
- Follow the guidelines given in `IMPLEMENTATION_GUIDE.md` to avoid merge conflicts.

---

**Happy Hacking!**