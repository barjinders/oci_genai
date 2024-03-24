
from langchain_community.embeddings import OCIGenAIEmbeddings
from langchain_community.llms import OCIGenAI

class OCIModelWrapper:
    def __init__(self):
        # Hardcoded parameters
        self.compartment_id = "<Compartment OCID>"
        self.auth_profile = "coeinfrastructure"
        self.service_endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
        self.embeddings_model_id = "cohere.embed-english-v3.0"
        self.llm_model_id = "cohere.command" #meta.llama-2-70b-chat
        self.model_kwargs = {"temperature": 0, "top_p": 0.75, "max_tokens": 1024}
        
        # Initialize both models upon instance creation
        self.initialize_embeddings()
        self.initialize_llm()

    def initialize_embeddings(self):
        self.embeddings = OCIGenAIEmbeddings(
            model_id=self.embeddings_model_id,
            service_endpoint=self.service_endpoint,
            compartment_id=self.compartment_id,
            auth_type="API_KEY",
            auth_profile=self.auth_profile,
            model_kwargs=self.model_kwargs
        )

    def initialize_llm(self):
        self.llm = OCIGenAI(
            model_id=self.llm_model_id,
            service_endpoint=self.service_endpoint,
            compartment_id=self.compartment_id,
            auth_type="API_KEY",
            auth_profile=self.auth_profile,
            model_kwargs=self.model_kwargs
        )

