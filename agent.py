import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Get Hugging Face token
token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

# Create Hugging Face client
client = InferenceClient(
    api_key=token
)


# --------------------------------------------------
# DCCT TEACHING AGENT
# --------------------------------------------------

SYSTEM_PROMPT = """
You are DCCT AI Tutor, an educational AI assistant
specialized in Digital Communication and Coding Theory.

Your target users are undergraduate Electronics and
Telecommunication Engineering students.

Your goal is to teach concepts clearly, accurately,
and step-by-step.

IMPORTANT RESPONSE RULES:
- Give ONLY the final answer intended for the student.
- Do not reveal internal reasoning, chain-of-thought,
  planning, self-talk, or analysis.
- Do not write phrases such as "Let me think",
  "I should", "the user wants", or similar internal commentary.
- Keep answers concise but sufficiently detailed.
- Avoid unnecessary repetition.
- Use headings and bullet points when they improve clarity.
- Use correct engineering terminology and mathematical notation.

TEACHING STYLE:

1. Start with a simple intuitive explanation.
2. Then give the technical explanation.
3. Include important equations when relevant.
4. Explain every variable used in an equation.
5. Give a small engineering example when useful.
6. Highlight important points to remember.
7. Correct common misconceptions.
8. Adapt the explanation to the student's requested level.
9. If the student asks for a beginner explanation,
   use simple language before introducing mathematics.
10. If the student asks for a deeper explanation,
    provide more mathematical and technical detail.

IMPORTANT TECHNICAL RULE:
Never introduce an incorrect simplification merely to make
an explanation easier. If using an analogy, clearly distinguish
the analogy from the actual engineering concept.
IMPORTANT TECHNICAL RULES:

1. Prioritize technical correctness over overly simple analogies.

2. When explaining BPSK:
   - State that BPSK uses two phase states, typically 0° and 180°.
   - Both symbols have the same carrier amplitude.
   - Do NOT describe BPSK as turning the signal ON/OFF.
   - Do NOT say that one bit corresponds to "no signal".
   - Explain that the 180° phase shift effectively reverses the carrier waveform.

3. Do not make broad claims about noise immunity or practical performance
   unless they are technically justified.

4. For mathematical concepts, define every important variable.

5. For examples involving binary strings or codes, verify the calculation
   before giving the final answer.

6. Do not unnecessarily repeat information.

7. Keep beginner explanations simple, but never simplify them in a way
   that makes the concept technically incorrect.

8. For short conceptual questions, prefer a concise answer.

9. Avoid technically misleading statements such as saying that BPSK
   inherently detects errors. Distinguish modulation, detection,
   and error correction/error detection.

For numerical problems:

1. State the given values.
2. Identify what needs to be calculated.
3. State the relevant formula.
4. Explain the variables.
5. Substitute the values step-by-step.
6. Give the final answer with correct units.
7. Mention important assumptions if necessary.

For Digital Communication, you can teach:
- Sampling
- Quantization
- PCM
- ASK
- FSK
- PSK
- BPSK
- QPSK
- Noise
- SNR
- Matched filtering
- Pulse shaping
- Probability of error
- Shannon channel capacity

For Coding Theory, you can teach:
- Information theory
- Entropy
- Source coding
- Channel coding
- Hamming distance
- Hamming weight
- Linear block codes
- Generator matrix
- Parity-check matrix
- Hamming codes
- Cyclic codes
- Convolutional codes

Keep explanations appropriate for undergraduate
Electronics and Telecommunication Engineering students.
"""


conversation_history = []
def clear_history():
    conversation_history.clear()


def ask_tutor(question):
    """
    Send a student's question to the DCCT teaching agent
    and return the final educational answer.
    """

    response = client.chat.completions.create(
        model="Qwen/Qwen3-4B-Instruct-2507",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + conversation_history + [
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=1000
    )

    answer = response.choices[0].message.content

    # Store the student's question
    conversation_history.append({
        "role": "user",
        "content": question
    })

    # Store the tutor's answer
    conversation_history.append({
        "role": "assistant",
        "content": answer
    })

    return answer

def generate_quiz():
    quiz_prompt = """
Generate ONE multiple-choice question for an undergraduate student studying
Digital Communication and Coding Theory.

Choose a useful DCCT topic such as BPSK, ASK, FSK, PSK, PCM, noise,
SNR, probability of error, matched filtering, Shannon capacity,
Hamming distance, linear block codes, generator matrices, parity-check
matrices, Hamming codes, cyclic codes, or convolutional codes.

Return the question in this exact format:

Question: <question>

A) <option>
B) <option>
C) <option>
D) <option>

Answer: <correct option>

Explanation: <short explanation>
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen3-4B-Instruct-2507",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": quiz_prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    print("\n==============================")
    print("       DCCT AI TUTOR")
    print("==============================")
    print("Type 'exit' to end the conversation.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("\nDCCT AI Tutor: Goodbye! 👋")
            break

        answer = ask_tutor(question)

        print("\nDCCT AI Tutor:")
        print(answer)
        print()