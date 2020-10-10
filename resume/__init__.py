from datetime import datetime


class Resume:
    def __init__(self):
        # CONTACT INFO
        self.info = {
            "name": "Ross Mountjoy",
            "email": "ross.mountjoy@gmail.com",
            "phone": "540-501-5167",
            "location": "Washington DC",
            "can_start": datetime.utcnow().strftime("%x"),
            "github_profile": "https://github.com/rmountjoy92",
            "headshot": "static/images/ross.jpg",
        }

        # SKILLS
        self.skills = [
            {"name": "Python (3+)", "level": "advanced"},
            {"name": "jQuery", "level": "advanced"},
            {"name": "HTML5", "level": "advanced"},
            {"name": "CSS", "level": "advanced"},
            {"name": "Flask (for websites)", "level": "advanced"},
            {"name": "Flask (for APIs)", "level": "advanced"},
            {"name": "Linux/Bash", "level": "advanced"},
            {"name": "Linux Virtual Private Servers (VPS)", "level": "advanced"},
            {"name": "SQLAlchemy", "level": "advanced"},
            {"name": "Jinja2", "level": "advanced"},
            {"name": "Git/Github", "level": "advanced"},
            {"name": "Bootstrap CSS", "level": "advanced"},
            {"name": "Materialize CSS", "level": "advanced"},
            {"name": "Docker", "level": "advanced"},
            {
                "name": "Gunicorn, uWsgi, Waitress, Supervisor, etc.",
                "level": "advanced",
            },
            {"name": "Google search/Stack Overflow/Reading docs", "level": "advanced"},
            {"name": "ES6 Javascript", "level": "proficient"},
            {"name": "AWS RDS", "level": "proficient"},
            {"name": "AWS s3", "level": "proficient"},
            {"name": "AWS ECS/ECR", "level": "proficient"},
            {"name": "AWS EC2", "level": "proficient"},
            {"name": "AWS", "level": "proficient"},
            {"name": "NGINX", "level": "proficient"},
            {"name": "Socket-IO", "level": "proficient"},
            {"name": "Flutter/Dart", "level": "familiar"},
            {"name": "React/Vue/Angular", "level": "familiar"},
            {"name": "Android Development (Kotlin)", "level": "familiar"},
        ]

        # EDUCATION
        self.education = [
            {
                "years": 2,
                "major": "Software Engineering",
                "school": "Virginia Tech",
                "graduated": "N",
            },
            {
                "years": 2,
                "major": "Graphic Design/Business Management",
                "school": "Portland State",
                "graduated": "Y",
            },
        ]

        # EXPERIENCE
        self.experience = [
            {
                "date": "2019 - present",
                "title": "Co-owner",
                "company": "HomePrep.com",
                "duties": [
                    (
                        "Full-stack developer, managing all aspects from "
                        "design/development/deployment of the HomePrep web application"
                    ),
                    (
                        "HomePrep Stack: Linux (Ubuntu) VPS > NGINX > Supervisor > "
                        "Gunicorn > Flask > HTML5/Jinja2 front end using Materialize "
                        "CSS and jQuery"
                    ),
                    (
                        "Design all branding assets including logos, marketing"
                        " pieces, website, landing pages, etc."
                    ),
                    (
                        "Create/manage marketing campaigns (print/mail, social "
                        "media, events, etc)."
                    ),
                ],
                "achievements": [
                    (
                        "The HomePrep software has the following features: "
                        "https://airtable.com/shrb2GXArTZlWR1Q8/tblrvLI61zE3Gm80y"
                    ),
                ],
            },
            {
                "date": "2017 - present",
                "title": "Co-owner",
                "company": "Waterloo Investments",
                "duties": [
                    "Purchasing distressed properties to renovate and resale. ",
                    (
                        "Acquiring data from public and paid sources of people "
                        "that are likely to sell their distressed properties."
                    ),
                    (
                        "Built automation/scheduling services for acquiring the"
                        " data on VPS's using Python/Docker"
                    ),
                    (
                        "Write algorithms in Python that would aggregate, manipulate"
                        " and filter those lists based on conditions we had decided "
                        "upon to create mailing lists. "
                    ),
                    (
                        "Design all branding assets including logos, marketing"
                        " pieces, website, landing pages, etc."
                    ),
                    (
                        "Create/manage marketing campaigns (print/mail, social "
                        "media, events, etc)."
                    ),
                ],
                "achievements": [
                    (
                        "We've purchased/renovated/sold over 50 houses to "
                        "date, beginning in 2017."
                    ),
                ],
            },
            {
                "date": "2015 - present",
                "title": "Co-owner",
                "company": "Mountjoy Properties, Keller Williams",
                "duties": [
                    (
                        "Maintain a fleet of office desktop computers "
                        "(which I built from parts and used desktop Linux to save "
                        "on cost) and office printers."
                    ),
                    (
                        "Design all branding assets including logos, marketing"
                        " pieces, website, landing pages, etc."
                    ),
                    (
                        "Create/manage marketing campaigns (print/mail, social "
                        "media, events, etc)."
                    ),
                    (
                        "Taught classes on IT topics at a large Keller Williams office. "
                        "Convey somewhat complex IT topics to very unsaavy users."
                    ),
                    (
                        "Implement/maintain/build/teach software systems for lead"
                        " acquisition, lead automation, large multi-user CRM, "
                        "large mailing lists, SCRUM style task management,and more."
                    ),
                    (
                        "Oversee/manage all operations for real estate transactions, "
                        "managing vendors, the agents, and one other back "
                        "office employee."
                    ),
                ],
                "achievements": [
                    (
                        "Increased sales volume from $10m/year to $50/year in "
                        "first 3 years"
                    ),
                ],
            },
        ]

        # PERSONAL PROJECTS
        self.projects = [
            {
                "name": "DashMachine",
                "description": "The un-opinionated dashboard.",
                "urls": [
                    "https://github.com/rmountjoy92/DashMachine",
                    "https://github.com/rmountjoy92/DashMachine-0.7",
                ],
                "tech_used": [
                    "Flask",
                    "Docker",
                    "SQLAlchemy",
                    "HTML5/Jinja2",
                    "Bootstrap CSS",
                    "ES6 Javascript",
                    "Materialze CSS (old version)",
                    "jQuery (old version)",
                ],
                "achievements": [
                    "Has over 10 million (across different sources) downloads",
                    "600+ stars on Github",
                    "Featured on Awesome Selfhosted",
                ],
            },
            {
                "name": "AirtableCaching",
                "description": (
                    "Utility for caching api responses from the "
                    "airtable-python-wrapper and provides an ORM style "
                    "interface for querying cached records."
                ),
                "urls": [
                    "https://github.com/rmountjoy92/AirtableCaching",
                    "https://pypi.org/project/airtable-caching/",
                ],
                "tech_used": [
                    "Python",
                    "PyPi",
                ],
                "achievements": [
                    "Full test coverage, complete documentation",
                    "150+ downloads/mo on PyPi",
                ],
            },
            {
                "name": "This Website",
                "description": "Created in minutes using my custom Flask cookiecutter",
                "urls": [
                    "https://github.com/rmountjoy92/Portfolio",
                ],
                "tech_used": [
                    "Flask",
                    "Docker",
                    "SQLAlchemy",
                    "HTML5/Jinja2",
                    "Bootstrap CSS",
                    "ES6 Javascript",
                ],
                "achievements": [
                    "Is ready for scale with modular structure.",
                    "It took me 2 hours to make this entire website.",
                    "Rest API with auto-generated SwaggerUI documentation.",
                    "Run using included testing server, or build/run with Docker",
                ],
            },
        ]

        # HOBBIES
        self.hobbies = [
            {
                "name": "Self Hosting",
                "description": (
                    "Hosting services myself to avoid closed source SaaS applications. "
                    "This is done on a Ubuntu server in my basement using Docker. "
                    "Services include: Nextcloud (file sync), Bitwarden "
                    "(password manager), Jellyfin (Netflix like media server), "
                    "Custom Automation Services (like Zapier), this website, and more!"
                ),
            },
            {
                "name": "DIY Electronics",
                "description": (
                    "I have designed and built multiple DIY electronic devices, from "
                    "designing and having PCBs manufactured, to soldering components, "
                    "to 3D printing parts and cases. I have built a few micro laptops "
                    "and a few portable retro game emulator devices."
                ),
            },
            {
                "name": "Traditional Rock Climbing",
                "description": (
                    "Climbing large rock walls, placing the protection that you "
                    "clip the rope to in cracks/weaknesses in the rock as you climb. "
                    "I regularly scale Seneca Rocks in WV, which is a 300+ ft rock face."
                ),
            },
        ]

        # PITCH
        self.pitch = (
            "I am still employed by the businesses listed on this resume. "
            "The lead Realtor on my team is retiring to North Carolina, "
            "and has recommended to me that I begin to look for new employment. "
            "As for HomePrep, I maintain ownership in the company, "
            "but as the system is already built, my duties there do not"
            " consist of full-time work. "
            "Working on HomePrep, I've really fallen back in love with programming,"
            " and have decided to try out working in the industry. "
            "I can provide multiple references that will describe me as a highly"
            " motivated person with a knack for solving difficult problems. I am an"
            " avid googler that spends his free time learning new things. If there is"
            " not a skill listed above that you guys need from me, I can guarantee you"
            " that it will not take me long to gain it. Software Engineering is my"
            " passion, and I am very excited to start working in the industry."
        )

        # REFERENCES
        self.references = [
            {
                "title": "CEO HomePrep, Co-owner Waterloo Investments",
                "name": "Josh Snyder",
                "phone": "Email me for phone",
            },
            {
                "title": "CEO Mountjoy Properties, Co-owner Waterloo Investments",
                "name": "Rick Mountjoy",
                "phone": "Email me for phone",
            },
            {
                "title": "CEO Keller Williams McLean",
                "name": "Amina Basic",
                "phone": "Email me for phone",
            },
        ]
