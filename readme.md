# Getting structured JSON output using Pydantic and Instructor

This example demonstrates how to get consistent structured output from Large Language Models (LLMs) using the [Pydantic](https://docs.pydantic.dev/latest/) and [Instructor](https://python.useinstructor.com/) libraries.

The example extracts key details from an existing resume in Markdown format `./data/resume.md` and outputs the data in a structured JSON format as `./data/resume.json`. The JSON output confirms to Pydantic schemas.

## Instructor

Instructor is an open-source re-prompting based structured output library.

Instructor makes it easier to get structured and typed outputs directly from LLMs using Pydantic schemas.

When an LLM output doesn't match the format requested, then it will try again until it validates the desired output, or reaches the maximum number of retries.

![alt text](https://github.com/user-attachments/assets/c592f771-bd25-4ccc-a566-244069174867 "Instructor Flowchart")

### Instructor Pros:

- Simple to use.
- Requires less prompt engineering. Developers can focus more on defining desired outputs, rather than fiddling with prompts.
- Works with any LLM Application Programming Interface (API).
- Uses a consistent API across providers, such as OpenAI or Anthropic. This prevents vendor lock-in.
- Supports everything that Pydantic does. This catches formatting issues early and makes it easy to define and test output structures without writing custom parsing logic.
- Allows Field Regular Expressions, for example to ensure valid date formats or email addresses.

### Instructor Cons:

- Although Instructor will be successful in most cases, Instructor cannot fully enforce structure.
- Multiple LLM retries increase costs.

## Required API key for this example

You need an OpenAI API key for this example. [Get your OpenAI API key here](https://platform.openai.com/login). Insert the OpenAI API key into the `.env.example` file and then rename this file to just `.env` (remove the ".example" ending).
