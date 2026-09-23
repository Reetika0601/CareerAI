SKILL_RESOURCES = {

    "python": {
        "priority": "High",
        "reason": "Python is widely used for software development, automation and machine learning.",
        "topics": [
            "Python basics",
            "Functions",
            "Object-Oriented Programming",
            "File handling",
            "Exception handling"
        ]
    },

    "sql": {
        "priority": "High",
        "reason": "SQL is essential for working with relational databases and data analysis.",
        "topics": [
            "SELECT",
            "WHERE",
            "GROUP BY",
            "JOINs",
            "Subqueries",
            "Window functions"
        ]
    },

    "machine learning": {
        "priority": "High",
        "reason": "Machine learning is required to build predictive and intelligent applications.",
        "topics": [
            "Regression",
            "Classification",
            "Feature engineering",
            "Model evaluation",
            "Scikit-learn"
        ]
    },

    "docker": {
        "priority": "Medium",
        "reason": "Docker is widely used to package and deploy applications consistently.",
        "topics": [
            "Images",
            "Containers",
            "Dockerfile",
            "Docker Compose",
            "Container deployment"
        ]
    },

    "aws": {
        "priority": "Medium",
        "reason": "AWS is commonly used for deploying and scaling applications in the cloud.",
        "topics": [
            "EC2",
            "S3",
            "IAM",
            "VPC",
            "Cloud deployment"
        ]
    },

    "react": {
        "priority": "Medium",
        "reason": "React is widely used for building modern interactive web interfaces.",
        "topics": [
            "Components",
            "Props",
            "State",
            "Hooks",
            "API integration"
        ]
    },

    "javascript": {
        "priority": "Medium",
        "reason": "JavaScript is fundamental for interactive web applications.",
        "topics": [
            "Variables",
            "Functions",
            "DOM",
            "Async JavaScript",
            "Fetch API"
        ]
    },

    "node.js": {
        "priority": "Medium",
        "reason": "Node.js is commonly used for building backend services with JavaScript.",
        "topics": [
            "Node basics",
            "Express",
            "REST APIs",
            "Middleware",
            "Authentication"
        ]
    },

    "fastapi": {
        "priority": "Medium",
        "reason": "FastAPI is useful for building high-performance Python APIs.",
        "topics": [
            "Routes",
            "Request validation",
            "Pydantic",
            "Authentication",
            "API deployment"
        ]
    },

    "flask": {
        "priority": "Medium",
        "reason": "Flask is a lightweight Python framework commonly used for web applications.",
        "topics": [
            "Routes",
            "Templates",
            "Forms",
            "REST APIs",
            "Deployment"
        ]
    }
}


def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        skill = skill.lower()

        if skill in SKILL_RESOURCES:

            resource = SKILL_RESOURCES[skill]

            recommendations.append({
                "skill": skill,
                "priority": resource["priority"],
                "reason": resource["reason"],
                "topics": resource["topics"]
            })

        else:

            recommendations.append({
                "skill": skill,
                "priority": "Low",
                "reason": f"Learning {skill} can improve your job compatibility.",
                "topics": [
                    f"{skill} fundamentals",
                    f"{skill} practical projects",
                    f"{skill} interview preparation"
                ]
            })

    return recommendations