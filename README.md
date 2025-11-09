# Bright Bubbles TV – Data Engineering Portfolio

**4.4K views • 13× CTR • 17 VPH** — all from **data-driven content optimization**

## Pipeline Overview


1. **`1_ingest.py`** – Pulls 33 videos via YouTube Data API v3  
2. **`2_transform.py`** – Calculates **Views Per Hour (VPH)** & **CTR multiplier**  
3. **`gold_bright_bubbles.parquet`** – Clean, analytics-ready gold layer  
4. **Power BI** – Interactive dashboard (free Desktop)

---

## Key Results
| Metric | Value |
|-------|-------|
| Top Video | *"Learn Addition with Music!"* |
| Views | **4,400** |
| CTR Multiplier | **13×** average |
| Latest VPH | **17** |

---

## Run It Yourself
```bash
pip install pandas requests pyarrow
python 1_ingest.py && python 2_transform.py
