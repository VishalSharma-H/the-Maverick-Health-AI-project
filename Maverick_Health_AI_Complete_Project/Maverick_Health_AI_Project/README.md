# Maverick Health AI — Complete Project Folder

**Team:** The Mavericks  
**Project area:** AI in Healthcare  
**Primary SDG:** SDG 3 — Good Health and Well-being  
**Related SDGs:** SDG 9 — Industry, Innovation and Infrastructure; SDG 10 — Reduced Inequalities

## Team members
- Parth Sachan — S26CSEU3213
- Vishal Sharma — S26CSEU3224
- Abhyuday Bajpai — S26CSEU3218

## Project overview
Maverick Health AI is an educational prototype demonstrating three safeguards that can be applied when reviewing an AI-generated healthcare prediction: confidence checking, training-data coverage checking across patient groups, and patient-consent checking. The prototype flags cases that may need human review. It is **not a medical diagnosis system** and does not connect to a real medical AI model, hospital records, or a clinical database.

## Folder guide
| Folder | Contents |
|---|---|
| `01_Planning` | Original Milestone I SDG–Technology Mapping Canvas and problem identification |
| `02_Design` | Detailed Milestone II design documentation, architecture, workflow, data flow and UI wireframe |
| `03_Development` | Website source code and Python console demonstration |
| `04_Implementation` | How to run the prototype and implementation notes |
| `05_Testing` | Test cases and expected results |
| `06_Results` | Sample outputs and observations |
| `07_Conclusion_and_Future_Work` | Conclusion, limitations and proposed next steps |
| `08_Presentation_and_References` | Submission/presentation notes and source list |

## Run the website
Open `03_Development/Maverick_Health_AI.html` in a modern web browser. No installation or server is required for this front-end demonstration.

## Run the Python demonstration
Run `03_Development/maverick_health_ai_console.py` with Python 3:

```bash
python maverick_health_ai_console.py
```

## Important implementation note
The website uses illustrative, hard-coded training-data counts and rule thresholds (300 records and 80% confidence). These are demonstration values, not clinically validated standards. The Python file in this package is a companion console demonstration of the same described checks, included for coursework demonstration; the HTML website is the supplied working interface source.
