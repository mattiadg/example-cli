import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Example v2")
    parser.add_argument("command", choices=["train", "infer"])

    args_ = parser.parse_args()

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
