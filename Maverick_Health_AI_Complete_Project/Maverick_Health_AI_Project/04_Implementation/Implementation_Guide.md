# Implementation Guide

## Website
1. Open the `Maverick_Health_AI.html` file in Chrome, Edge, Firefox or another modern browser.
2. The page loads with three illustrative sample cases.
3. Enter a patient name, prediction label, confidence percentage, patient group and consent status in the form.
4. Submit the form to run the three checks and display the decision and any warnings.
5. Use the clear-all control to reset the displayed cases.

## Python console companion
1. Install Python 3 if it is not already available.
2. Open a terminal in the `03_Development` folder.
3. Run `python maverick_health_ai_console.py`.
4. Enter the requested values. Type `exit` at the patient-name prompt to stop.

## Technologies
- HTML for page structure.
- CSS for visual styling.
- JavaScript for form handling, rule checks and dashboard updates.
- Python 3 for the simple console demonstration.

## Current scope
The website stores cases in browser memory while the page is open. It has no backend or persistent database. All counts and thresholds are illustrative.
