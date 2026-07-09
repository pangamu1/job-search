"""Placeholder template for resume_data.py.

Copy this file to resume_data.py and fill in your real details:
    cp resume_data.example.py resume_data.py

resume_data.py is gitignored so your personal data never gets committed.
Both build_resume.py (.docx) and build_html.py (PDF) import from the module,
so any edit here flows to both outputs. Keep it honest: only claims you can
defend in an interview, no invented numbers.
"""

CONTACT = {
    "name": "FIRST LAST",
    "title": "Senior Data Engineer",
    "location": "City, Country",
    "email": "you@example.com",
    "phone": "+1 555 000 0000",
    "linkedin_url": "https://www.linkedin.com/in/your-handle",
    "linkedin_text": "linkedin.com/in/your-handle",
    "github_url": "https://github.com/your-handle",
    "github_text": "github.com/your-handle",
}

SUMMARY = (
    "One tight paragraph. Who you are, years of experience, the two or three "
    "things you are strongest at, the domains you have worked in, and how you "
    "add value. No buzzwords, no invented metrics."
)

# (Category, comma-separated items). Keep project-only tools out of job bullets.
SKILLS = [
    ("Languages", "Python, SQL"),
    ("Data Processing", "PySpark, Databricks, Spark Structured Streaming"),
    ("Transformation & Modeling", "dbt, Dimensional modeling (Star / Snowflake), SCD Type 2, Medallion architecture"),
    ("Orchestration", "Apache Airflow, AWS Step Functions"),
    ("Cloud", "S3, Glue, Athena, Lambda, IAM, CloudWatch"),
    ("Data Quality & Governance", "Great Expectations, dbt tests, Unity Catalog"),
    ("IaC & CI/CD", "Terraform, Git, GitHub Actions, Docker"),
    ("BI & Analytics", "Power BI, Tableau, Excel, Pandas"),
    ("File Formats", "Parquet, Delta, JSON, CSV"),
    ("Ways of Working", "Agile / Scrum, JIRA, Confluence"),
]

EXPERIENCE = [
    {
        "role": "Job Title",
        "dates": "Mon YYYY – Mon YYYY",
        "company": "Company, City, ST",
        "bullets": [
            "Action verb + what you built + scope (real numbers only) + impact.",
            "Keep 4 to 6 bullets for a recent role, fewer for older roles.",
        ],
    },
    {
        "role": "Earlier Job Title",
        "dates": "Mon YYYY – Mon YYYY",
        "company": "Company, City, ST",
        "bullets": [
            "Two concise lines are enough for an early-career role.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Project Name",
        "url": "https://github.com/your-handle/project",
        "url_text": "github.com/your-handle/project",
        "stack": "Comma, separated, tech, stack",
        "bullets": [
            "What the project does and the interesting engineering in it.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "Master of Science, Computer Science",
        "dates": "YYYY – YYYY",
        "school": "University Name",
    },
]
