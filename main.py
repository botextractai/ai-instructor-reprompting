import instructor
import json
import os
from dotenv import load_dotenv
from enum import Enum
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional, List

import warnings
warnings.filterwarnings('ignore')

# Environment variables
load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]

class SeniorityLevel(str, Enum):
    junior = "Junior"
    senior = "Senior"
    lead = "Lead"

class WorkExperience(BaseModel):
    company_name: str = Field(..., description="Name of the company")
    position: str = Field(..., description="Position or title held at the company")
    duration_years: int = Field(..., description="Duration of employment in years")
    achievements: List[str] = Field(..., description="Key achievements in this role")

class Resume(BaseModel):
    name: str = Field(..., description="Full name of the individual")
    title: str = Field(..., description="Title of the individual")
    location: str = Field(..., description="Current location or address")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    github: Optional[str] = Field(None, description="GitHub profile URL")
    contact: Optional[str] = Field(None, description="Phone number or other contact information")
    email: str = Field(..., description="Email address")
    summary: str = Field(..., description="Brief professional summary or objective statement")
    years_of_experience: int = Field(..., description="Total years of professional experience")
    seniority: SeniorityLevel = Field(..., description="Seniority level of the individual")
    work_experience: List[WorkExperience] = Field(..., description="List of work experiences")
    education: str = Field(..., description="Education summary")
    skills: str = Field(..., description="Skills summary")
    certifications: str = Field(..., description="Certifications summary")
    projects: str = Field(..., description="Projects summary")

    def to_json(self, file_path: str):
        """Save the Resume data as a JSON file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.model_dump(), f, indent=4, ensure_ascii=False)

def process_resume(resume_path: str) -> Optional[Resume]:
    with open(resume_path, 'r', encoding='utf-8') as file:
        resume_text = file.read()

    client = instructor.from_openai(OpenAI())

    try:
        reply = client.chat.completions.create(
            model="gpt-4-turbo",
            # Note: OpenAI uses response_format, instructor uses response_model!
            response_model=Resume,
            max_tokens=4096,
            max_retries=3,
            messages=[
                {"role": "system", "content": "Respond in JSON with values extracted from the Markdown resume."},
                {"role": "user", "content": resume_text}
            ]
        )
        return reply
    except Exception as e:
        print(f"Error processing resume: {e}")
        return None

resume = process_resume('./data/resume.md')
if resume:
    resume.to_json('./data/resume.json')
else:
    print("Failed to process the resume.")
