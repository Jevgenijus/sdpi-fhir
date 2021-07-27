import sys
import argparse
import xmlrunner

from Tooling.Tests.TestLogger import logger, setUpLogger
from Tooling.Tests.ReferenceConsumer import ReferenceConsumer

class TestRunnerTool:

    ENDPOINT_ARG = "Endpoint reference address to test."

    def __init__(self):

        parser = argparse.ArgumentParser(
            description='Reference Provider/Consumer Specification tests',
            usage='''TestRunner <command> [<args>]

            The commands are:
               consumer    Executes tests against provider with specific endpoint reference address. Example: consumer 24639edc-c215-11eb-bd49-f8cab80f9344.
            ''')
        parser.add_argument('command', help='Command to run')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            logger.error(f"Command {args.command} not found.\n")
            parser.print_help()
            exit(1)
        self.runner = xmlrunner.XMLTestRunner()

        getattr(self, args.command)()

    def consumer(self):
        parser = argparse.ArgumentParser(description='Executes tests against provider with'
                                                     ' specific endpoint reference address. \n'
                                                     'Example: consumer 24639edc-c215-11eb-bd49-f8cab80f9344.')
        parser.add_argument('endpoint', metavar='endpoint', help=self.ENDPOINT_ARG)
        args = parser.parse_args(sys.argv[2:])
        logger.info("Executing consumer test for endpoint %s", args.endpoint)
        ReferenceConsumer.runReferenceConsumerTestSuite(args.endpoint)

if __name__ == '__main__':
    setUpLogger()
    TestRunnerTool()