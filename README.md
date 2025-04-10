# Reasoning Model Inferencing

A template repository for quickly building and testing production-ready reasoning use cases using Azure OpenAI services, specifically designed around the o3-mini model.

## Purpose

This repository provides a structured template for developing, testing, and deploying reasoning model use cases. It enables data scientists and AI engineers to:

- Quickly prototype and test reasoning-based AI solutions
- Create structured, auditable AI outputs with proper citations
- Implement function/tool calling capabilities
- Define custom data schemas for consistent input/output patterns
- Test various reasoning effort levels (low, medium, high)

The main component is a Jupyter notebook template that guides you through the process of building a complete reasoning model use case.

## Features

- Pre-configured Azure OpenAI integration
- Structured outputs using Pydantic models
- Tool/function calling capabilities
- Citation and justification system for AI responses
- Customizable system messages and prompts
- Example data handling and processing

## Prerequisites

- Python 3.11+
- Azure OpenAI account with access to o3-mini model
- Basic understanding of Pydantic and OpenAI's API

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/reasoning-model-inferencing.git
   cd reasoning-model-inferencing
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your Azure OpenAI credentials:
   ```
   O3MINI_AZURE_ENDPOINT=your_azure_endpoint
   O3MINI_API_KEY=your_api_key
   ```

## Usage

The main component of this repository is the Jupyter notebook `use_case_template.ipynb`. To use it:

1. Ensure your virtual environment is activated
2. Start Jupyter:
   ```
   jupyter notebook
   ```
3. Open `use_case_template.ipynb`
4. Follow the guided sections in the notebook:
   - Define your inputs (instructions, rules, examples, datasets)
   - Configure your Pydantic models for structured output
   - Set up any necessary tool functions
   - Construct the prompt
   - Generate predictions and analyze the results

## Template Structure

The template guides you through several key sections:

1. **Environment Setup**: Importing libraries and setting up the OpenAI client
2. **Input Definition**: 
   - Instructions and tasks
   - Rules and policies
   - Few-shot examples
   - Datasets for analysis
3. **Output Schema Definition**: Using Pydantic models for structured output
4. **Tool Function Setup**: Optional tools for retrieving additional data
5. **Prompt Construction**: Combining all inputs into a well-structured prompt
6. **Prediction Generation**: Running the model with appropriate reasoning effort
7. **Result Analysis**: Examining citations and justifications

## Customizing for Your Use Case

1. Modify the Pydantic models in the notebook to match your specific data structures
2. Update the system message in the `o3minicall` function to better reflect your use case
3. Add your own tool functions in `tools.py` to integrate with your data sources
4. Adjust the reasoning effort based on the complexity of your task

## Environment Variables

- `O3MINI_AZURE_ENDPOINT`: Your Azure OpenAI service endpoint
- `O3MINI_API_KEY`: Your Azure OpenAI API key