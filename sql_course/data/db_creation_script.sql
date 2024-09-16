
create table courses (
course_id integer, 
course_name text,
course_desc text, 
course_category text, 
course_level text, 
start_date date, 
num_weeks integer, 
num_learners_registered integer, 
num_TAs integer,
nps integer
);




create table course_info (
course_id integer, 
course_name text,
course_desc text, 
course_category text, 
course_level text 
);


create table instructors (
instructor_id integer,
name text,
affiliation text,
teaching_experience integer
);





create table learners (
learner_id integer,
name text,
affiliation text
);




create table course_run (
course_run_id integer,
course_id integer,
instructor_id integer,
start_date date,
num_weeks integer,
num_TAs integer,
nps integer
);




create table course_registration_info (
course_run_id integer,
learner_id integer
);

