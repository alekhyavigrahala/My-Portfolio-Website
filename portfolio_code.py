import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import base64

st.set_page_config(layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/321820b2-d292-42f5-b514-49ca6959cd83/keTD5NYFqz.json")
lottie_contact = load_lottieurl("https://lottie.host/6b83d313-9187-448f-8419-1f0f725b80f9/HnWuic28EA.json")
image_task = Image.open("Portfolio Attachments/Task Management System.jpg")
image_project = Image.open("Portfolio Attachments/Project Management System.jpg")
image_verbal = Image.open("Portfolio Attachments/Verbal Quest.png")
image_space = Image.open("Portfolio Attachments/space and aesthetic system.png")
image_profile = Image.open("Portfolio Attachments/VigrahalaAlekhya Photo.jpeg")
image_klu = Image.open("Portfolio Attachments/KLU logo.png")
image_srisarada = Image.open("Portfolio Attachments/sri sarada logo.png")
image_srichaitanya = Image.open("Portfolio Attachments/sri chaitanya logo.png")


st.subheader(":pray: Welcome to")
st.title("Alekhya's Portfolio Website")
st.write("""
This portfolio provides a comprehensive view of my academic background, technical skills, professional experiences, and projects. 
It includes details of my education, internships, certifications, and hands-on work in areas such as data analytics, software development, 
and problem-solving. The goal of this portfolio is to showcase my journey as a Computer Science undergraduate and demonstrate 
my ability to apply knowledge to real-world challenges.
""")
st.write("[LinkedIn](https://www.linkedin.com/in/alekhya-vigrahala/) &nbsp; | &nbsp; [GitHub](https://github.com/alekhyavigrahala) &nbsp; | &nbsp; [HackerRank](https://www.hackerrank.com/profile/KLU_2100030599)")
st.write('---')

# Initialize a session_state variable to track if a tab has been clicked
if 'tab_clicked' not in st.session_state:
    st.session_state.tab_clicked = False

def on_tab_change(key):
    st.session_state.tab_clicked = True
    st.session_state.selected_tab = st.session_state[key]

if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = None

selected = option_menu(
    menu_title=None,
    options=['About','Experience','Projects','Skills','Certifications','Contact'],
    icons=['person','briefcase','file-earmark-code-fill','code-slash','award','chat-left-text-fill'],
    orientation='horizontal',
    on_change=on_tab_change,
    key="portfolio_menu",
    default_index=-1
)

if st.session_state.tab_clicked:
    if st.session_state.selected_tab == 'About':
        with st.container():
            col1, col2 = st.columns((2,0.7))
            with col1:
                st.write("")
                st.write("")
                st.header("Hello, I'm Alekhya Vigrahala")
                st.write("")
                st.markdown("<p style='font-size:18px;'>A Computer Science undergraduate from K L University with a strong foundation in programming, software development, and data analytics. My technical journey includes building full-stack applications with Python, Java, Spring Boot, Django, React, and MySQL, and developing data visualization solutions using Tableau and Power BI. I gained practical exposure through virtual internship programs with Deloitte, Quantium, and BCG, where I worked on analytics and consulting tasks, and I hold certifications in AWS, Oracle Cloud, Red Hat, and Salesforce AI. Along with my technical skills, I bring strengths in problem-solving, testing, teamwork, and adaptability, and I aspire to contribute to impactful software and data-driven solutions in the industry..</p>", unsafe_allow_html=True)
            with open("Portfolio Attachments/ALEKHYAVIGRAHALA_RESUME.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(
                label="📄 Download My Resume",
                data=PDFbyte,
                file_name="ALEKHYAVIGRAHALA_RESUME.pdf",
                mime="application/pdf",
            )


            with col2:
                st.write("")
                st.write("")
                st.image(image_profile, width=230)

        st.write("---")

        st.markdown("""
        <div style='text-align:center;'>
            <h1>My Education</h1>
        </div>
        """, unsafe_allow_html=True)
        st.write("##")

        # KL University
        col7, col1, col2 = st.columns([0.2, 1, 2])
        with col1:
            st.write("")
            st.image(image_klu, width=190)
        with col2:
            st.subheader("Bachelor of Technology (B.Tech)")
            st.markdown("<p style='font-size:21px;'><b>K L University</b>, Vijayawada</p>", unsafe_allow_html=True)
            st.markdown("""    
            **Specialization:** &nbsp;Computer Science and Engineering  
            **Year of Graduation:** &nbsp;May 2025  
            **Grade:** &nbsp;8.86 CGPA  
            **Website:** &nbsp;[https://www.kluniversity.in/](https://www.kluniversity.in/)
            """)

        st.write("---")

        # Sri Sarada Junior College
        col8, col3, col4 = st.columns([0.2, 1, 2])
        with col3:
            st.write("")
            st.image(image_srisarada, width=150)
        with col4:
            st.subheader("Higher Secondary Education - MPC")
            st.markdown("<p style='font-size:21px;'><b>Sri Sarada Junior College</b>, Vijayawada</p>", unsafe_allow_html=True)
            st.markdown("""  
            **Stream:** &nbsp;MPC (Maths Physics Chemistry)  
            **Board:** &nbsp;Board of Intermediate Education, Andhra Pradesh  
            **Year of Completion:** &nbsp;May 2021  
            **Grade:** &nbsp;75%  
            **Website:** &nbsp;[https://www.saradaedu.com/](https://www.saradaedu.com/)
            """)

        st.write("---")

        # Sri Chaitanya High School
        col9, col5, col6 = st.columns([0.2, 1, 2])
        with col5:
            st.write("")
            st.image(image_srichaitanya, width=150)
        with col6:
            st.subheader("Secondary Education")
            st.markdown("<p style='font-size:21px;'><b>Sri Chaitanya High School</b>, Vijayawada</p>", unsafe_allow_html=True)
            st.markdown("""    
            **Board:** &nbsp;Board Of Secondary Education Andhra Pradesh  
            **Year of Completion:** &nbsp;April 2019  
            **Grade:** &nbsp;87%  
            **Website:** &nbsp;[https://srichaitanya.net/](https://srichaitanya.net/)
            """)


    elif st.session_state.selected_tab == 'Projects':
        with st.container():
            st.write("")
            st.title("My Projects")
            st.write("")

            projects = [
                (
                    image_task,
                    "Task Management System",
                    """Developed a full-stack Task Management System (To-Do List application) using Spring Boot, Java, and MySQL, enabling users to create, update, and delete tasks. The project streamlined user interactions by integrating both front-end and back-end components, providing an efficient and seamless task management experience.""",
                    "https://www.linkedin.com/posts/puli-rishitha_sdp3-jfsd-kluniversity-ugcPost-7102548170735325184-ZqTs?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADihrLYB7viNBC-ZcUijXzaplJGEKjukBMU"
                ),
                (
                    image_project,
                    "Project Management System",
                    """Developed a Project Management System using Django, Python, and MySQL, implementing back-end functionality for efficient data handling and managing databases to support project planning and lifecycle management, resulting in a user-focused and effective project management solution.""",
                    "https://www.linkedin.com/pulse/project-management-system-pjm-team51-yakshitha-kallam"
                ),
                (
                    image_verbal,
                    "Verbal Quest",
                    """Developed Verbal Quest, a Python-based word-guessing game where players try to discover a hidden 5-letter word using logic-based clues. Implemented game logic, feedback for guesses, and scoring to create an engaging and interactive experience, showcasing skills in Python programming and problem-solving.""",
                    "https://github.com/alekhyavigrahala/Python-Projects/tree/main/Project-1%20%3A%20Verbal%20Quest"
                ),
                (
                    image_space,
                    "Space and Aesthetic System",
                    """Developed the Space and Aesthetic Management System as part of a research-driven project, conducting surveys, interviews, and fieldwork to analyze customer needs in interior design. Designed user personas, identified key insights, and proposed customer-centric solutions that balanced quality, budget, and creativity, emphasizing innovation and user-focused design.""",
                    "https://www.linkedin.com/pulse/space-aesthetic-management-sdp-1-team-78-yakshitha-kallam"
                )
            ]

            for img, title, desc, link in projects:
                col1, col2 = st.columns((1, 2))
                with col1:
                    st.image(img, use_column_width=True)
                with col2:
                    st.subheader(title)
                    st.write(desc)
                    st.markdown(f"[Project Link]({link})")
                st.write("---")  # divider between projects

    elif st.session_state.selected_tab == "Contact":
        st.write("")
        st.title("Get in Touch...")
        st.write("##")

        contact_form = """
        <div style='
            background: #f8f9fa; 
            padding: 30px; 
            border-radius: 20px; 
            box-shadow: 5px 5px 20px rgba(0,0,0,0.1);
        '>
            <form action="https://formsubmit.co/alekhyavigrahala21@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your Name" required style='width:100%; padding:12px; margin-bottom:15px; border-radius:10px; border:1px solid #ccc;'>
                <input type="email" name="email" placeholder="Your Email" required style='width:100%; padding:12px; margin-bottom:15px; border-radius:10px; border:1px solid #ccc;'>
                <textarea name="message" placeholder="Your Message" required style='width:100%; padding:12px; margin-bottom:15px; border-radius:10px; border:1px solid #ccc; min-height:120px;'></textarea>
                <button type="submit" style='
                    background-color:#4CAF50; 
                    color:white; 
                    padding:12px 25px; 
                    border:none; 
                    border-radius:12px; 
                    cursor:pointer; 
                    font-size:16px;
                    transition:0.3s;
                ' onmouseover="this.style.backgroundColor='#45a049'" onmouseout="this.style.backgroundColor='#4CAF50'">
                    Send Message
                </button>
            </form>
        </div>
        """

        left_col, right_col = st.columns((1,1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_contact, height=400)


    elif st.session_state.selected_tab == "Skills":
        st.write("")
        st.markdown("""
        <div style='text-align:center;'>
            <h1>My Technical Skills</h1>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.write("")

        skills = [
            ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
            ("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"),
            ("C", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/C_Programming_Language.svg/1200px-C_Programming_Language.svg.png"),
            ("HTML", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"),
            ("CSS", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"),
            ("JavaScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"),
            ("MySQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"),
            ("Linux", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"),
            ("AWS", "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg"),
            ("GitHub", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png"),
            ("MS Office", "https://www.m-files.com/wp-content/uploads/2025/02/logo-microsoft-office.png"),
            ("Power BI", "https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg"),
            ("Tableau", "https://img.icons8.com/color/512/tableau-software.png")
        ]

        rows = (len(skills) + 3) // 4  # 4 skills per row
        for i in range(rows):
            cols = st.columns(4)
            for j, col in enumerate(cols):
                idx = i*4 + j
                if idx < len(skills):
                    name, icon_url = skills[idx]
                    col.markdown(f"""
                    <div style='
                        background: linear-gradient(135deg, #e0f7fa, #80cbc4);
                        border-radius:20px; 
                        padding:25px; 
                        margin:10px; 
                        text-align:center; 
                        box-shadow: 5px 5px 15px rgba(0,0,0,0.1); 
                        transition: transform 0.3s ease;
                        display:flex;
                        flex-direction:column;
                        justify-content:center;
                        align-items:center;
                        height:150px;
                    ' onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        <img src='{icon_url}' style='width:60px; height:60px; object-fit:contain; margin-bottom:10px;'>
                        <p style='margin:0; font-weight:bold; font-size:18px; color:#333'>{name}</p>
                    </div>
                    """, unsafe_allow_html=True)

    elif st.session_state.selected_tab == 'Experience':
        st.write("")
        st.markdown("""
        <div style='text-align:center;'>
            <h1>My Work Experience</h1>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.write("")

        experiences = [
            (
                "Data Strategy & AI Applications",
                "Deloitte Australia - Virtual Experience Program",
                "August 2025",
                "Completed Deloitte's program focusing on data strategy, AI applications, and digital transformation. Applied knowledge to real-world business scenarios to enhance analytical skills.",
                "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_aHgfioFxmJykuCJsa_1755997495116_completion_certificate.pdf"

            ),
            (
                "Strategy & Business Analytics",
                "Boston Consulting Group (BCG) - Virtual Experience Program",
                "July 2023",
                "Participated in BCG's program working on strategic problem-solving, market analysis, and business case studies. Developed analytical thinking and consulting skills.",
                "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/BCG%20/ntTvo6ru6Tq3A2JPq_BCG_Y55o9NpxjpAxuznZ6_1690437731870_completion_certificate.pdf"
            ),
            (
                "Data Analytics & Insights",
                "Quantium - Virtual Experience Program",
                "July 2023",
                "Completed Quantium's program focusing on real-world data analysis, data visualization, and business insights. Gained hands-on experience in statistical analysis and problem-solving for data-driven decisions.",
                "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Quantium/NkaC7knWtjSbi6aYv_Quantium_Y55o9NpxjpAxuznZ6_1690433143669_completion_certificate.pdf"
            )
        ]

        rows = (len(experiences) + 1) // 2
        for i in range(rows):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                idx = i*2 + j
                if idx < len(experiences):
                    title, company, duration, desc, cert_link = experiences[idx]
                    col.markdown(f"""
                    <div style='
                        border: 1px solid #ddd; 
                        border-radius: 10px; 
                        padding: 20px; 
                        margin: 10px 0; 
                        box-shadow: 3px 3px 15px rgba(0,0,0,0.1); 
                        display: flex; 
                        flex-direction: column; 
                        justify-content: space-between; 
                        height: 300px; 
                        width: 100%;'>
                        <div style='overflow: auto;'>
                            <h3 style='margin-bottom:5px;'>{title}</h3>
                            <h5 style='margin-top:0; color:gray;'>{company} | {duration}</h5>
                            <p>{desc}</p>
                        </div>
                        <div>
                            <a href='{cert_link}' target='_blank'>View Certificate</a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    elif st.session_state.selected_tab == 'Certifications':
        st.write("")
        st.markdown("""
        <div style='text-align:center;'>
            <h1>My Certifications</h1>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.write("")

        certifications = [
            ("https://1000logos.net/wp-content/uploads/2020/09/Red-Hat-Logo-2019.png",
            "Red Hat Certified Enterprise Application Developer","Red Hat","29-12-2023",
            "Portfolio Attachments/Red Hat Certified Enterprise Application Developer.pdf"),
            
            ("https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
            "AWS Certified Cloud Practitioner","Amazon Web Services","28-11-2023",
            "Portfolio Attachments/AWS Certified Cloud Practitioner.pdf"),
            
            ("https://logos-world.net/wp-content/uploads/2020/09/Oracle-Logo.png",
            "Oracle Cloud Infrastructure 2023 Certified Architect Associate","Oracle","28-08-2023",
            "Portfolio Attachments/Oracle Cloud Infrastructure 2023 Certified Architect Associate.pdf"),
            
            ("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Salesforce.com_logo.svg/1024px-Salesforce.com_logo.svg.png",
            "Salesforce Certified AI Associate","Salesforce","24-10-2024",
            "Portfolio Attachments/Salesforce Certified AI Associate.pdf"),
            
            ("https://images.squarespace-cdn.com/content/v1/5bec669f9f877016e7212b2d/6fa34e92-787f-46dd-b69b-afbdd86350ce/Simplilearn-logo300x100PNG+%281%29.png",
            "Power BI Essentials and Data Visualization","Simplilearn","05-08-2025",
            "Portfolio Attachments/PowerBI_CourseCompletion_Certificate.pdf"),
            
            ("https://internet2.edu/wp-content/uploads/2021/04/s-palo-alto-gallery.png",
            "Palo Alto Networks Certified Cybersecurity Fundamentals Professional","Palo Alto Networks","25-03-2025",
            "Portfolio Attachments/Palo Alto Networks Certified Cybersecurity Fundamentals Professional.pdf")
        ]

        st.markdown("""
        <style>
        .cert-card {
            background: linear-gradient(135deg, #ffffff, #e0f7fa);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 280px;
        }
        .cert-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 25px rgba(0,0,0,0.2);
        }
        .cert-logo {
            width: 80px;
            height: 80px;
            object-fit: contain;
            margin: 0 auto 15px auto;
        }
        .cert-name {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
            color: #00796b;
        }
        .cert-org {
            font-size: 14px;
            color: #555;
            margin-bottom: 15px;
        }
        .download-btn a {
            text-decoration: none;
            color: #ffffff;
            background-color: #00796b;
            padding: 8px 15px;
            border-radius: 8px;
            font-size: 14px;
        }
        .download-btn a:hover {
            background-color: #004d40;
        }
        </style>
        """, unsafe_allow_html=True)

        cols_per_row = 3
        rows = (len(certifications) + cols_per_row - 1) // cols_per_row

        for i in range(rows):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                idx = i * cols_per_row + j
                if idx < len(certifications):
                    logo, name, org, date, pdf_path = certifications[idx]
                    with open(pdf_path, "rb") as f:
                        pdf_bytes = f.read()
                    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

                    col.markdown(f"""
                    <div class='cert-card'>
                        <div style='width:100px; height:100px; display:flex; align-items:center; justify-content:center; margin:0 auto 15px auto;'>
                            <img src='{logo}' style='max-width:100%; max-height:100%; object-fit:contain;'>
                        </div>
                        <div class='cert-name'>{name}</div>
                        <div class='cert-org'>{org} | {date}</div>
                        <div class='download-btn'>
                            <a href='data:application/pdf;base64,{pdf_base64}' download='{name}.pdf'>View Certificate</a>
                        </div>
                    </div>
                    <br>
                    """, unsafe_allow_html=True)