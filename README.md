# OpenAI-API-Model-List
'OpenAI API Model List' is a simple Python program RUN in Terminal to see what OpenAI models are available to that specific API key.

Based on the model information provided, the most advanced model appears to be:

gpt-4

Here are a few reasons why gpt-4 seems to be the most advanced:

- It has the highest model ID in the sequence, indicating it was created more recently than other models like gpt-3.5-turbo and davinci. Newer models tend to be more advanced.

- It is owned by "openai" rather than "openai-dev" or "openai-internal", suggesting it is a production model rather than a test model.

- It has a very limited permissions set, with no allowances for logprobs, sampling, search indices, etc. This implies that gpt-4 is extremely powerful, and access is tightly restricted.

- The name follows the pattern of previous cutting-edge models like gpt-3 and gpt-2 rather than test model names like "text-similarity-babbage-001".

- No parents are listed, indicating gpt-4 is not an iteration or fine-tuning of an older model.

So while details like model size are not provided, gpt-4 appears to be the most advanced model overall based on the metadata and permissions. The tight access controls, in particular, suggest it represents the current state-of-the-art in language models from Anthropic.

Based on the model information in the table, no models contain "32k" in their name or description. The models with the largest parameter sizes seem to be:

- gpt-3.5-turbo-16k 
- gpt-3.5-turbo-16k-0613
- gpt-4
- gpt-4-0314

These models have "16k" in their name, indicating they likely have around 16 billion parameters. But there are no models with "32k" that would indicate 32 billion parameters.

Here is an indexed table format of the available model information:

| Model ID | Model Name | Owner | Created Date | Permissions | Root Model |
|-|-|-|-|-|-|  
| text-search-babbage-doc-001 |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-search-babbage-doc-001 |
| gpt-3.5-turbo-16k-0613 |  | openai | 1685474247 | allow_view, allow_sampling, allow_logprobs | gpt-3.5-turbo-16k-0613 |
| curie-search-query |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | curie-search-query |
| gpt-3.5-turbo-16k |  | openai-internal | 1683758102 | allow_view, allow_sampling, allow_logprobs | gpt-3.5-turbo-16k |  
| text-search-babbage-query-001 |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-search-babbage-query-001 |
| babbage |  | openai | 1649358449 | allow_view, allow_sampling, allow_logprobs | babbage |
| babbage-search-query |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | babbage-search-query |
| text-babbage-001 |  | openai | 1649364043 | allow_view, allow_sampling, allow_logprobs | text-babbage-001 |  
| text-similarity-davinci-001 |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-similarity-davinci-001 |
| davinci |  | openai | 1649359874 | allow_view, allow_sampling, allow_logprobs | davinci |
| davinci-similarity |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | davinci-similarity |
| code-davinci-edit-001 |  | openai | 1649880484 | allow_view, allow_sampling, allow_logprobs | code-davinci-edit-001 |
| curie-similarity |  | openai-dev | 1651172510 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | curie-similarity |
| babbage-search-document |  | openai-dev | 1651172510 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | babbage-search-document |
| curie-instruct-beta |  | openai | 1649364042 | allow_view, allow_sampling, allow_logprobs | curie-instruct-beta | 
| text-search-ada-doc-001 |  | openai-dev | 1651172507 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-search-ada-doc-001 |
| davinci-instruct-beta |  | openai | 1649364042 | allow_view, allow_sampling, allow_logprobs | davinci-instruct-beta |
| gpt-4 |  | openai | 1687882411 |  | gpt-4 |
| text-similarity-babbage-001 |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-similarity-babbage-001 |  
| text-search-davinci-doc-001 |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-search-davinci-doc-001 |
| gpt-4-0314 |  | openai | 1687882410 |  | gpt-4-0314 |
| babbage-similarity |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | babbage-similarity |
| davinci-search-query |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | davinci-search-query |  
| text-similarity-curie-001 |  | openai-dev | 1651172507 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-similarity-curie-001 |
| text-davinci-001 |  | openai | 1649364042 | allow_view, allow_sampling, allow_logprobs | text-davinci-001 |
| text-search-davinci-query-001 |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-search-davinci-query-001 |
| ada-search-document |  | openai-dev | 1651172507 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | ada-search-document |
| ada-code-search-code |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | ada-code-search-code |
| babbage-002 |  | system | 1692634615 | allow_view, allow_sampling, allow_logprobs | babbage-002 |
| davinci-002 |  | system | 1692634301 | allow_view, allow_sampling, allow_logprobs | davinci-002 |
| davinci-search-document |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | davinci-search-document |  
| curie-search-document |  | openai-dev | 1651172508 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | curie-search-document |
| babbage-code-search-code |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | babbage-code-search-code |
| text-search-ada-query-001 |  | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | text-search-ada-query-001 |
| text-curie-001 |  | openai | 1649364042 | allow_view, allow_sampling, allow_logprobs | text-curie-001 |
| ada |  | openai | 1649358449 | allow_view, allow_sampling, allow_logprobs | ada |
| ada-search-query |  | openai-dev | 1651172507 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | ada-search-query |  
| curie |  | openai | 1649359874 | allow_view, allow_sampling, allow_logprobs | curie |
| curie-code-search-code |  | openai-dev | 1651172509 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | curie-code-search-code |
| text-ada-001 |  | openai | 1649364042 | allow_view, allow_sampling, allow_logprobs | text-ada-001 |
| ada-similarity |  | openai-dev | 1651172507 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | ada-similarity |
| babbage-code-edit-001 |  | openai | 1649917713 | allow_view, allow_sampling, allow_logprobs | babbage-code-edit-001 |
| text-davinci-edit-001 |  | openai | 1649852269 | allow_view, allow_sampling, allow_logprobs | text-davinci-edit-001 |  
| text-babbage-edit-001 |  | openai | 1649852284 | allow_view, allow_sampling, allow_logprobs | text-babbage-edit-001 |
| text-ada-edit-001 |  | openai | 1649852284 | allow_view, allow_sampling, allow_logprobs | text-ada-edit-001 |
| text-curie-edit-001 |  | openai | 1649852284 | allow_view, allow_sampling, allow_logprobs | text-curie-edit-001 |
| davinci-code-edit-001 |  | openai | 1649917752 | allow_view, allow_sampling, allow_logprobs | davinci-code-edit-001 |
| curie-code-edit-001 |  | openai | 1649917674 | allow_view, allow_sampling, allow_logprobs | curie-code-edit-001 |
| ada-code-edit-001 |  | openai | 1649917674 | allow_view, allow_sampling, allow_logprobs | ada-code-edit-001 |
