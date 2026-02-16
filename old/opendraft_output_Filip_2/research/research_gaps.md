# Research Gap Analysis & Opportunities

**Topic:** Optimization of Emergency Medical Services (EMS/PRM) in Poland
**Papers Analyzed:** 3 (Representative sample of 19)
**Analysis Date:** October 26, 2023

---

## Executive Summary

**Key Finding:** The Polish EMS (PRM) system is at a critical pivot point between a legacy "Physician-Centric" model and a future "Tele-Supported Paramedic" model. While Paper 1 forecasts massive economic benefits (10M PLN savings) from this shift, there is a **critical lack of empirical validation** regarding patient safety outcomes and technological reliability in the rural areas identified as vulnerable in Paper 2.

**Recommendation:** Move beyond economic forecasting. Research should focus on the **technological and operational feasibility** of replacing Specialist (S) teams with Basic (P) teams supported by telemedicine, specifically in rural "connectivity blind spots."

---

## 1. Major Research Gaps

### Gap 1: The "Connectivity vs. Necessity" Paradox
**Description:** Paper 1 proposes telemedicine to solve staffing shortages. Paper 2 identifies rural areas as having the longest response times and highest need for support. However, no paper overlays **cellular network coverage maps** with **rural EMS incident data**.
**Why it matters:** If the areas with the worst doctor shortages (rural) also have the worst 5G/LTE coverage, the proposed solution (telemedicine) will fail where it is needed most.
**Evidence:** Paper 1 assumes connectivity; Paper 2 highlights rural logistical friction.
**Difficulty:** 🟡 Medium (Requires GIS data integration)
**Impact potential:** ⭐⭐⭐⭐⭐

**How to address:**
- **GIS Study:** Overlay map of "White spots" (poor coverage) with map of "Prolonged Response Times" (from SWD PRM data).
- **Simulation:** Stress-test the Renk/Letkiewicz model (Paper 1) assuming 15% connection failure rates.

### Gap 2: Clinical Outcome Data for Tele-EMS
**Description:** Paper 1 provides *financial* forecasts. There is a total absence of *clinical* outcome data comparing "Paramedic + Tele-doctor" vs. "Physical Doctor" in the Polish context.
**Why it matters:** Cost savings are irrelevant if mortality rates in complex cases (e.g. Severe toxicology as per Paper 3) increase.
**Evidence:** Paper 1 is a forecast/model, not a clinical trial.
**Difficulty:** 🔴 High (Requires hospital outcome data linkage)
**Impact potential:** ⭐⭐⭐⭐⭐

**How to address:**
- **Retrospective Cohort:** Compare outcomes of Basic (P) teams consulting doctors by radio vs. Specialist (S) teams for specific conditions (e.g. Stroke, AMI).

### Gap 3: The "Post-Reform" Operational Landscape
**Description:** Papers 2 and 3 rely on data from 2011–2014. The Polish EMS system underwent massive centralization and digitization (SWD PRM) post-2016.
**Why it matters:** Older papers discuss communication disjoints that may have already been solved by SWD PRM, or created new bottlenecks not yet documented.
**Evidence:** Paper 2 cites legal frameworks from 2014; Paper 3 uses 2011-2013 data.
**Difficulty:** 🟢 Low (Update via recent government reports/stats)
**Impact potential:** ⭐⭐⭐⭐

---

## 2. Emerging Trends (2023-2024)

### Trend 1: Demedicalization of Ambulance Teams
**Description:** A shift from "bringing the hospital to the patient" (doctor on board) to "bringing the patient to the hospital" (paramedic led).
**Evidence:** Paper 1 (2023) explicitly advocates for reducing physician presence to 10% of current levels.
**Maturity:** 🟡 Growing (Policy stage, moving to implementation)
**Opportunity:** Analyze the *psychological* impact of this shift on paramedics who suddenly bear more responsibility.

### Trend 2: Cross-Service Integration (KSRG + PRM)
**Description:** Increasing reliance on Firefighters (KSRG) as medical First Responders due to ambulance shortages.
**Evidence:** Paper 2 establishes the baseline; current trends suggest this reliance has deepened post-COVID.
**Maturity:** 🟢 Established (But data is outdated)
**Opportunity:** Evaluate the "Scope of Practice" friction—are firefighters being asked to perform medical acts beyond their KPP (Qualified First Aid) training?

---

## 3. Unresolved Questions & Contradictions

### Debate 1: The "Platinum Ten" vs. "Tele-Consultation"
**Position A:** Paper 2 emphasizes speed ("Platinum Ten minutes") and immediate physical intervention by firefighters/paramedics.
**Position B:** Paper 1 emphasizes remote consultation time.
**Why it's unresolved:** Does the time taken to set up a live stream and consult a remote doctor eat into the critical "Platinum Ten" minutes? There is a trade-off between *speed of transport* and *accuracy of on-scene diagnosis*.
**How to resolve:** Time-motion study of ambulance teams using tele-consultation vs. standard protocols.

