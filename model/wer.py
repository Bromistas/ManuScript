def calculate_wer(reference_text: str, ocr_output: str) -> int:
    """Return WER for a given text and the ocr output for that text"""

    reference_tokens = reference_text.split()
    ocr_tokens = ocr_output.split()

    # Substitutions
    S = sum(1 for r, o in zip(reference_tokens, ocr_tokens) if r != o)

    # Insertions
    I = max(len(ocr_tokens) - len(reference_tokens), 0)

    # Deletions
    D = max(len(reference_tokens) - len(ocr_tokens), 0)

    # Total words of reference text
    N = len(reference_tokens)

    wer = (S + I + D) / N
    return wer


def wer(original_texts: list[str], ocr_outputs: list[str]) -> int:
    """Return WER for a list of texts and their corresponding ocr outputs"""
    total_wer = 0
    for i, text in enumerate(original_texts):
        total_wer += calculate_wer(text, ocr_outputs[i])
    
    wer_score = total_wer/len(original_texts)
    return wer_score