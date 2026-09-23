import { useState } from "react";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFile = (file) => {
    if (!file) return;

    const allowedTypes = [".pdf", ".docx", ".txt"];
    const fileName = file.name.toLowerCase();

    if (!allowedTypes.some((type) => fileName.endsWith(type))) {
      setError("Please upload a PDF, DOCX, or TXT resume.");
      return;
    }

    setResume(file);
    setError("");
  };

  const handleDrop = (event) => {
    event.preventDefault();
    handleFile(event.dataTransfer.files[0]);
  };

  const analyzeResume = async () => {
    if (!resume) {
      setError("Please upload your resume first.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter the job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Analysis failed.");
      }

      setResult(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      {/* NAVBAR */}
      <nav className="navbar">
        <div className="brand">
          <div className="brand-icon">C</div>
          <span>CareerAI</span>
        </div>

        <div className="nav-status">
          <span className="status-dot"></span>
          AI Career Intelligence
        </div>
      </nav>


      {/* HERO SECTION */}
      <section className="hero-section">

        <div className="hero-badge">
          ✦ Resume Intelligence Platform
        </div>

        <h1>
          Turn your resume into your
          <span> career advantage.</span>
        </h1>

        <p>
          Compare your resume with a job description, discover skill gaps,
          and get a personalized learning roadmap.
        </p>

      </section>


      {/* MAIN CONTENT */}
      <main className="main-container">

        {/* INPUT SECTION */}
        <div className="input-grid">

          {/* RESUME CARD */}
          <section className="glass-card">

            <div className="card-heading">

              <div className="heading-icon">
                📄
              </div>

              <div>
                <h2>Your Resume</h2>
                <p>Upload your latest resume</p>
              </div>

            </div>


            <div
              className={`upload-zone ${resume ? "file-selected" : ""}`}
              onDragOver={(event) => event.preventDefault()}
              onDrop={handleDrop}
              onClick={() =>
                document.getElementById("resumeInput").click()
              }
            >

              <input
                id="resumeInput"
                type="file"
                accept=".pdf,.docx,.txt"
                hidden
                onChange={(event) =>
                  handleFile(event.target.files[0])
                }
              />

              {resume ? (
                <>
                  <div className="upload-icon success">
                    ✓
                  </div>

                  <h3>{resume.name}</h3>

                  <p>
                    Resume ready for analysis
                  </p>

                  <button
                    className="change-file"
                    onClick={(event) => {
                      event.stopPropagation();
                      document.getElementById("resumeInput").click();
                    }}
                  >
                    Change file
                  </button>
                </>
              ) : (
                <>
                  <div className="upload-icon">
                    ↑
                  </div>

                  <h3>
                    Drop your resume here
                  </h3>

                  <p>
                    or <strong>browse files</strong>
                  </p>

                  <small>
                    PDF, DOCX or TXT • Max 10 MB
                  </small>
                </>
              )}

            </div>

          </section>


          {/* JOB DESCRIPTION CARD */}
          <section className="glass-card">

            <div className="card-heading">

              <div className="heading-icon">
                💼
              </div>

              <div>
                <h2>Job Description</h2>
                <p>Paste the role you're targeting</p>
              </div>

            </div>


            <textarea
              className="job-input"
              placeholder="Paste the job description here..."
              value={jobDescription}
              onChange={(event) =>
                setJobDescription(event.target.value)
              }
            />

            <div className="character-count">
              {jobDescription.length} characters
            </div>

          </section>

        </div>


        {/* ERROR */}
        {error && (
          <div className="error-box">
            ⚠ {error}
          </div>
        )}


        {/* ANALYZE BUTTON */}
        <button
          className="analyze-button"
          onClick={analyzeResume}
          disabled={loading}
        >

          {loading ? (
            <>
              <span className="spinner"></span>
              Analyzing your profile...
            </>
          ) : (
            <>
              Analyze My Career Match
              <span>→</span>
            </>
          )}

        </button>


        {/* RESULTS */}
        {result && (
          <section className="results-section">

            {/* RESULT HEADER */}
            <div className="results-header">

              <div>

                <div className="section-label">
                  ANALYSIS COMPLETE
                </div>

                <h2>
                  Your Career Match
                </h2>

                <p>
                  Here's how your profile compares with this role.
                </p>

              </div>


              <div className="recommendation-pill">
                {result.recommendation}
              </div>

            </div>


            {/* SCORE CARD */}
            <div className="score-card">

              <div
                className="score-ring"
                style={{
                  "--score": `${result.final_score}%`,
                }}
              >

                <div className="score-inner">

                  <strong>
                    {result.final_score}
                  </strong>

                  <span>
                    % MATCH
                  </span>

                </div>

              </div>


              <div className="score-info">

                <h3>
                  Overall compatibility
                </h3>

                <p>
                  Your resume currently matches this job based on
                  skills and textual similarity.
                </p>


                <div className="score-stats">

                  <div>

                    <strong>
                      {result.match_score}%
                    </strong>

                    <span>
                      Skill Match
                    </span>

                  </div>


                  <div>

                    <strong>
                      {result.similarity_score}%
                    </strong>

                    <span>
                      Text Similarity
                    </span>

                  </div>

                </div>

              </div>

            </div>


            {/* SKILLS SECTION */}
            <div className="skills-grid">

              {/* MATCHED SKILLS */}
              <div className="skill-card matched">

                <div className="skill-title">

                  <span>✓</span>

                  <h3>
                    Matched Skills
                  </h3>

                </div>


                <div className="skill-list">

                  {result.matched_skills &&
                  result.matched_skills.length > 0 ? (

                    result.matched_skills.map((skill) => (

                      <span
                        className="skill-chip"
                        key={skill}
                      >
                        {skill}
                      </span>

                    ))

                  ) : (

                    <p>
                      No matched skills found.
                    </p>

                  )}

                </div>

              </div>


              {/* MISSING SKILLS */}
              <div className="skill-card missing">

                <div className="skill-title">

                  <span>+</span>

                  <h3>
                    Skills to Develop
                  </h3>

                </div>


                <div className="skill-list">

                  {result.missing_skills &&
                  result.missing_skills.length > 0 ? (

                    result.missing_skills.map((skill) => (

                      <span
                        className="skill-chip"
                        key={skill}
                      >
                        {skill}
                      </span>

                    ))

                  ) : (

                    <p>
                      No major skill gaps found.
                    </p>

                  )}

                </div>

              </div>

            </div>


            {/* YOUR STRENGTHS */}
            <div className="strengths-section">

              <div className="section-label">
                YOUR STRENGTHS
              </div>

              <h2>
                What you're already bringing to the role
              </h2>

              <p className="roadmap-description">
                These skills from your resume already align with
                the requirements of this job.
              </p>


              <div className="strengths-list">

                {result.matched_skills &&
                result.matched_skills.length > 0 ? (

                  result.matched_skills.map((skill, index) => (

                    <div
                      className="strength-item"
                      key={skill}
                    >

                      <div className="strength-number">
                        0{index + 1}
                      </div>

                      <div className="strength-icon">
                        ✓
                      </div>

                      <div className="strength-content">

                        <h3>
                          {skill}
                        </h3>

                        <p>
                          This skill matches a requirement
                          mentioned in the job description.
                        </p>

                      </div>

                    </div>

                  ))

                ) : (

                  <div className="strength-empty">
                    No directly matched skills were identified yet.
                  </div>

                )}

              </div>

            </div>


            {/* PERSONALIZED ROADMAP */}
            <div className="roadmap-section">

              <div className="section-label">
                PERSONALIZED ROADMAP
              </div>

              <h2>
                What should you learn next?
              </h2>

              <p className="roadmap-description">
                CareerAI identified these areas that could improve
                your compatibility with this role.
              </p>


              <div className="recommendation-grid">

                {result.recommendations &&
                result.recommendations.map((item, index) => (

                  <div
                    className="recommendation-card"
                    key={item.skill}
                  >

                    <div className="recommendation-number">
                      {String(index + 1).padStart(2, "0")}
                    </div>


                    <div className="recommendation-content">

                      <div className="recommendation-top">

                        <h3>
                          {item.skill}
                        </h3>

                        <span
                          className={`priority ${item.priority.toLowerCase()}`}
                        >
                          {item.priority}
                        </span>

                      </div>


                      <p>
                        {item.reason}
                      </p>


                      <div className="topic-list">

                        {item.topics &&
                        item.topics.map((topic) => (

                          <span key={topic}>
                            {topic}
                          </span>

                        ))}

                      </div>

                    </div>

                  </div>

                ))}

              </div>

            </div>

          </section>
        )}

      </main>


      {/* FOOTER */}
      <footer>

        <strong>
          CareerAI
        </strong>

        <span>
          Built for smarter career decisions.
        </span>

      </footer>

    </div>
  );
}

export default App;