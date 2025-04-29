## Structured Output in Langchain

It is a way to get the output of LLM in a structured format such as JSON, instead of a free form text. Structured outputs are way easier to deal with programmatically.

## Usecases of Structured Output

1. Data Extraction
2. API
3. Agents -> Agents need tool to perform a task and tools would expect a structured output.
* LLMs were incapable of working with other systems due to their free form text output, with structured output technique, it made easier for LLMs to work with external systems and tools.

*  There are LLMs which can generate the structured output (like OpenAI models) and some which cant generate the structure outputs by default.
* with_structured_output -> To work with LLMs which can generate structured output
* OutputParsers -> To work with LLMs which cant generate structured output

## with_structured_output

We need to call with_structured_output before model.invoke with the specified data format.
Three ways to specify the data format:
1. TypedDict -> Just insures that the dictionary in python follows a specific structure. (but no validation)
2. Pydantic -> data validation and data parsing library which ensures that the data you work with is correct, structured and type-safe.
3. json_schema

## When to use these data formats:

1. TypedDict:
    * We only need typed hints
    * No need of type validation
    * We trust the LLM to return the correct data
2. Pydantic:
    * Need data validation
    * Need default values if LLM misses it
    * Need automatic type conversion 
3. json_schema:
    * Dont want to import addition python libraries like Pydantic
    * Need validations but dont need python objects
    * Want to define structure in a standard JSON format.

## Important Note:

with_structured_output has an additional parameter called method:
1. json_mode -> When the structured output needs to be a json, commonly used with Claude, Gemini models etc.
2. function_calling -> When the structured output needs to be used to call a function/tools, commonly used with OpenAi models.

There are models which dont support the structured outputs with both json_mode and function_calling, eg. HuggingFace models. In that case you need to explicitly use the OutputParsers.