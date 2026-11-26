# Results and Observations

The prototype demonstrates that simple rule-based checks can flag three categories of concern before a healthcare prediction is considered: low confidence, limited training records for a patient group, and missing patient consent.

## Built-in sample observations
- **Dhruv:** Cancer prediction, 89% confidence, urban group, consent yes. No warnings; the interface displays the approved status with a doctor sign-off note.
- **Pawan:** Diabetes prediction, 66% confidence, children group, consent no. Three warnings are generated; the interface marks the case high risk and requires doctor review.
- **Manish:** Viral prediction, 95% confidence, elderly group, consent yes. The group has 200 illustrative records, below the 300 threshold, so a bias warning is generated and human review is requested.

## Observation
The example cases show how multiple safeguards can change the review status. The tool is a demonstration of checks, not a predictor of disease and not evidence of improved clinical outcomes.
