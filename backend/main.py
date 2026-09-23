from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

from ml.nlp_engine import analyze_resume
from ml.document_reader import extract_text
from ml.similarity_engine import calculate_text_similarity
from ml.recommendation_engine import generate_recommendations
app = FastAPI(
    title="CareerAI",
    description="AI-powered Resume and Job Description Analyzer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Supported resume formats
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}


@app.get("/")
def home():
    return {
        "message": "CareerAI backend is running!"
    }


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # -----------------------------------
    # 1. Check uploaded file
    # -----------------------------------

    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Please upload a resume."
        )

    filename = resume.filename.lower()

    if "." not in filename:
        raise HTTPException(
            status_code=400,
            detail="File must have an extension."
        )

    extension = os.path.splitext(filename)[1]

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. "
                   "Please upload PDF, DOCX, or TXT."
        )


    # -----------------------------------
    # 2. Check job description
    # -----------------------------------

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )


    # -----------------------------------
    # 3. Save uploaded resume temporarily
    # -----------------------------------

    file_path = f"temp_{resume.filename}"


    try:

        with open(file_path, "wb") as file:
            file.write(await resume.read())


        # -----------------------------------
        # 4. Extract text from resume
        # -----------------------------------

        resume_text = extract_text(file_path)


        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the resume."
            )


        # -----------------------------------
        # 5. Analyze resume skills
        # -----------------------------------

        result = analyze_resume(
            resume_text,
            job_description
        )


        # -----------------------------------
        # 6. Calculate text similarity
        # -----------------------------------

        similarity_score = calculate_text_similarity(
            resume_text,
            job_description
        )


        # -----------------------------------
        # 7. Get skill match score
        # -----------------------------------

        skill_score = result["match_score"]


        # -----------------------------------
        # 8. Calculate final score
        # -----------------------------------

        final_score = round(
            (skill_score * 0.6)
            +
            (similarity_score * 0.4),
            2
        )


        # -----------------------------------
        # 9. Add similarity and final score
        # -----------------------------------

        result["similarity_score"] = similarity_score

        result["final_score"] = final_score


        # -----------------------------------
        # 10. Generate learning recommendations
        # -----------------------------------

        recommendations = generate_recommendations(
            result["missing_skills"]
        )

        result["recommendations"] = recommendations


        # -----------------------------------
        # 11. Generate overall recommendation
        # -----------------------------------

        if final_score >= 80:

            recommendation = "Excellent match"

        elif final_score >= 65:

            recommendation = "Good match"

        elif final_score >= 50:

            recommendation = "Moderate match"

        else:

            recommendation = "Needs improvement"


        result["recommendation"] = recommendation


        # -----------------------------------
        # 12. Return final response
        # -----------------------------------

        return result


    except HTTPException:
        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Error processing resume: {str(e)}"
        )


    finally:

        # -----------------------------------
        # 13. Delete temporary resume file
        # -----------------------------------

        if os.path.exists(file_path):

            os.remove(file_path)