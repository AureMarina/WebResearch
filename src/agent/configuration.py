import os
from pydantic import BaseModel, Field
from typing import Optional, Literal, Union
from langchain_core.runnables import RunnableConfig

class Configuration(BaseModel):
    query_generator_model: str = Field(
        default = "gpt-4o",
        metadata = {
            "description": "The name of the language model to use for the agent's query generation."
        },
    )
    
    reflection_model: str = Field(
        default = "gpt-4o",
        metadata = {
            "description": "The name of the language model to use for the agent's reflection."
        },
    )
    
    answer_model: str = Field(
        default = "gpt-4o",
        metadata={
            "description": "The name of the language model to use for the agent's answer."
        },
    )
    
    max_research_loops: int = Field(
        default=2,
        metadata={"description": "The maximum number of research loops to perform."},
    )