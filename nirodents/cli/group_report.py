from niworkflows.reports.core import Report
rodents_path = "/oak/stanford/groups/russpold/data/rodents/derivatives/antsai-yes/ratLCdfMRI_RAS/"
Report("/home/oesteban/tmp/nirodents/out/", "madeoutuid", reportlets_dir=rodents_path, config="group.yml").generate_report()