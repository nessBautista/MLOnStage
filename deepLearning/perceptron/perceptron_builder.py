from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum
from datetime import datetime

class CodeContext(BaseModel):
    """Structure for code-related context"""
    language: str = Field(..., description="Programming language of the code")
    code: str = Field(..., description="The actual code snippet")
    file_path: Optional[str] = Field(None, description="Path to the file if applicable")
    dependencies: Optional[List[str]] = Field(default=[], description="Required dependencies")

class TaskMeta(BaseModel):
    """Meta object for AI coding tasks"""
    
    # Basic Task Information
    id: str = Field(..., description="Unique identifier for the task")
    title: str = Field(..., description="Title of the task")
    description: str = Field(..., description="Detailed description of what needs to be done")
    context_file_paths: Optional[List[str]] = Field(
        default=None, 
        description="Paths for read only files that contains related context"
    )
    # Task Context
    code_context: Optional[List[CodeContext]] = Field(
        default=None, 
        description="Relevant code snippets and documentationcontext"
    )

    requirements: Optional[List[str]] = Field(
        default=None,
        description="Requirements for the task"
    )
    tags: Optional[List[str]] = Field(
        default=None,
        description="Tags for the task"
    )

    def build_prompt(self) -> str:
        """
        Builds a structured string prompt from the TaskMeta object.
        
        Returns:
            str: A formatted string containing the structured prompt
        """
        sections = []
        
        # Add task header with ID and title
        sections.append(f"# Task: {self.title} (ID: {self.id})")
        
        # Add description if present
        if self.description:
            sections.append("\n## Description")
            sections.append(self.description)
        
        # Add target files if present
        if self.context_file_paths:
            sections.append("\n## Context read only Files")
            for file_path in self.context_file_paths:
                sections.append(f"- {file_path}")
        
        # Add requirements if present
        if self.requirements:
            sections.append("\n## Requirements")
            for req in self.requirements:
                sections.append(f"- {req}")
        
        # Add code context if present
        if self.code_context:
            sections.append("\n## Code Context")
            for idx, context in enumerate(self.code_context, 1):
                # add code snippet header                
                sections.append(f"\n### Code Snippet {idx}")
                # Specify language
                sections.append(f"Language: {context.language}")
                if context.dependencies:
                    sections.append("Dependencies:")
                    for dep in context.dependencies:
                        sections.append(f"- {dep}")
                # Specify file path if available
                if context.file_path:
                    sections.append("file path:")
                    sections.append(f"- {context.file_path}")
                # Add contents of the code snippet
                sections.append("\n```" + context.language)
                sections.append(context.code.strip())
                sections.append("```")
        
        # Add tags if present
        if self.tags:
            sections.append("\n## Tags")
            sections.append(", ".join(self.tags))
        
        # Join all sections with newlines
        return "\n".join(sections)

    class Config:
        """Pydantic model configuration"""
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


from pathlib import Path
from aider.coders import Coder
from aider.models import Model
import sys
 

pyproject_path = Path.cwd() / "perceptron.py"
documentation = Path.cwd() / "perceptron.md"
eng_design = Path.cwd() / "perceptron_eng_design.md"


context_editable = [
    str(pyproject_path),    
]



context_read_only = [
    str(documentation),
    str(eng_design)
]



if __name__ == "__main__":
    task_1 = TaskMeta(
        id="implement_base_class",
        title="Create Perceptron Base Class Structure",
        description="""
        Create the basic Perceptron class with constructor and docstrings:
        1. Define class and constructor
        2. Add parameters: eta, n_iter, random_state
        3. Add class and method docstrings
        """,
        context_file_paths=context_read_only,
        code_context=[
            CodeContext(
                language="python",
                code="""
                class Perceptron:
                    def __init__(self, eta=0.01, n_iter=50, random_state=1):
                        # TODO: Implement constructor
                        pass
                """,
                file_path=str(pyproject_path)
            )
        ],
        requirements=[
            "Include learning rate parameter (eta)",
            "Include number of iterations parameter (n_iter)",
            "Include random seed parameter (random_state)",
            "Add proper docstrings following NumPy format"
        ],
        tags=["perceptron", "class-structure", "initialization"]
    )
    print(task_1.model_dump_json())

    model = Model("claude-3-5-sonnet-20241022")
    # Initialize AI Coding Assistant
    coder = Coder.create(
    main_model=model,
        fnames=task_1.code_context[0].file_path,
        read_only_fnames=task_1.context_file_paths,
        # auto_commits=False,
        # suggest_shell_commands=False,
    )
   