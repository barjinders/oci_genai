
from langchain_community.embeddings import OCIGenAIEmbeddings
from langchain_community.llms import OCIGenAI
from config import compartment_id, auth_profile,service_endpoint,embeddings_model_id,llm_model_id,llm_model_kwargs,embeddings_model_kwargs

class OCIModelWrapper:
    def __init__(self):
        # Hardcoded parameters
        self.compartment_id = compartment_id
        self.auth_profile = auth_profile
        self.service_endpoint = service_endpoint
        self.embeddings_model_id = embeddings_model_id
        self.llm_model_id = llm_model_id
        self.llm_model_kwargs = llm_model_kwargs
        self.embeddings_model_kwargs = embeddings_model_kwargs
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
            model_kwargs=self.embeddings_model_kwargs
        )

    def initialize_llm(self):
        self.llm = OCIGenAI(
            model_id=self.llm_model_id,
            service_endpoint=self.service_endpoint,
            compartment_id=self.compartment_id,
            auth_type="API_KEY",
            auth_profile=self.auth_profile,
            model_kwargs=self.llm_model_kwargs
        )

