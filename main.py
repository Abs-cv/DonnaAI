from workflows.pipeline_workflow import create_pipeline
from utils.env_setup import load_env_variables

def main():
    \"\"\"Main entry point for running the pipeline.\"\"\"
    load_env_variables()

    task_type = "Image Classification"
    dataset_paths = "/path/to/dataset"
    user_test_prompt = "Analyze the dataset and generate a report."
    additional_info = "Include detailed statistics."

    pipeline = create_pipeline(task_type, dataset_paths, user_test_prompt, additional_info)
    pipeline.run()

if __name__ == "__main__":
    main()
