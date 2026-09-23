# CareerAI

AI-powered Resume and Job Description Analyzer that helps candidates understand their job compatibility, identify skill gaps, and receive personalized learning recommendations.

## Overview

CareerAI compares a candidate's resume with a target job description and generates an intelligent career analysis.

The application extracts skills from both documents, calculates skill compatibility and textual similarity, identifies missing skills, and generates a personalized learning roadmap.

## Key Features

- Resume upload support for PDF, DOCX, and TXT files
- Job description analysis
- Resume skill extraction
- Job skill extraction
- Matched skill identification
- Missing skill identification
- Skill match percentage
- Text similarity analysis
- Overall career match score
- Personalized learning recommendations
- Interactive React-based dashboard
- FastAPI backend API
- Drag-and-drop resume upload
- Responsive user interface

## Application Architecture

```text
                 CareerAI
                    │
                    ▼
          React Frontend (Vite)
                    │
                    │ HTTP POST
                    ▼
          FastAPI Backend
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Document      NLP/Skill    Similarity
   Reader        Analysis     Engine
        │           │           │
        └───────────┼───────────┘
                    ▼
              Match Analysis
                    │
                    ▼
          Recommendation Engine
                    │
                    ▼
              JSON Response
                    │
                    ▼
            React Results UI