## What are prompt templates in langchain

Prompt Templates in langchain is a structured way to create dynamic prompts by inserting the values
to a predefined template. It allows you to define the placeholders that can be filled at runtime with
different inputs


## Benefits of using prompt template

Why not use the f-string to inject the variables in the prompt ??
1. Default Validation with validate_template parameter -> True/False
2. Reusability -> Prompts can be saved in a json and can be used with load_prompt function
3. Tight coupling with Langchain Ecosystem.

## Types of messages in Langchain

1. System Message -> System level message at the start of the conversation to define the role/persona to the model.
2. Human Message -> Message sent by the user to the LLM
3. AI Message -> The response to user query sent by the LLM


## Invoke

1. Invoke method can be used with:
    a. Single Message - Single turn standalone query
        * Static message
        * Dynamic message (Prompt template)
    b. List of messages - Multi turn conversation
        * Static message - SystemMessage, HumanMessage, AIMessage
        * Dynamic message - ChatPromptTemplate (used when list of messages are sent)


## Message Placeholder

A MessagePlaceholder in langchain is a special placeholder used inside a ChatPromptTemplate to dynamically insert the chat history or a list of messages in runtime.
