import os
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["research_paper", "summary_length", "summary_style"],
    template="""
    Summarize the following research paper:
    {research_paper} with {summary_length} and {summary_style}
    Make sure to include all the important details and equations. Keep it concise and to the point.
    Include the analogies and metaphors to make it more engaging.
    """,
    validate_template=True
)

base_path = os.path.join(os.path.dirname(__file__), "prompts")
os.makedirs(base_path, exist_ok=True)
template.save(os.path.join(base_path, "prompt_template.json"))