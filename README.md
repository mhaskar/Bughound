![Stability](https://img.shields.io/badge/Stability-Beta-yellowgreen) ![Version](https://img.shields.io/badge/Version-Beta-brightgreen) ![Python](https://img.shields.io/badge/Python-3-blue)
![Docker Pulls](https://img.shields.io/docker/pulls/bughound/bughound)

# What is Bughound?

Bughound is an open-source static code analysis tool that analyzes your code and sends the results to Elasticsearch and Kibana to get useful insights about the potential vulnerabilities in your code.

Bughound has its own Elasticsearch and Kibana Docker image that is preconfigured with dashboards to give you a strong visualization for the findings.

You can detect various types of vulnerabilities such as:
* Command Injection.
* XXE.
* Unsafe Deserialization.
* And more!

Bughound can analyze `PHP` and `JAVA` code for now, and it contains a group of unsafe functions for these languages.

I will make sure to add more and more functions/languages coverage with time, but for now the main focus is for the project stability itself.


***Please note that Bughound results are not 100% accurate, it built to help you identify potential weaknesses during your analysis to investigate.***



# How it works?

First of all, Bughound will build a list of all the files inside your project based on the extension of the files you want to audit, then it will read each file and try to find any pre-defined unsafe functions for your project's language.

The analysis phase depends on pre-configured regex and some custom text matching to detect the potential vulnerabilities, so again, you need to do the manual analysis so you can check if these findings are exploitable.

Finally, it will send the results to the Bughound docker image which has a pre-configured Elasticsearch and Kibana that contain the customized dashboards for your findings.

The dashboards will give you details about the findings such:
* Function name.
* Category of the vulnerability.
* Line number.
* And much more!

Also using Kibana, you will be able to view the potentially vulnerable code snippet to start doing your analysis and tracing phase to check if it's exploitable or not.

Of course, you can use your own ELK stack if you want, and Bughound will do the initial configuration for you, but you will not have the pre-configured dashboards in this case.


# Requirements

You can install all the requirements to run Bughound code using the following command:

`pip3 install -r requirements.txt`

That will make sure all the requirements are installed for the code.

Also, you need to [install Docker](https://docs.docker.com/engine/install/) in order to run the Bughound image, more regarding this in the next section!

**If you want to use your own Elasticsearch and Kibana instances, skip the docker installation step**



# Installation

Make sure to get the latest version of Bughound using the following command:

`git clone https://github.com/mhaskar/Bughound`

And after installing the requirements in the previous step you can run Bughound using the following command:

`./Bughound.py`

You will get the main screen of Bughound.

```
┌─[✗]─[askar@hackbook]─[/opt/bughound]
└──╼ $./bughound.py

.______    __    __    _______  __    __    ______    __    __  .__   __.  _______
|   _  \  |  |  |  |  /  _____||  |  |  |  /  __  \  |  |  |  | |  \ |  | |       \
|  |_)  | |  |  |  | |  |  __  |  |__|  | |  |  |  | |  |  |  | |   \|  | |  .--.  |
|   _  <  |  |  |  | |  | |_ | |   __   | |  |  |  | |  |  |  | |  . `  | |  |  |  |
|  |_)  | |  `--'  | |  |__| | |  |  |  | |  `--'  | |  `--'  | |  |\   | |  '--'  |
|______/   \______/   \______| |__|  |__|  \______/   \______/  |__| \__| |_______/



          \ /
          oVo
      \___XXX___/
       __XXXXX__
      /__XXXXX__\
      /   XXX   \
           V                  V1.0 Beta

usage: bughound.py [-h] [--path PATH] [--git GIT_REPO] --language
                   LANGUAGE --extension EXTENSION --name NAME
bughound.py: error: argument --language is required
┌─[✗]─[askar@hackbook]─[/opt/bughound]
└──╼ $

```

### Docker image installation

To install the Bughound docker image, you can simply do the following:

`docker pull bughound/bughound`

And that will pull the latest version of the image and save it to your machine.

Once we pulled the image, we can run it using the following command:

`docker run --name bughound -p5601:5601 -p 9200:9200 bughound/bughound`

That will run the image under a new container called `bughound` and expose the ports that are needed by Bughound to communicate Elasticsearch and Kibana to your host.

After getting two things done, you are ready now to use Bughound!

# Preconfigured Dashboards

If you decided to use the official Bughound docker image, you will get a couple of ready to use dashboards that will help you to do your analysis.

The following dashboards are available so far:
* Bughound main dashboard
* Command injection dashboard
* Deserialization dashboard
* XXE dashboard

These dashboards will give you statistics about the functions and code snippets that was found in the code so you can start your tracing process.

# Usage

To start the analysis process for your code, you should use `Bughound.py` file which has some options, to see these options via the help banner, you can use the following command:

```
┌─[✗]─[askar@hackbook]─[/opt/bughound]
└──╼ $./bughound.py -h

.______    __    __    _______  __    __    ______    __    __  .__   __.  _______
|   _  \  |  |  |  |  /  _____||  |  |  |  /  __  \  |  |  |  | |  \ |  | |       \
|  |_)  | |  |  |  | |  |  __  |  |__|  | |  |  |  | |  |  |  | |   \|  | |  .--.  |
|   _  <  |  |  |  | |  | |_ | |   __   | |  |  |  | |  |  |  | |  . `  | |  |  |  |
|  |_)  | |  `--'  | |  |__| | |  |  |  | |  `--'  | |  `--'  | |  |\   | |  '--'  |
|______/   \______/   \______| |__|  |__|  \______/   \______/  |__| \__| |_______/



          \ /
          oVo
      \___XXX___/
       __XXXXX__
      /__XXXXX__\
      /   XXX   \
           V                  V1.0 Beta

usage: bughound.py [-h] [--path PATH] [--git GIT] --language LANGUAGE
                   --extension EXTENSION --name NAME

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           local path of the source code
  --git GIT             git repository URL
  --language LANGUAGE   the used programming language
  --extension EXTENSION
                        extension to search for
  --name NAME           project name to use
┌─[askar@hackbook]─[/opt/bughound]
└──╼ $
```
