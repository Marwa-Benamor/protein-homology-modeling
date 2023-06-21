from modeller import *
from modeller.automodel import *
log.verbose()
env = Environ()
env.io.atom_files_directory = './'

a = AutoModel(env,
              alnfile='ali.pir',
              knowns='1jd7_clean',
              sequence='alpha_amy')
a.starting_model = 1
a.ending_model = 10
a.make()

# Open file for writing scores
with open('score.txt', 'w') as f:
    # Assess normalized DOPE score of each model
    for i in range(a.starting_model, a.ending_model + 1):
        filename = '{0}.B999900{1}.pdb'.format(a.sequence, str(i).zfill(2))
        mdl = Model(env, file=filename)
        score = mdl.assess_normalized_dope()
        f.write("Model %d: Score %.10f\n" % (i, score))

print("Scores written to score.txt")