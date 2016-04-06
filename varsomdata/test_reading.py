import os
import pickle
import datetime as dt
import setenvironment as env
# import makepickle as mp
from getproblems import get_all_problems
# from getregobs import get_problems_from_AvalancheWarnProblemV

import pylab as plt

def get_data():
    region_id = 118
    from_date = dt.date(2015, 12, 1)
    to_date = dt.date(2016, 4, 5)


    # all_problems = get_problems_from_AvalancheWarnProblemV(region_id, from_date, to_date) # no danger level
    # a = 1

    all_problems = get_all_problems(region_id, from_date, to_date)


    var_prob = []
    var_prob_1_slabs = []
    var_prob_1_loose = []
    obs_prob = []
    for prob in all_problems:
        if prob.source == 'Varsel':
            var_prob.append(prob)
            if prob.order == 0:
                if prob.cause_tid == 24:
                    var_prob_1_loose.append(prob)
                else:
                    var_prob_1_slabs.append(prob)
        else:
            obs_prob.append(prob)

    print len(var_prob_1_slabs)
    print len(var_prob_1_loose)


    with open(os.path.join(env.local_storage, 'slab_probs.pck'), 'w') as f:
        pickle.dump(var_prob_1_slabs, f)


def load_data():
    with open(os.path.join(env.local_storage, 'slab_probs.pck')) as f:
        var_prob_1_slabs = pickle.load(f)

    danger_levels = []
    issue_dates = []

    for prob in var_prob_1_slabs:
        danger_levels.append(prob.danger_level)
        issue_dates.append(prob.date)

    plt.plot(issue_dates, danger_levels)
    plt.show()

'''
.danger_level
.aval_probability
.aval_trigger
.aval_size
.cause_name
.cause_tid # TODO: separate between dry/wet loose snow avalanches, wet slabs and, dry slabs
'''

if __name__ == "__main__":
    get_data()
    load_data()
    a = 1