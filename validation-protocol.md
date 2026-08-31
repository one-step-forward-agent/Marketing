# Validation protocol — falsifiable tests for the three JTBD

## V01 Context recovery
**Hypothesis:** qualified users lose enough time reconstructing work context that a source-linked recap creates repeated pull.  
**Pre-declared success:** ≥5 of 8 qualified concierge users save ≥10 self-timed minutes on a real return-to-task episode **and** ≥4 voluntarily bring a second episode within 14 days.  
**Failure/revise:** savings are trivial, source correction burden is high, or second-use pull is absent.

## V02 Decision support
**Hypothesis:** exposing criteria/evidence is more valuable than a generic LLM recommendation.  
**Test:** same live decision represented as generic answer vs criterion/evidence matrix.  
**Pre-declared success:** ≥60% prefer the evidence representation and ≥4 of 8 save/revisit the rationale later.  
**Failure/revise:** users only want a fast answer or do not revisit rationale.

## V03 Time feedback
**Hypothesis:** goal-vs-time evidence changes future planning and can become a weekly loop.  
**Pre-declared success:** ≥50% of 10 qualified users return for week 2 without manual chasing and ≥40% make a concrete priority/schedule change attributable to the report.  
**Failure/revise:** review feels like surveillance/admin or produces no behavioral change.

## Trust guardrail
Across all tests, unsupported/hallucinated evidence must remain below a pre-agreed correction threshold. Any privacy objection that blocks data connection is recorded as a product boundary signal, not dismissed as user error.
