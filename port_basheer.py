import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Basheer Shaik Portfolio", page_icon="💼", layout="wide")

# --- HERO SECTION ---
st.markdown(
    """
    <style>
    .hero {
        text-align: center;
        padding: 40px 0;
    }
    .hero h1 {
        font-size: 3rem;
        color: #0A66C2;
    }
    .hero p {
        font-size: 1.2rem;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>Basheer Shaik</h1>
        <p>Data Analyst | Python Developer | Machine Learning Enthusiast</p>
        <p>📍 Hyderabad, India</p>
        <p>
            <a href="https://www.linkedin.com/in/basheer-shaik-473949300" target="_blank">LinkedIn</a> |
            <a href="https://github.com/Basheershaik2002" target="_blank">GitHub</a> |
            <a href="mailto:basheershaik7013@gmail.com">Email</a> |
            <a href="https://basheer-shaik-hxvmj33.gamma.site/" target="_blank">Portfolio</a>
        </p>
    </div>
    """, unsafe_allow_html=True
)

st.write("---")

# --- EXPERIENCE ---
st.header("💼 Experience & Internships")
experience_list = [
    ("Data Analysis & Visualization Intern – Accenture", "Jan 2025 – Feb 2025", 
     "Built dashboards using Power BI and Tableau after cleaning datasets in Excel."),
    ("Data Analysis Intern – TCS iON", "Nov 2024 – Dec 2024", 
     "Performed data cleaning and analysis using Python & Excel, improving report accuracy by 25%."),
    ("Data Science & Analytics Intern – HP", "Sep 2024 – Oct 2024", 
     "Developed predictive models and Power BI dashboards, reducing reporting time by 30%."),
    ("Python Developer Intern – Internshala", "Apr 2024 – Jul 2024", 
     "Automated data collection and cleaning with Python, improving processing time by 30%.")
]
for title, dates, desc in experience_list:
    st.subheader(title)
    st.write(f"**{dates}**")
    st.write(desc)

st.write("---")

# --- PROJECTS ---
st.header("📂 Projects")
projects = [
    ("Sentiment Analysis for Product Rating", "Analyzed keywords in comments to determine sentiment using database keyword matching."),
    ("World Sustainability Analysis – Climate Change & Net Zero Emission", "Applied statistical analysis and machine learning to model global climate initiatives."),
    ("Sales Performance Analysis", "Identified low-performing products and monitored KPIs with Power BI dashboards.")
]
for title, desc in projects:
    st.subheader(title)
    st.write(desc)

st.write("---")

# --- SKILLS ---
st.header("🛠 Skills")
skills = [
    "Python", "Excel", "SQL", "Power BI", "MySQL", "SQLite",
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn",
    "Communication", "Team Collaboration", "Critical Thinking"
]
st.write(", ".join(skills))

st.write("---")

# --- CERTIFICATIONS ---
st.header("📜 Certifications")
certs = [
    "Data Analysis and Visualization – Accenture",
    "Data Science & Analytics – HP",
    "Data Analyst – IBM",
    "TCS Ion Career Edge – Young Professional – TCS",
    "ChatGPT & AI Tools Expert – Dr. Finance",
    "Python – Naresh IT",
    "Internet of Things (IoT) – SkillDzire",
    "Data Analytics – Google",
    "Data Analyst – Deloitte",
    "AI Engineer",
    "SQL",
    "Excel",
    "Python – Unstop"
]
st.write(", ".join(certs))

st.write("---")

# --- EDUCATION ---
st.header("🎓 Education")
st.subheader("B.Tech in Electronics and Communication Engineering")
st.write("Narasaraopeta Engineering College, 2020 – 2024 | CGPA: 6.69")

st.write("---")

# --- CONTACT ---
st.header("📬 Contact")
st.write("📧 Email: basheershaik7013@gmail.com")
st.write("🔗 LinkedIn: [Profile](https://www.linkedin.com/in/basheer-shaik-473949300)")
st.write("💻 GitHub: [Profile](https://github.com/Basheershaik2002)")
st.write("🌐 Portfolio: [Website](https://basheer-shaik-hxvmj33.gamma.site/)")

st.write("© 2025 Basheer Shaik | Designed with Streamlit")
