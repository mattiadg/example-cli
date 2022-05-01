def add_arguments(parser):
    parser_trafo = parser.add_argument_group("transformer")
    parser_trafo.add_argument("--num_layers", type=int, help="Number of Transformer layers")
    parser_trafo.add_argument("--forward_size", type=int, help="Number of units in the forward propagation")
    parser_trafo.add_argument("--hidden_size", type=int, help="Number of units in the hidden FF layers")


class Transformer:
    def call(self, x):
        print("Transformer does something with x")
