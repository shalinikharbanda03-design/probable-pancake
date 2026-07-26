# System Architecture

## Overview
The AI-Powered Email & Benefits Query Assistant is a single-process Streamlit application built with Python. It parses client/broker email queries (.txt/.eml), extracts key details, checks member eligibility against a local mock CSV database using rule-based logic, and drafts professional, HIPAA-conscious responses using the Anthropic Claude API.

## Architecture Diagram (Mermaid)

```mermaid
graph TD
    A[User / Healthcare Analyst] -->|Uploads .txt/.eml File| B[Streamlit UI - app.py]
    B -->|Raw Text| C[Text Extraction & Parsing - extraction.py]
    C -->|Extracted Fields: Name, Dates, Location| D[Rule-Based Compliance Check - compliance_check.py]
    D -->|Match Query| E[(Mock Dataset - data/mock_members.csv)]
    E -->|Member Data & Discrepancies| D
    D -->|Flags & Extracted Data| F[AI Draft Generation - ai_drafting.py]
    F -->|Prompt + Context| G[Anthropic Claude API]
    G -->|Drafted Response| F
    F -->|Draft & Insights| B
    B -->|Analyst Reviews & Approves| H[Audit Logger - data/audit_log.csv]
