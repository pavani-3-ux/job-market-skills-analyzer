import pandas as pd
from collections import Counter

# Read jobs with extracted skills
df = pd.read_csv("data/jobs_with_skills.csv")

print("=" * 60)
print("JOB MARKET SKILLS ANALYZER")
print("=" * 60)

print("\nTotal Jobs Collected:", len(df))


# --------------------------------------------------
# 1. TOP SKILLS ANALYSIS
# --------------------------------------------------

all_skills = []

for skills in df["skills"].fillna(""):
    skill_list = [
        skill.strip()
        for skill in skills.split(",")
        if skill.strip()
    ]
    all_skills.extend(skill_list)

skill_counts = Counter(all_skills)

skills_df = pd.DataFrame(
    skill_counts.items(),
    columns=["Skill", "Job_Count"]
).sort_values(by="Job_Count", ascending=False)

print("\nTOP 10 SKILLS IN DEMAND")
print("-" * 60)

if not skills_df.empty:
    print(skills_df.head(10).to_string(index=False))
else:
    print("No skills found.")


# --------------------------------------------------
# 2. TOP JOB LOCATIONS
# --------------------------------------------------

locations_df = (
    df["location"]
    .fillna("Unknown")
    .replace("", "Unknown")
    .value_counts()
    .reset_index()
)

locations_df.columns = ["Location", "Job_Count"]

print("\nTOP 10 JOB LOCATIONS")
print("-" * 60)
print(locations_df.head(10).to_string(index=False))


# --------------------------------------------------
# 3. TOP COMPANIES
# --------------------------------------------------

companies_df = (
    df["company"]
    .fillna("Unknown")
    .replace("", "Unknown")
    .value_counts()
    .reset_index()
)

companies_df.columns = ["Company", "Job_Count"]

print("\nTOP 10 COMPANIES")
print("-" * 60)
print(companies_df.head(10).to_string(index=False))


# --------------------------------------------------
# 4. TOP JOB TITLES
# --------------------------------------------------

titles_df = (
    df["title"]
    .fillna("Unknown")
    .replace("", "Unknown")
    .value_counts()
    .reset_index()
)

titles_df.columns = ["Job_Title", "Job_Count"]

print("\nTOP 10 JOB TITLES")
print("-" * 60)
print(titles_df.head(10).to_string(index=False))


# --------------------------------------------------
# 5. SALARY ANALYSIS
# --------------------------------------------------

df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")
df["average_salary"] = pd.to_numeric(
    df["average_salary"],
    errors="coerce"
)

salary_df = df[
    ["salary_min", "salary_max", "average_salary"]
].describe()

print("\nSALARY STATISTICS")
print("-" * 60)
print(salary_df.to_string())


# --------------------------------------------------
# SAVE ALL ANALYSIS INTO ONE EXCEL FILE
# --------------------------------------------------

with pd.ExcelWriter(
    "data/job_market_analysis.xlsx",
    engine="openpyxl"
) as writer:

    skills_df.to_excel(
        writer,
        sheet_name="Top Skills",
        index=False
    )

    locations_df.to_excel(
        writer,
        sheet_name="Top Locations",
        index=False
    )

    companies_df.to_excel(
        writer,
        sheet_name="Top Companies",
        index=False
    )

    titles_df.to_excel(
        writer,
        sheet_name="Top Job Titles",
        index=False
    )

    salary_df.to_excel(
        writer,
        sheet_name="Salary Statistics"
    )


print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("\nExcel file saved:")
print("data/job_market_analysis.xlsx")