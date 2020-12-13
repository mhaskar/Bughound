# What is Bughound

Bughound is an open-source static code analysis tool that analyzes your code and sends the results to Elasticsearch and Kibana to get useful insights about the potential vulnerabilities in your code.

Bughound has its own Elasticsearch and Kibana Docker container that is preconfigured with dashboards to give you a strong visualization for the findings.

You can detect various types of vulnerabilities such as:
* Command Injection.
* XXE.
* Unsafe Deserialization.
* And more! 

Bughound can analyze `php` and `java` code for now, and it contains the most unsafe functions for these languages.


***Please note that Bughound results are not 100% accurate, it built to help you identify potential weaknesses during your analysis*** 

# How it works?

First of all, Bughound will get all the files inside your project based on the extension of the files you want to audit and then, it will read each file and try to find any pre-defined unsafe functions for your project's language, and finally, it will send the results to Bughound docker container which has a pre-configured Elasticsearch and Kibana that contain the customaized dashboards for your findings.

The dashboards will give you detials about the findings such:
* Function name.
* Category of the vulnerability.
* Line number.
* And much more! 

Also using Kibana, you will be able to view the potential vulnerable code snippet and start do your analysis and tracing phase to check if it's exploitable or not.

Of course you can use your own ELK stack if you want and Bughound will do the initial configuration for you, but you will not have the pre-configured dashboards in this case.
