#!/opt/conda/envs/morpheus/bin/python

import logging

import click

from morpheus.config import Config
from morpheus.config import CppConfig
from morpheus.messages.message_meta import MessageMeta
from morpheus.pipeline import LinearPipeline
from morpheus.stages.general.monitor_stage import MonitorStage
from morpheus.stages.input.kafka_source_stage import KafkaSourceStage
from morpheus.utils.logger import configure_logging

logger = logging.getLogger("morpheus.{__name__}")


@click.command()
@click.option(
    "--num_threads",
    default=1,
    type=click.IntRange(min=1),
    help="Number of internal pipeline threads to use.",
)
@click.option(
    "--pipeline_batch_size",
    default=1,
    type=click.IntRange(min=1),
    help=("Internal batch size for the pipeline. Can be much larger than the model batch size. "
          "Also used for Kafka consumers."),
)
@click.option('--bootstrap_servers', default='localhost:9092', help="Comma-separated list of bootstrap servers.")
@click.option('--input_topic',
              type=str,
              default='test_cm',
              help="Name of the Kafka topic from which messages will be consumed.")
@click.option('--group_id', type=str, default='ai-pf', help="Kafka input data consumer group identifier.")
def run_pipeline(num_threads, pipeline_batch_size, bootstrap_servers, input_topic, group_id):
    configure_logging(log_level=logging.DEBUG)

    CppConfig.set_should_use_cpp(False)

    config = Config()
    config.num_threads = num_threads
    config.pipeline_batch_size = pipeline_batch_size

    pipeline = LinearPipeline(config)

    pipeline.set_source(
        KafkaSourceStage(config, bootstrap_servers=bootstrap_servers, input_topic=input_topic, group_id=group_id))

    pipeline.add_stage(MonitorStage(config, description="Source rate"))

    pipeline.run()


if __name__ == "__main__":
    run_pipeline()
