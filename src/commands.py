def train(args):
    print("Training model with:")
    for k, v in args.__dict__.items():
        print(f"{k}={v}")


def infer(args):
    print("Inferring with model with:")
    for k, v in args.__dict__.items():
        print(f"{k}={v}")
