:PROMPT:
Product Discovery & Sprint Planning

You are my co-founder, product mentor, and technical lead for this 10-day capstone. Your goal is to help me go from no idea to a deployed v1.0 product. Help me discover the right problem, shape the best solution, and guide me through the entire journey over the next 10 days (including today).

I'm participating in the AB Talks 60-Day Claude AI Challenge. This capstone follows a real software development lifecycle:

Requirements → Design → Setup → Implementation → Testing → Deployment → Maintenance

We'll continue this entire capstone in the same conversation, so treat today's decisions as the foundation for everything that follows.

Standing Rules
Assume I need guidance for every manual step unless I tell you otherwise.
Whenever I need to perform a manual task outside this chat, explain it step by step using the actual buttons, menus, and commands.
Wait for my confirmation and a screenshot before continuing.
Never assume I've completed a step.
Do not recommend paid tools or services unless I explicitly ask for them.

Today's Goal

Interview me one question at a time.

Keep every question simple, and briefly explain why you're asking it.

If I don't already have a project idea, interview me to discover one. Understand my interests, goals, skills, strengths, and constraints, then suggest, compare, refine, combine, and challenge ideas until we've chosen the strongest project I can realistically build in 10 days.

Don't optimize for the most ambitious project. Optimize for the most impressive project that can be fully completed within the available time. Continuously protect me from scope creep.

Once we've selected the project, continue the interview until you have everything needed to confidently guide the remaining nine days.

Clearly define:

What the v1.0 will include
What will intentionally be left out
What success on Day 10 looks like

Before generating any documents, summarize the finalized project in one paragraph and ask for my approval.

Only generate the deliverables after I confirm.

Deliverables

Generate downloadable versions of:

1. Product Requirements Document (PRD)

A complete, professional PRD for the finalized project.

2. Implementation Blueprint (Days 2-10)

Generate a project-specific implementation blueprint for building this exact project over the remaining nine days.

This must not be a generic template.

Break the project into realistic daily milestones so that completing every day's work results in a polished, deployed v1.0 by Day 10.

For each day, include:

🎯 Objective
📖 What I'll learn
🛠 Features to build
📝 Step-by-step implementation plan
📂 Files and folders to create or modify
🔗 APIs, libraries, services, or tools to integrate (if applicable)
🧪 Testing tasks
🐞 Common issues and debugging tips
✅ End-of-day checklist
📸 Expected project state and screenshots to capture
➡️ Handoff notes for the next day

The implementation plan should contain enough technical detail that the corresponding daily AI prompt can guide me through building the project without redesigning, re-planning, or making major architectural decisions.

Assume each remaining day begins with a fresh AI conversation. Therefore, each day's section must contain enough context that another AI assistant could immediately continue building from where the previous day ended.

The blueprint should function as the single source of truth for the remainder of the capstone.

3. Project Pitch Deck

Create a presentation-ready pitch deck covering:

Problem
Target Users
Solution
Key Features
Technical Approach
Future Scope
Vision

Important

Do not choose the tech stack or write code today.

Today's objective is to discover the right project, define it clearly, and produce a complete implementation blueprint that will enable the remaining daily prompts to guide me through building and shipping a polished v1.0 product by Day 10.
:Files ZiP For 10-Days#
"C:\Users\DELL\OneDrive\Documents\GitHub\Day3\files.zip\Day_1_Instructions.md"
"C:\Users\DELL\OneDrive\Documents\GitHub\Day3\files.zip\Implementation_Blueprint_Days_2-10.md"
"C:\Users\DELL\OneDrive\Documents\GitHub\Day3\files.zip\PRD.md"

import streamlit as st

# Page Configuration
st.set_page_config(page_title="Benefits Email Assistant", layout="wide")
st.title("AI-Powered Email & Benefits Query Assistant")

st.write("Environment check: Streamlit is running! 🟢")
app.py
# File Uploader Section
uploaded_file = st.file_uploader(
    "Upload a broker/client email (.txt or .eml)", 
    type=["txt", "eml"]
)

if uploaded_file is not None:
    st.success(f"File received: {uploaded_file.name}")

requirements.txt
streamlit
pandas
anthropic

<img width="1173" height="610" alt="image" src="https://github.com/user-attachments/assets/9934df10-ad68-452e-a12e-c72b4ad35a90" />
<img width="486" height="533" alt="image" src="https://github.com/user-attachments/assets/fe647c06-8dc3-4e1e-8856-bd6486d6b571" />

Reminder for Replit#

<img width="1314" height="613" alt="image" src="https://github.com/user-attachments/assets/6df2805e-9105-41ac-ae32-ffd3ad830ea5" />
