from .register import register


@register("train")
class Train:
    def add_argument_group(self, parser):
        group = parser.add_argument_group("train")
        group.add_argument(
            "--architecture",
            "-a",
            required=True,
            help="name of the deep learning architecture to use",
        )
        group.add_argument(
            "--save_model_path",
            required=True,
            help="Path to the directory where to save the model",
        )
        group.add_argument(
            "--dropout",
            type=float,
            default=0.1,
            help="Dropout value, equal for each value",
        )
        group.add_argument(
            "--batch_size", type=int, help="Batch size during training"
        )

    def run(self, args):
        print("Training model with:")
        for k, v in args.__dict__.items():
            print(f"{k}={v}")
