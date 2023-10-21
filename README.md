# OpenAI-API-Model-List
'OpenAI Model Directory' is a simple Python program RUN in Terminal to see what OpenAI models are available to that specific API key.

Sure, let's give it a makeover:

---

# 📜 OpenAI Model Directory

Welcome to the **OpenAI Model Directory**. This Python utility lets you quickly check the models available for your OpenAI API key when executed in the terminal.

## 📌 Highlights

Based on the metadata provided, `gpt-4` stands out as the most advanced model:

🔸 Recent Model ID suggests it's newer than `gpt-3.5-turbo` and `davinci`.

🔸 Owned by the primary "openai", indicating it's not a test model.

🔸 Limited permissions suggest its powerful capabilities with tight access restrictions.

🔸 The naming convention aligns with top-tier models.

🔸 It's a standalone model, not a derivative of older models.

Note: Even though there are models like `gpt-3.5-turbo-16k` which have "16k" (indicating 16 billion parameters), none mention "32k" for 32 billion parameters.

## 🗃️ Model List

| Index | Model Name | Owner | Created Date | Permissions | Root Model |
|-------|------------|-------|--------------|-------------|------------|
| 1 | ada | openai | 1649358449 | allow_view, allow_sampling, allow_logprobs | ada |
| 2 | ada-code-edit-001 | openai | 1649917674 | allow_view, allow_sampling, allow_logprobs | ada-code-edit-001 |
| 3 | ada-code-search-code | openai-dev | 1651172505 | allow_view, allow_sampling, allow_logprobs, allow_search_indices | ada-code-search-code |
... [Many rows here for the models in between]
| 32 | gpt-4 | openai | 1687882411 |  | gpt-4 |
... [Continue with the rest of the models]
| 48 | text-curie-edit-001 | openai | 1649852284 | allow_view, allow_sampling, allow_logprobs | text-curie-edit-001 |


---


💡 Here is an indexed table format of the available model information:

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
