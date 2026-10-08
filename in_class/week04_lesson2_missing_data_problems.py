#%%
# Week 04, Lesson 2: Missing Data Team Problems
#
# Work with your group to complete each problem.
# Every problem should be solved with Polars.

from pathlib import Path

import polars as pl


# Find the CSV beside this Python file, even when cells are run interactively.
DATA_FILE = "student_learning_missing.csv"

# Load the local dataset.
students = pl.read_csv(DATA_FILE)

# Preview the data before beginning the problems.
students.head()


# %%

#%%
# Problem 1: Count the missing values
#
# Create a one-row DataFrame showing the null count for every column.
# Save the result as missing_counts.

missing_counts = students.null_count()
missing_counts


#%%
# Problem 2: Find rows with a missing quiz score
#
# Return student_id, program, and quiz_score for only the students whose
# quiz_score is null. Save the result as missing_quiz_scores.

missing_quiz_scores = (
    students.select("student_id","program","quiz_score")
    .filter(pl.col("quiz_score").is_null())
)
missing_quiz_scores


#%%
# Problem 3: Find rows missing either major score
#
# Count how many students are missing quiz_score OR project_score.
# Save the single number as students_missing_a_score.

students_missing_a_score = (
    students.filter((pl.col("quiz_score").is_null())|(pl.col("project_score").is_null()))
    .shape[0]
)
students_missing_a_score


#%%
# Problem 4: Turn a placeholder into a real null
#
# The program column uses the text "Not reported" as disguised missing data.
# Replace that text with null and save the new DataFrame as programs_fixed.
# Keep every row and every column.

programs_fixed = (
    students.with_columns(pl.col("program").replace("Not reported",None))
)
programs_fixed


#%%
# Problem 5: Fill a missing category
#
# Starting with programs_fixed, fill null values in program with "Undeclared".
# Save the result as programs_filled.

programs_filled = (
    programs_fixed.with_columns(pl.col("program").replace(None,"Undeclared"))
)
programs_filled


#%%
# Problem 6: Fill a missing numeric value with the median
#
# Fill missing study_hours values with the median of study_hours.
# Save the completed DataFrame as study_hours_filled.

study_hours_filled = (
    students.with_columns(pl.col("study_hours").replace(None,pl.col("study_hours").mean()))
)
study_hours_filled

#%%
# the star in front of the "" is unpacking, a python function removes the list and keeps the insides
group_by = (
    students.group_by("program")
    .agg(pl.col("study_hours").mean(), (pl.col("sleep_hours").mean()))
)

group_by


#%%
# Problem 7: Fill a missing count with zero
#
# A missing tutoring_sessions value means the student attended no sessions.
# Fill those null values with 0 and save the result as tutoring_filled.

tutoring_filled = None  # TODO: Replace None with your Polars code.
tutoring_filled


#%%
# Problem 8: Convert an impossible value to null
#
# attendance_pct contains -1 when attendance was not recorded.
# Use pl.when(), pl.then(), and otherwise() to replace negative attendance
# values with null. Keep valid percentages unchanged.
# Save the result as attendance_fixed.

attendance_fixed = None  # TODO: Replace None with your Polars code.
attendance_fixed


#%%
# Problem 9: Remove rows that cannot be used for a quiz analysis
#
# Drop only the rows where quiz_score is null.
# Save the result as quiz_ready.

quiz_ready = None  # TODO: Replace None with your Polars code.
quiz_ready


#%%
# Problem 10: Label rows that need score follow-up
#
# Add a column named score_status.
# Its value should be "Needs follow-up" when quiz_score OR project_score is
# null; otherwise, its value should be "Complete".
# Save the result as score_status_added.

score_status_added = None  # TODO: Replace None with your Polars code.
score_status_added


#%%
# Problem 11: Fill several numeric columns with their own medians
#
# Use a list comprehension to fill null values in study_hours, sleep_hours,
# quiz_score, and project_score. Each column must use its own median.
# Save the result as numeric_values_filled.

numeric_columns = [
    "study_hours",
    "sleep_hours",
    "quiz_score",
    "project_score",
]

numeric_values_filled = None  # TODO: Replace None with your Polars code.
numeric_values_filled


#%%
# Problem 12: Create a complete score table
#
# Remove students missing either quiz_score or project_score.
# Keep student_id, program, quiz_score, and project_score.
# Sort the rows from highest quiz_score to lowest quiz_score.
# Save the result as complete_scores.

complete_scores = None  # TODO: Replace None with your Polars code.
complete_scores


#%%
# Final check
#
# After the problems are complete, use this cell to display the final table.

if isinstance(complete_scores, pl.DataFrame):
    print(complete_scores)
else:
    print("Complete Problem 12, then run this cell again.")