### Debate 2: Toxicology Management
**Position A:** Paper 3 shows high volume of alcohol/drug cases requiring airway management.
**Position B:** Paper 1 suggests removing doctors.
**Unresolved:** Can paramedics (P-teams) legally and technically manage severe airway compromises in combative toxicology patients without a physical doctor present, relying only on a screen?

---

🔴 **DOMAIN-CRITICAL GAPS DETECTED**

**EMS / Public Health Papers - Missing Discussions:**

1. **System Wspomagania Dowodzenia (SWD PRM)**
 * Paper 2 discusses dispatch issues but predates the full SWD PRM rollout.
 * **Must Address:** Any modern analysis *must* account for how this centralized digital system changed dispatch logic.

2. **Seasonal Confounding**
 * Paper 3 mentions seasonality in toxicology.
 * **Must Address:** EMS demand is highly seasonal (flu season, summer accidents). Any staffing model (like Paper 1) must account for peak-load variance, not just average costs.

3. **Legal Definition of "Remote" Medical Acts**
 * Paper 1 mentions legal barriers.
 * **Must Address:** Who is liable if the connection drops during a tele-guided procedure? The paramedic or the remote doctor?

---

## 4. Methodological Opportunities

### Underutilized Methods
1. **Discrete Event Simulation (DES):** Use software (e.g., Arena, AnyLogic) to model the Paper 1 proposal. Input: Call arrival rates, Service times, 5G failure rates. Output: System failure probability.
2. **Geospatial Analysis (GIS):** Mapping 15-minute isochrones for ambulances vs. fire trucks (building on Paper 2) using 2023 road network data.

### Datasets Not Yet Explored
1. **GUS (Statistics Poland) 2022-2023 Health Reports:** Post-pandemic ambulance utilization data.
2. **NFZ (National Health Fund) Billing Data:** To verify the cost assumptions made in Paper 1.

---

## 5. Interdisciplinary Bridges

### Connection: Telecommunications Engineering ↔️ Emergency Medicine
**Observation:** Medical papers (Paper 1) assume "live streaming" is available. Engineering papers know that rural bandwidth is volatile.
**Opportunity:** Collaborate with network engineers to map "Digital Exclusion Zones" and correlate them with "Medical Exclusion Zones."

---

## 6. Your Novel Research Angles

Based on this analysis, here are **3 promising directions**:

### Angle 1: The "Digital Exclusion" Risk in EMS Modernization
**Gap addressed:** The assumption that technology works everywhere (Gap 1).
**Novel contribution:** Empirically identifying regions where the "Tele-Doctor" model (Paper 1) is physically impossible due to infrastructure.
**Why promising:** Directly challenges the optimism of recent reforms with hard engineering data.
**Proposed approach:**
1. Obtain coverage maps for major Polish carriers (Orange, Play, Plus, T-Mobile).
2. Obtain rural EMS intervention coordinates (or density maps).
3. Perform spatial intersection analysis.
**Expected contribution:** A "Risk Map" showing where the new EMS model will fail.

### Angle 2: The Economic-Clinical Trade-off Analysis
**Gap addressed:** Lack of clinical context in economic forecasts (Gap 2).
**Novel contribution:** Calculating the "Cost per Life Saved" rather than just "Operational Cost Savings."
**Why promising:** Policymakers love cost savings; clinicians fear patient harm. This bridges the debate.
**Proposed approach:**
1. Take the 10M PLN savings figure (Paper 1).
2. Model the cost of potential adverse events (e.g. Missed diagnosis due to video lag).
3. Determine the "Break-even point" where litigation/treatment costs outweigh operational savings.

### Angle 3: The "Firefighter-Medic" Capability Gap
**Gap addressed:** Updating the 2014 data on Firefighter integration (Paper 2).
**Novel contribution:** Assessing if current KPP (First Aid) training is sufficient for the *actual* cases firefighters face (e.g. The toxicology cases from Paper 3).
**Proposed approach:**
1. Review KPP training curriculum.
2. Compare against top 5 EMS diagnoses (from Paper 3 and newer reports).
3. Identify "Skill Gaps" (e.g. Handling opioid overdose/Narcan administration).

---

## 7. Next Steps Recommendations

**Immediate actions:**
1. [ ] **Verify:** Check if the "Tele-EMS" model has been legally ratified in Poland since the 2023 paper.
2. [ ] **Search:** Find a paper detailing the technical specifications of the SWD PRM system (crucial context).
3. [ ] **Data Check:** Look for "GUS - Emergency rescue services in 2022" report for updated statistics.

**Short-term:**
1. [ ] Draft a problem statement focusing on "The dependency of EMS modernization on rural digital infrastructure."
2. [ ] Read up on "Telemedicine liability laws in Poland."

---

## Confidence Assessment

**Gap analysis confidence:** 🟢 High (The contrast between economic theory and operational reality is stark).
**Trend identification:** 🟡 Medium (Sample size is small; need to confirm if other 2023 papers support the Tele-EMS trend).
**Novel angle viability:** 🟢 High (The GIS/Infrastructure angle is very publishable).