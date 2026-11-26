# Testing Plan and Test Cases

Testing is based on the rule logic in the supplied website source. The counts and thresholds are illustrative.

| Test | Confidence | Group | Consent | Expected warnings | Expected decision |
|---|---:|---|---|---|---|
| Dhruv sample | 89% | urban (900) | yes | None | Approved (doctor still signs off) |
| Pawan sample | 66% | children (120) | no | Low confidence, bias risk, privacy risk | High risk: doctor must review |
| Manish sample | 95% | elderly (200) | yes | Bias risk | Needs human review |
| Low confidence only | 65% | urban (900) | yes | Low confidence | Needs human review |
| Missing consent only | 90% | urban (900) | no | Privacy risk | Needs human review |

## Test procedure
1. Open the HTML file.
2. Confirm the three sample cases appear.
3. Enter a new case with values from the table.
4. Submit and compare the displayed warnings and decision with the expected result.
5. Use Clear All and confirm the case list and summary reset.

## Test status
The three named sample cases are preloaded by the supplied website code. The additional rows are manual test scenarios derived from the same rules and should be run during the demonstration. This document does not claim formal clinical validation or independent medical testing.
