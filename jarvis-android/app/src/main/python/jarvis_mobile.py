"""Android bridge into the genuine OpenJarvis cloud inference engine."""
import os
from openjarvis.engine.cloud import CloudEngine
from openjarvis.core.types import Message, Role

def ask(api_key: str, model: str, prompt: str) -> str:
    os.environ["OPENAI_API_KEY"] = api_key
    engine = CloudEngine()
    if not engine.health():
        raise RuntimeError("OpenJarvis could not initialize its cloud provider.")
    messages = [Message(role=Role.USER, content=prompt)]
    try:
        result = engine.generate(messages, model=model, temperature=0.7, max_tokens=1024)
        return result.get("content", "")
    finally:
        engine.close()
