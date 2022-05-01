def add_arguments(parser):
    parser_lstm = parser.add_argument_group("lstm")
    parser_lstm.add_argument("--num_layers", type=int, help="Number of LSTM layers")
    parser_lstm.add_argument("--forward_size", type=int, help="Number of units in the forward propagation")
    parser_lstm.add_argument("--state_size", type=int, help="Number of units for the state vector")


class Lstm:
    def call(self, x):
        print("LSTM does something with x")
