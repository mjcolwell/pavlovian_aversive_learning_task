# Schedule generator for Binary Choice PAL task by Dr Michael Colwell (michael.colwell@psych.ox.ac.uk)

import numpy as np
import pandas as pd
from random import shuffle, randint, seed
import os

# Set seed for reproducibility
seed(777) # Version 1: 45; Version 2: 189; Version 3: 777
np.random.seed(777) #Version 1: 45; Version 2: 189; Version 3: 777

# Constants
N_PHASES = 7
TRIALS_PER_PHASE = [randint(25, 35) for _ in range(N_PHASES)]
REVERSAL_CUE = "Fractals/Version_3/ApoAV-250719-155.jpg"
STABLE_THREAT = "Fractals/Version_3/ApoAV-250719-247.jpg"
STABLE_SAFE = "Fractals/Version_3/ApoAV-250719-208.jpg"

# Outcome pool tracking
outcome_bank = {}

all_rows = []
trial_counter = 0

for phase_idx in range(N_PHASES):
    reversal_prob = 0.75 if phase_idx % 2 == 0 else 0.25
    reversal_label = "75_Threat" if reversal_prob == 0.75 else "75_Safe"

    n_trials = TRIALS_PER_PHASE[phase_idx]
    n_reversal = n_trials // 2
    n_stable = n_trials - n_reversal
    n_stable_each = n_stable // 2

    cues = ([REVERSAL_CUE] * n_reversal +
            [STABLE_THREAT] * n_stable_each +
            [STABLE_SAFE] * (n_stable - n_stable_each))
    shuffle(cues)

    rev_outcomes_this_phase = []

    rev_trial_counter = 0
    for i, cue in enumerate(cues):
        global_index = trial_counter + i

        if cue == REVERSAL_CUE:
            cue_type = "Reversal"
            cue_prop = reversal_label
            prob = reversal_prob
            rev_trial_counter += 1
        elif cue == STABLE_THREAT:
            cue_type = "Stable"
            cue_prop = "75_Threat"
            prob = 0.75
        else:
            cue_type = "Stable"
            cue_prop = "75_Safe"
            prob = 0.25

        # Strict outcome control
        cue_key = f"{phase_idx}_{cue}"
        if cue_key not in outcome_bank:
            count = cues.count(cue)
            n_ones = int(round(count * prob))
            n_zeros = count - n_ones
            outcome_list = [1] * n_ones + [0] * n_zeros
            np.random.shuffle(outcome_list)
            outcome_bank[cue_key] = outcome_list

        outcome = outcome_bank[cue_key].pop()

        # --- ✅ Enforce no 3x consecutive 25% outcomes for Reversal cues ---
        if cue == REVERSAL_CUE:
            rare_outcome = 0 if prob == 0.75 else 1  # 25% is the *unexpected* outcome
            if len(rev_outcomes_this_phase) >= 2:
                if rev_outcomes_this_phase[-2:] == [rare_outcome, rare_outcome] and outcome == rare_outcome:
                    outcome = 1 - rare_outcome  # force to expected
            rev_outcomes_this_phase.append(outcome)
        # ------------------------------------------------------------------

        # Oddball logic
        expected = int(prob >= 0.5)
        oddball = 1 if cue == REVERSAL_CUE and rev_trial_counter > 5 and outcome != expected else 0

        # Reversal_event instead of "Shift"
        reversal_event = 1 if i == 0 else 0

        high_prob_choice_corr = "right" if prob >= 0.5 else "left"

        all_rows.append([
            cue, cue_type, cue_prop, reversal_event, oddball, outcome, high_prob_choice_corr
        ])

    trial_counter += len(cues)

# ISIs
n_trials = len(all_rows)
pre_isi = np.round(np.random.uniform(2.5, 4.0, n_trials), 2)
int_isi = np.round(np.random.uniform(1.0, 2.5, n_trials), 2)

# Build dataframe
df = pd.DataFrame(all_rows, columns=[
    "Fractal_img", "Cue_Type", "Cue_Prop", "Reversal_event", "Oddball",
    "Outcome", "High_Prob_Choice_Corr"
])
df["Pre_ISI"] = pre_isi
df["Int_ISI"] = int_isi

# Save
output_path = "PAL_Deterministic Schedule.xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Script completed. File saved to: {output_path}")
