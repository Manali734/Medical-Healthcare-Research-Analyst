
from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from agno.team.mode import TeamMode

from app.agents.tools import search_library
from app.config import GROQ_MODEL


def build_team():
    # One shared Groq model instance for all agents
    model = Groq(id=GROQ_MODEL)

    analyzer = Agent(
        name="Query Analyzer",
        role="Classify the healthcare or medical-research question and identify the exact information needed.",
        model=model,
        instructions=[
            "Identify the user's main question and whether it concerns general health education, "
            "research methods, or interpretation of published evidence.",
            "Do not diagnose, prescribe, or infer missing clinical facts.",
            "Make a concise research plan for the team."
        ],
        markdown=True,
    )

    researcher = Agent(
        name="Research Agent",
        role="Find relevant passages in the local educational healthcare library and summarize them.",
        model=model,
        tools=[search_library],
        instructions=[
            "Use search_library to look for relevant passages in the supplied local library.",
            "Clearly distinguish library-supported information from general background knowledge.",
            "Name the supplied source titles when relevant. Never invent citations, studies, statistics, "
            "guidelines, URLs, or claims that a source was consulted when it was not.",
            "If the library has no relevant evidence, say so."
        ],
        markdown=True,
    )

    reviewer = Agent(
        name="Answer Reviewer",
        role="Review the proposed healthcare research response for unsupported claims and safety.",
        model=model,
        instructions=[
            "Review the analysis and research findings for unsupported assertions, fabricated sources, "
            "overconfident language, and missing limitations.",
            "Return a clear answer with sections: Summary, Evidence from the project library, "
            "Limitations, and Suggested next steps.",
            "Do not provide a diagnosis or personalized treatment plan. Encourage a qualified clinician "
            "for individual medical decisions. For possible emergencies, advise contacting local emergency services.",
            "Do not claim that you verified external medical sources."
        ],
        markdown=True,
    )

    return Team(
        name="Medical Healthcare & Research Analyst Team",
        model=model,
        members=[analyzer, researcher, reviewer],
        mode=TeamMode.coordinate,
        instructions=[
            "Coordinate the three specialist agents to answer healthcare education and research questions.",
            "Ask the Research Agent to search the local library and have the Answer Reviewer scrutinize the answer.",
            "Use only educational guidance, acknowledge uncertainty, and never claim to diagnose."
        ],
        markdown=True,
        show_members_responses=True,
    )


medical_team = build_team()
