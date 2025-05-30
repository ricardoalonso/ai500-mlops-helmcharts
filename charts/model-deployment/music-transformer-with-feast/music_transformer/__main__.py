import argparse
import kserve
from kserve import logging

from .music_transformer import MusicTransformer

parser = argparse.ArgumentParser(parents=[kserve.model_server.parser])

parser.add_argument(
    "--scaler_file_path", 
    help="The file path to the scaler in the sidecar", 
    required=True
)
parser.add_argument(
    "--encoder_file_path", 
    help="The file path to the encoder in the sidecar", 
    required=True
)
parser.add_argument(
    "--feast_server_url",
    type=str,
    default="",
    help="The url of the Feast feature server.",
    required=True,
)
parser.add_argument(
    "--feature_service",
    type=str,
    help="Feature Service mapping to the relevant features for the model.",
    required=True,
)
parser.add_argument(
    "--entity_id_name",
    type=str,
    help="Name of the entity id we want to fetch.",
    required=True,
)

args, _ = parser.parse_known_args()

if __name__ == "__main__":
    transformer = MusicTransformer(
        name=args.model_name,
        predictor_host=args.predictor_host,
        predictor_protocol=args.predictor_protocol,
        predictor_use_ssl=args.predictor_use_ssl,
        scaler_file_path=args.scaler_file_path,
        encoder_file_path=args.encoder_file_path,
        feast_server_url=args.feast_server_url,
        feature_service=args.feature_service,
        entity_id_name=args.entity_id_name,
    )
    server = kserve.ModelServer()
    server.start(models=[transformer])