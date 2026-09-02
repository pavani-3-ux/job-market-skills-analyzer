import pandas as pd
import re

# Read cleaned job data
df = pd.read_csv("data/cleaned_jobs.csv")

print("Total jobs:", len(df))

# Skills we want to identify
SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Machine Learning",
    "Data Analysis",
    "Data Analytics",
    "Pandas",
    "NumPy",
    "Statistics",
    "R",
    "Java",
    "AWS",
    "Azure",
    "Google Cloud",
    "ETL",
    "Data Visualization",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Spark",
    "Hadoop"
]


def extract_skills(text):
    """
    Finds skills from a job description.
    """
    
    if pd.isna(text):
        return []

    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# Extract skills from every job description
df["skills"] = df["description"].apply(extract_skills)

# Convert list to readable text
df["skills"] = df["skills"].apply(lambda skills: ", ".join(skills))

# Save results
df.to_csv("data/jobs_with_skills.csv", index=False)
df.to_excel("data/jobs_with_skills.xlsx", index=False)

print("\nSkill extraction completed!")
print("CSV saved: data/jobs_with_skills.csv")
print("Excel saved: data/jobs_with_skills.xlsx")

# Show first few results
print("\nSample Results:")
print(df[["title", "skills"]].head())