from app.data.sample_documents import DOCUMENTS

def search_library(query: str) -> str:
    """Search the local educational medical reference library for relevant passages."""
    terms = {word.lower().strip(".,?!:;()[]{}") for word in query.split() if len(word) > 2}
    ranked = []
    for doc in DOCUMENTS:
        text = f"{doc['title']} {doc['text']}".lower()
        score = sum(1 for term in terms if term in text)
        if score:
            ranked.append((score, doc))
    ranked.sort(key=lambda item: item[0], reverse=True)
    if not ranked:
        return (
            "No matching passages were found in the local project library. "
            "State this limitation clearly and do not invent a source."
        )
    return "\n\n".join(
        f"Title: {doc['title']}\nSource: {doc['source']}\nPassage: {doc['text']}"
        for _, doc in ranked[:3]
    )
