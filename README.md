# OCI Generative AI: RAG Demo

This project demonstrates the integration of Oracle Cloud Infrastructure's Generative AI capabilities with the Langchain and Llamaindex framework to create a robust Retrieval-Augmented Generation (RAG) application. By leveraging Oracle's powerful machine learning models and the flexibility of Langchain and Llamaindex users can achieve enhanced natural language processing tasks.

## OCI_RAG_Langchain.ipynb

The Jupyter notebook `OCI_RAG_Langchain.ipynb` serves as a comprehensive guide to utilizing the following components using Oracle Cloud Infrastructure:

- **Cohere Command LLM Model**: A state-of-the-art language model capable of understanding and generating human-like text based on the input provided.
- **"cohere.embed-english-v3.0" Embedding Model**: This embedding model processes text to produce vector representations, enabling the efficient retrieval of information by capturing the semantic similarity between text inputs.
- **Langchain Framework**: An open-source toolkit designed to facilitate the development of applications that combine language models with retrieval mechanisms, thereby enhancing the model's ability to generate informed and contextually relevant responses.

### Features

- **Integration with Oracle Cloud Infrastructure**: Demonstrates how to set up and use Oracle Cloud's Generative AI models within a cloud computing environment.
- **Retrieval-Augmented Generation**: Combines the power of language models with the precision of retrieval-based methods to improve the quality and relevance of generated text.
- **Practical Examples**: The notebook includes practical examples and use cases, showcasing the capabilities of the integrated system in real-world scenarios.


# OCI Generative AI: RAPTOR Framework Demonstration

This Jupyter notebook is dedicated to showcasing the capabilities of the **OCI Generative AI** based **RAG (Retrieval-Augmented Generation)** model, utilizing the innovative **RAPTOR Framework**. RAPTOR stands for **Recursive Abstractive Processing for Tree-Organized Retrieval**, a cutting-edge approach to information retrieval.

## Overview of RAPTOR

RAPTOR enhances the retrieval process by **recursively clustering** and **summarizing clusters** in layers, which significantly improves the efficiency and relevance of the retrieval in various applications. This notebook provides a hands-on demonstration of implementing RAPTOR with `llama-index`, leveraging the powerful `RAPTOR llama-pack`.

### Key Features of RAPTOR:

- **Tree Traversal Retrieval Mode**: This mode involves traversing the tree of clusters, performing a top-k retrieval at each level within the tree to efficiently narrow down the search space.

- **Collapsed Retrieval Mode**: In this mode, the entire tree is treated as a single, expansive pile of nodes. A simple top-k retrieval is performed across this collective set, offering a straightforward approach to information retrieval.

For a detailed understanding of the algorithms and methodologies underpinning RAPTOR, refer to the [original research paper](https://arxiv.org/abs/2401.18059).

## OCI_RAG_Raptor_LlamaIndex.ipynb

This notebook guides you through the steps to utilize the RAPTOR framework using LlamaIndex with OCI Generative AI's RAG model, including setup, configuration, and execution of retrieval tasks in both `tree_traversal` and `collapsed` modes. Dive in to explore the innovative world of recursive abstractive processing for enhanced retrieval capabilities.

### Documentation and Support
For more information on Oracle Cloud Infrastructure's Generative AI services and the Langchain framework, please refer to the official documentation:

[Oracle Cloud Infrastructure Documentation] (https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm) 
[Langchain GitHub Repository] (https://github.com/langchain-ai/langchain)

[RAPTOR research paper](https://arxiv.org/abs/2401.18059).

[Llama-Index-Pack] (https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-raptor/examples/raptor.ipynb)


### Getting Started

To get started with this project, you will need access to Oracle Cloud Infrastructure and the necessary permissions to use the Generative AI models. Clone the repository and follow the instructions in `OCI_RAG_Langchain.ipynb` to set up your environment, update the Compartment OCID in 'oci_model_wrapper.py' and begin experimenting with the technology.

```bash
git https://github.com/barjinders/oci_genai
cd oci_genai
```
Provide the auth config file.The default configuration file name and location is ~/.oci/config.

### Acknowledgments
I would like to extend my sincere gratitude to the following individuals on YouTube, whose invaluable tutorials and insights have significantly contributed to my learning and the successful completion of this demo. Their expertise and willingness to share knowledge have been instrumental in my development:

[Mehdi Allahyari](https://www.youtube.com/watch?v=bpeeqbBIH1A)

[Sam Witteveen](https://www.youtube.com/watch?v=3yPBVii7Ct0)

[Krish Naik](https://www.youtube.com/watch?v=zxo3T4aQj6Q)

[Prompt Engineering](https://www.youtube.com/@engineerprompt)

[llamaindex RAPTOR webinar](https://www.youtube.com/watch?v=Bhnq8grQm5Y&t=2067s)

[Greg Kamradt](https://www.youtube.com/@DataIndependent)


Their dedication to educating others in the field is truly inspiring, and I highly recommend their channels to anyone looking to expand their knowledge in GenAI.


For support, consider reaching out to the respective communities or the support channels provided by Oracle Cloud Infrastructure.
