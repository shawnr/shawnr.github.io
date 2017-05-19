Title: Python Education Summit 2017 Notes
Date: 2017-05-18 10:00
Modified: 2017-05-18 14:00
Category: Events
Tags: Python, conference, education
Summary: Notes from the Python Ed Summit 2017 in Portland, OR. Speakers included: Luciano Ramalho, Charolotte Chang, Jessica Ingrasselino, and more.

The Python Education Summit is happening on May 18, 2017 in Portland, OR. I am
writing some notes as we go through the day. Apologies to all of the great things
I've missed in these notes (some of the sessions run simultaneously, and I can,
unfortunately, only be in one place at a time).

## Keynote&mdash;Luciano Ramalho

Coming with a long history of development and teaching experience, Ramalho
discussed his personal history learning to program as well as some of the
exciting tools and methods of teaching programming in classrooms today. Ramalho
humorously recounted his dismal Study Hall experience when he first moved to
the US, and how the installation of Apple ][ machines in the library liberated
him from the doldrums of sitting quietly in a classroom for an hour.

Ramalho asked, appropriately, "Why did only two of us in the whole classroom
take the opportunity to teach ourselves to program?" He discussed with the
audience, which led to lots of ideas about fear of failure or not wanting to be
different from the rest of the group.

I think those are all valid points, but I wonder if it was more the result of a
lack of vision: Those kids had no way to understand the valuable benefits they
would get from learning to code. This is something I think many people deal with
today: They don't really know what is involved with writing code, and they have
no idea of how learning to code could be beneficial. It's a reflection of the
poor understanding that people have of coding and software in general.

It seems to me unfair to expect students to be able to realize the benefit of
learning something they have no idea about. It's exceptional when students can
lead themselves to that point, but it's totally understandable why a student
would not be able to get there without help. This is why it's so important to
begin education about coding and software early in our educational careers.

## Charlotte Chang&mdash;Climbing Rocks and Coding Blocks

Chang dicussed the challenges of learning to code and the ways in which these
challenges can feel intimidating, scary, and dangerous. She made several great
analogies to rock climbing (if you climb, you expect falls; if you code, expect
failures) and generally asserted the idea that learning to code is a risky
endeavor.

Chang's examples and experiences definitely echo with me both personally and
in terms of what I see in my students. There are many examples of students
defeating themselves before they ever really get going due to the fear of
failure, feelings of inadequacy, and generally discouraging experiences of
frustration and exasperation.

## Jessica Ingrassellino&mdash;Teaching a Diverse Population

Ingrassellino provided an impromptu talk filling in for a speaker whose Visa was
denied and, therefore, was prevented from attending the conference.

Ingrassellino provided a helpful talk discussing ways in which she accommodates
students with diverse needs and abilities in the classroom. She stressed the
need to create a safe space where students could fail without fear, but also
to modulate content to better reach students. She did a good job underlining the
basics of differentiated pedagogy and concerning ourselves with the social
well-being of the classroom.

## Lightning Talks

I am not going to provide full summaries of the Lightning Talks (they go too
quickly!), but here are some takeaways:

* PyCon UK has a great Education track!
* Logo is still relevant, programming with graphics is fun and good.
* Processing (the visual programming framework) with the Python module is cool.
* Helping students learn to ask questions is crucial.
* Answers that students discover themselves are much more meaningful and resilient.
* Show students what success looks like.
* Show students what failure looks like.
* Adafruit is a cool company that makes systems on which you can write Python.
* Adafruit has new, tiny, cheap chips that you can use to build cool things.
* Programming is a way of thinking. [Read more about it here.](https://blogs.scientificamerican.com/guest-blog/programming-as-a-way-of-thinking/)
* Visual Bash.

## Andrew M. Dawes&mdash;Teaching Quantum Mechanics with Python

[Dawes](http://amcdawes.com) discussed using [Jupyter](http://jupyter.org/) and
[QuTip](http://qutip.org/) to teach Quantum Mechanics to undergrads. Robust tools
allow students to work through material in an interactive way, and give the
students ways to do _real_ quantum mechanics work using the same tools used by
professional researchers.

Students are not required to have any prior Computer Science or programming
before taking this course. They have been exposed to other Math-based tools (like
Maple), so the interface and code is not totally foreign, but it is a
substantial amount of new stuff. Students work together to get through challenges.
Class time includes pair programming work.

Jupyter Notebook allows for a much more smooth integration of the advanced QuTiP
tool into the classroom. The notebook allows information to be conveyed with
interactivity. Example problems can be provided with solutions that students can
interrogate and learn better from. Examples from the book can also be
re-created in the notebook, allowing students to investigate those examples
more fully, too.

Students write code in labs, where they are able to work together, spend more
time investigating concepts, and easily get help in order to maximize their
understanding.

Key takeaways (summarized by Dawes in his slides):
* Find real-world frameworks
* Re-create examples so they can reinforce what they read in their books
* Don't be afraid to give out fully-worked examples
* Encourage tinkering

## Carol Willing&mdash;JupyterHub: Interactive Learning and Classrooms at Scale

What is learning? "Learning results from what the student does and thinks, and
only from what the student does and thinks" (Herbert Simon). Willing points out
many ways in which Jupyter Notebooks inspire people to "play" with them: change
elements, experiment to get different results, and do lots of different things
with very few lines of code.

Jupyter has diversified since the iPython Notebook days. The iPython core team
develops the Python core of Jupyter, and then other community developers
contribute modules to run over 70 other languages. This has allowed the concept
of the Notebook to move beyond the boundaries of any one language.

Jupyter Hub allows for web-based Notebooks, sharing, and collaboration without
requiring local installs of the software. Goal is to remove the hurdles for
getting started with Notebooks.

After discussion of the value of Notebooks for providing valuable features and
experiences, Willing discussed some additional pedagogical concepts. Discussing
how the learning process works, Willing listed three major steps:

* Motivate - Teachers must inspire students to learn.
* Develop Mastery - Students must actually build skills and understanding
* Apply Knowledge - Students can use their skills and understanding to solve
real problems in real situations.

Willing describes how Jupyter Notebooks help accomplish these goals. Notebooks
can help motivate, help develop mastery, and then can actually be a tool used
by students to apply their knowledge. Willing also goes through several examples
of how Jupyter Notebooks and Jupyter Hub have been used in real courses.

**Motivation**

The [nbviewer](https://nbviewer.jupyter.org) is an example of something that
can motivate students by showing them cool things that people have done and
enticing them to jump in and start experimenting with an existing Notebook.

Willing worked with Jessica Keller's _Intro to Python_ workshop to translate the
workshop information and goals into Notebooks that students could work through
and then take home and continue experimenting and learning (or refer back to).
The Notebooks reduced the stress level of students during the workshop.

Willing describes a course taught by Demba Ba at Harvard to teach singal processing
using wearables and Jupyter Notebooks. (See SciPy 2016 talk for more details.)

**Develop Mastery**

Kristen Thyng teaches Python for Geosciences and uses the nbgrader tool to handle
grading. Her course also begins with simple information and then seamlessly allows
students to increase the complexity of what they are doing.

Tanya Schlusser teaches R with Jupyter Notebooks. She uses a flipped classroom
approach to allow students to engage with materials at home, and in class they
focus on working in Notebooks on code, examples, problems, etc. Class sessions
are designed around short, practical challenges.

Brian Granger teaches Data Science at Cal Poly SLO that includes Jupyter
Notebooks, Ansible, etc. Notebooks allow students to get much further than would
otherwise be possible.

**Apply Knowledge**

UC Berkeley Data Science course (Data 8) is a cross-disciplinary course offered
campus-wide that teaches data science with Notebooks and includes instruction
for deploying [Jupyter Hub with Kubernetes](http://zero-to-jupyterhub.readthedocs.io/).

Jupyter Labs is a new product coming that will allow more complex Notebook
creation including more media. Keep an eye out for this to launch and bring new
features.

## Al Sweigart&mdash;Tortuga.py: Expanding Turtle.py Beyond English

Sweigart points out that Python has some great features for teaching new coders
using the classic Turtle programming module `turtle.py`. Considering teaching
students whose native language is not English, Sweigart came to feel that the
use of English words to program the Turtle ("up", "down", "left", "right", etc.)
add to the difficulty of learning to program. Although key words ("for", "in", etc.)
cannot be translated into other languages, the rest of the `turtle.py` module has
been translated into Spanish and is available as Tortuga (`pip install tortuga`).

This definitely makes the code for Turtle scripts more accessible to coders in
foreign languages. Sweigart has outlined a technical plan for improving the
`turtle.py` component in the standard Python library in order to make this change
fully accessible to people wanting to teach code in a foreign language. Each
added language only adds about 4k of code to the package, which should allow for
many other languages to be supported.

Sweigart hopes to encourage people to work with him to complete the project and
eventually get the translations added to the standard library. He welcomes
anyone to come work on the `Tortuga.py` project with him. [Check out his
presentation here](http://bit.ly/tortugapy).

## Dan Pozmanter&mdash;Teaching Practical Python

Pozmanter wants to ease the frustration and anxiety students feel when they get
out of school and into real-world projects. He discusses the need to create
assignments/projects that are ambitious enough that students need to ask
questions about "perspective":

* Thinking ahead
* Thinking behind
* Thinking sideways

Simple projects do not encourage this kind of thinking. And projects that are
too difficult make it impossible for students to do a good job of thinking
through the project. It's a challenge to hit the correct level of difficulty.

Some ways to cause students to leverage their perspective might be:

* Reading how somebody else solved a similar problem and determining how to use
that code in their own projects.
* Add "scope creep" to projects: Change requirements in mid-assignment, add
requirements, cause students to revise and re-envision their work.
* Have students roleplay QA teams where they actively try to break other students'
apps and then figure out why it broke.
* Have students work on projects as business groups and "try on" all the roles
of the group in order to better understand how various roles contribute as well
as to better think about the software architecture.

Pozmanter mentioned a survey of software developers and things that cause
"unhappiness":

* Getting stuck
* Time pressure
* Bad code quality
* Unclear requirements
* etc.

He advocates that these "unhappy issues" can be used as tools to teach and will also have the
effect of helping students better cope with these issues when they come up
outside the classroom.

Ultimately, the goal is to create a well-rounded developer who is more than _just_
a coder:

* Communication skills
* Strategic Thinking
* Love of Learning
* Outside Interests
* Healthy relationship with failure
* Self confidence

The idea of reproducing unpleasant real-world situations in a course is appealing
to me, too. I feel that we often plan for the best case scenario, while we know
that our students will actually walk into something much more tragic and chaotic.

Scaffolding projects to provide opportunities for these sorts of curve balls can
definitely be a great way to help students make the transition from school to work.
It's tough to imagine how to do this in lower level courses, but this is certainly
something that would help advanced students, and we should consider these approaches
for our advanced groupwork or capstones.

We attempt a form of this team-based education in the
[Professional Practice](http://webdev.seattleu.edu/courses.html) course we run as part of
the Web Dev Certificate at Seattle University. The course runs as, essentially,
a big role-playing game for the first seven weeks, allowing students to inhabit
the roles of a full dev team and work together.

## Sam Redmond&mdash;Breaking Bad Habits: The Usefulness of Style Feedback

Redmond is an undergrad who will graduate in 2018. He has been teaching CS41:
Hap.py Code at Stanford. This is an intro to Python course.

Redmond spoke about giving stylistic feedback. This is a fascinating topic for
me, probably due to my history with teaching writing and art. I've long believed
that accuracy is only half the job: We also aim to make things beautiful. Beauty
is useful.

Key takeaway Redmond wants to convey: Style feedback should help students "think
in Python."

Redmond wants us to move beyond PEP-8 compliance and aim our feedback to help
students not only improve their code, but also improve their understanding. Style
feedback should teach students about the language features and help them
leverage those features more effectively.

It's tough to teach style in Python because Python draws from different paradigms.
This causes confusion. Python also has clear bias and preference from a stylistic
perspective. If we are teaching students who come from other languages, then
it's important to help them navigate between all of these paradigms and
considerations.

Stylistic feedback should help students "stretch their mental habits" to "begin
thinking in another way."

Redmond proposes a stylistic feedback framework:

1. Pythonic Practices - "Thinking in Python"
2. Program Deisgn - Language agnostic considerations of software design
3. Python Mechanics - PEP-8 adherance

Redmond asserts that the most important aspect of the feedback is the Pythonic
Practices. As much as possible, feedback should encourage use of Pythonic
features such as:

* List comprehensions
* Iterables and generators
* Don't reinvent the wheel
* Custom Errors
* Magic methods

In order to address style, feedback should:

1. Identify an area of stylistic weakness in the code
2. Articulate the cause of the weakness clearly to the student
3. Offer actionable advice about how to improve the code
4. Word feedback constructively

Redmond's advice for writing feedback is, "Don't violate the dummy rule." If
you can add the word "dummy" to the end of your feedback and it fits, then your
feedback is probably inappropriate.

We should also take into account the students' level in giving feedback. Prioritize
feedback so that students at a basic level get feedback that helps them understand
big Pythonic concepts. But for advanced students, feedback can focus on more
subtle improvements that build in prior knowledge.

I appreciate Redmond's points, and they are vital to teaching students. The
challenge of providing helpful, accurate feedback is huge, and many teachers
struggle with this part of the job.
