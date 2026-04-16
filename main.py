from . import pipeline


if __name__ == '__main__':
    input_path = str(input("Input data file path: "))
    output_path = "./data"
    pipeline.run_pipeline(input_path, output_path)
