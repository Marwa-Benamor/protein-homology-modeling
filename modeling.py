# Homology modeling by the automodel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = './'

a = automodel(env,
              alnfile  = 'ali.pir',     # alignment filename
              knowns   = '1jd7_clean',              # codes of the templates
              sequence = 'alpha_amy',               # code of the target
	      assess_methods=(assess.DOPE))
a.starting_model= 1                 # index of the first model
a.ending_model  = 10                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modeling

