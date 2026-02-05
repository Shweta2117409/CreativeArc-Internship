# Simple text generation demo (conceptual example)

def generate_text(prompt):
    responses = {
        "What is AI?": "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
        "Explain neural networks": "Neural networks are models inspired by the human brain and are used to recognize patterns in data.",
        "What is Generative AI?": "Generative AI refers to models that can create new content such as text, images, or code."
    }

    return responses.get(prompt, "This is a generated response based on learned patterns.")

if __name__ == "__main__":
    prompt = "What is Generative AI?"
    print("Prompt:", prompt)
    print("Generated Text:", generate_text(prompt))
