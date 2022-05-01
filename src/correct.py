import argparse

from commands import train, infer


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Example v3")
    parser.add_argument("command", choices=["train", "infer"])

    args_, _ = parser.parse_known_args()

    if args_.command == "train":
        group_train = parser.add_argument_group("train")
        group_train.add_argument(
            "--architecture",
            "-a",
            required=True,
            help="name of the deep learning architecture to use",
        )
        group_train.add_argument(
            "--save_model_path",
            required=True,
            help="Path to the directory where to save the model",
        )
        group_train.add_argument(
            "--dropout",
            type=float,
            default=0.1,
            help="Dropout value, equal for each value",
        )
        group_train.add_argument(
            "--batch_size", type=int, help="Batch size during training"
        )
    elif args_.command == "infer":
        group_infer = parser.add_argument_group("infer")
        group_infer.add_argument(
            "--model_path", required=True, help="Path to the model to use for inference"
        )
        group_infer.add_argument(
            "--batch_size", type=int, help="Batch size during inference"
        )

    args = parser.parse_args()

    if args.command == "train":
        train(args.architecture, args.save_model_path, dropout=args.dropout, batch_size=args.batch_size)
    elif args.command == "infer":
        infer(args.model_path, batch_size=args.batch_size)
