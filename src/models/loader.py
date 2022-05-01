import importlib


def load_model_args(parser, model):
    module = importlib.import_module("."+model, "models")
    module.add_arguments(parser)
