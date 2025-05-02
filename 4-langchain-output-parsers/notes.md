## What are Output parsers ?

Output parsers in langchain are the classes that help you convert raw llm response to a structured output such as JSON, Pydantic models, csv and more. They ensure consistency, validation and ease of use in applications.
There are multiple types of output parsers in langchain but most commonly used are:
1. StrOutputParser
2. JSONOutputParser
3. StructuredOutputParser
4. PydanticOutputParser

### 1. StrOutputParser

* These are the simplest output parsers present in langchain. They parse the raw response of the LLM and return it as a plain string.

### 2. JSONOutputParser

* Forces an LLM to return its response in a json format.
* Disadvantage: Only disadvantage of using JsonOutputParser is, even though we can get the JSON response from the LLM, we cant enforce any schema to it. This means we cant tell what would be the structure of our JSON. Even if included in prompt, the LLM might or might not give the structure we asked.
* To solve this issue, we can use StructuredOutputParser.

### 3. StructuredOutputParser

* StructureOutputParser is an output parser in langchain which helps in extracting the structured response from the LLM. The structured response conforms to the predefined field schema.
* It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows the structured format.
* Disadvantage: No data validation. Solution is to use PydanticOutputParser.

### 4. PydanticOutputParser

* It is a structured output parser in langchain that uses Pydantic models to enforce schema validation when processing the LLM response.
* Advantages: Strict Schema enforcement, Data Validation, Type Safety, Seamless integration
  