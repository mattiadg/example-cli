from .register import register


@register("infer")
class Infer:
    def add_argument_group(self, parser):
        group = parser.add_argument_group("infer")
        group.add_argument(
            "--model_path", required=True, help="Path to the model to use for inference"
        )
        group.add_argument(
            "--batch_size", type=int, help="Batch size during inference"
        )

    def run(self, args):
        print("Inferring with model with:")
        for k,v in args.__dict__.items():
            print(f"{k}={v}")
