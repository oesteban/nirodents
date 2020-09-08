"""Command Line Interface to generate group reports"""

import os
from pathlib import Path

def get_parser():
    """Build parser object."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    
    parser = ArgumentParser(
        prog="generate_group_report",
        description="""generate_group_report -- Create group report based on individual reportlets.""",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-r", "--reports", type=Path, help="The location of reportlet files.", required=True
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="The output location for report."
    )
    parser.add_argument(
        "-n", "--report-name", help="The output file name."
    )
    return parser

def main():
    """Entry point."""
    from niworkflows.reports.core import Report
    opts = get_parser().parse_args()
    if opts.output is None:
        opts.output = opts.reports
    if opts.report_name is None:
        opts.report_name = 'group_report.html'
    
    Report(
        out_dir=opts.output,
        run_uuid="madeoutuid",
        reportlets_dir=opts.reports,
        config="group.yml",
        out_filename=opts.report_name,
        ).generate_report()
    

if __name__ == "__main__":
    raise RuntimeError(
        """\
nirodents/cli/group_report.py should not be run directly;
Please `pip install` nirodents and use the `generate_group_report` command."""
    )
