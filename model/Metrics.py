import jiwer


def Calculate_WER(reference: list[str], hypothesis: list[str]) -> float:
    """Calculates WER metric for one or multiple transcriptions"""

    wer = jiwer.wer(reference, hypothesis)
    return wer


def Calculate_CER(reference: list[str], hypothesis: list[str]) -> float:
    """Calculates CER metric for one or multiple transcription"""

    cer = jiwer.cer(reference, hypothesis)
    return cer
