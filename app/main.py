from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import APP_NAME, GROQ_API_KEY, GROQ_MODEL
from app.schemas import AskRequest, AskResponse

app = FastAPI(
    title=APP_NAME,
    description="Educational multi-agent healthcare and medical research assistant.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def home():
    return FileResponse("app/static/index.html")

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "app_name": APP_NAME,
        "groq_configured": bool(GROQ_API_KEY),
        "model": GROQ_MODEL,
        "agents": ["Query Analyzer", "Research Agent", "Answer Reviewer"],
    }

@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest):
    if not GROQ_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="GROQ_API_KEY is not configured. Add it to .env and restart the application."
        )
    try:
        from app.agents.team import medical_team
        result = medical_team.run(payload.question)
        answer = getattr(result, "content", None)
        if answer is None:
            answer = str(result)
        return AskResponse(
            status="success",
            question=payload.question,
            answer=str(answer),
            sources=[
                "Local educational healthcare reference library (when matched by the Research Agent)"
            ],
            disclaimer=(
                "Educational information only; not a diagnosis, emergency service, or substitute "
                "for advice from a qualified healthcare professional. The local sample library is limited."
            ),
        )
    except Exception as exc:
        # Avoid returning provider credentials or internal stack traces to the client.
        print(f"Agent request failed: {type(exc).__name__}: {exc}")
        raise HTTPException(
            status_code=502,
            detail="The AI service could not complete this request. Check server logs and Groq configuration."
        ) from exc
