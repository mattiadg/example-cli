import argparse

from commands import train, infer


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Example v2")
    subparsers = parser.add_subparsers(help="Sub-commands help")

    parser_train = subparsers.add_parser("train", help="Train a model")
    parser_train.add_argument(
        "--model",
        "-m",
        required=True,
        help="name of the deep learning architecture to use",
    )
    parser_train.add_argument(
        "--save_model_path",
        required=True,
        help="Path to the directory where to save the model",
    )
    parser_train.add_argument(
        "--dropout",
        type=float,
        default=0.1,
        help="Dropout value, equal for each value",
    )
    parser_train.add_argument(
        "--batch_size", type=int, help="Batch size during training"
    )
    parser_train.set_defaults(func=train)

    parser_infer = subparsers.add_parser("infer", help="Use a model for inference")
    parser_infer.add_argument(
        "--model_path", required=True, help="Path to the model to use for inference"
    )
    parser_infer.add_argument(
        "--batch_size", type=int, help="Batch size during inference"
    )
    parser_infer.set_defaults(func=infer)

    args = parser.parse_args()
    args.func(args)
