# 📊 Job Market Skills Analyzer

A real-world data analytics project that collects job market data, cleans and processes it, identifies in-demand technical skills, and presents job market insights through Excel and Power BI.

---

## 🚀 Project Overview

The **Job Market Skills Analyzer** helps analyze current job-market trends for Data Analyst opportunities.

The project collects job postings using the **Adzuna Job API**, processes the data with Python, extracts technical skills from job descriptions, and generates analytical reports.

The final insights are visualized using an interactive **Power BI dashboard**.

---

## 🎯 Objectives

- Collect real-world job market data
- Clean and prepare raw job data
- Extract technical skills from job descriptions
- Identify the most demanded skills
- Analyze hiring companies
- Analyze job locations
- Analyze common job titles
- Analyze salary information
- Export processed data to CSV and Excel
- Build a Power BI dashboard for visualization

---

## 🏗️ Project Architecture

```text
                Adzuna Job API
                      │
                      ▼
                scraper.py
                      │
                      ▼
             Raw Job Data
          CSV / Excel Files
                      │
                      ▼
                cleaner.py
                      │
                      ▼
            Cleaned Job Data
                      │
                      ▼
             skill_extractor.py
                      │
                      ▼
             Skills Identified
                      │
                      ▼
                 analyzer.py
                      │
                      ▼
            Job Market Analysis
                      │
             ┌────────┴────────┐
             ▼                 ▼
          Excel              CSV
             │
             ▼
        Power BI Dashboard
