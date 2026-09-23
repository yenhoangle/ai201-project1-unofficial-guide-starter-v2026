def judge(question, expects, answer, results) -> bool: 
    return expects.lower().strip() in answer.lower().strip()

def retrieval_hits(expects, results) -> bool:
    """
    Returns True if the expected answer is in the top-k retrieval results.
    """
    for result in results:
        if expects.lower().strip() in result.lower().strip():
            return True
    return False