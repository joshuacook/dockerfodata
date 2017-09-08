Title: Configuring the `jupyter/scipy-notebook` Image with the `nbgrader` Extension
Date: 2017-09-04 13:00
Modified: 2017-09-04 13:00
Category: jupyter/scipy-notebook
Tags: teaching, extensions
Slug: configure_scipy_notebook_for_nbgrader
Authors: Joshua Cook
Summary: On setting up the default `jupyter/scipy-notebook` image for use with the `nbgrader` extension.

I am very keen on using the [`nbgrader`](https://nbgrader.readthedocs.io/en/stable/index.html)
extension for Jupyter Notebooks in my classes during this next session.
I am hopeful that the tool will bring some level of automation to the feedback process in my class. Feedback is
something with which I continually struggle and hopefully this tool will help me to be more responsive
in providing feedback around student work.

Being wholly invested in running Jupyter from with Docker, I will of course need to define a `Dockerfile` that
will install and configure the extension. The [`nbgrader` documentation](https://nbgrader.readthedocs.io/en/stable/user_guide/installation.html)
recommends the following practice for installing the tool:

```bash
conda install -c conda-forge nbgrader
jupyter nbextension install --sys-prefix --py nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader
```

We will begin by adding these commands as additional layers to the base `jupyter/scipy-notebook` image

```bash
FROM jupyter/scipy-notebook
RUN conda install -c conda-forge nbgrader
RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader
```

I build the image using the standard `docker build` command from
within the same directory as the `Dockerfile`.

```bash
$ docker build -t nbgrader .
```

I ran the quickstart tool using this command

```bash
$ docker run -v `pwd`:/home/jovyan -p 8890:8888 nbgrader nbgrader quickstart dsiplus2
```

