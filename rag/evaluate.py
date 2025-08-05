# rag/evaluate.py


def run_tests(generated_code, test_list):
    local_env = {}
    try:
        exec(generated_code, {}, local_env)  # Injects code into local_env
        for test in test_list:
            exec(test, {}, local_env)
        return True
    except Exception as e:
        return False, str(e)
