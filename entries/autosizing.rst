Autosizing web services
#######################

:date: 2017-10-06
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


Molotov, the load testing tool I've developed, comes now with an **autosizing**
feature. When the **--sizing** option is used, Molotov will slowly ramp-up the
number of workers per process and will stop once there are too many failures
per minute.

The default tolerance for failure is 5%, but this can be tweaked with the
**--sizing-tolerance** option.

Molotov will use 500 workers that are getting ramped up in 5 minutes, but you
can set your own values with **--workers** and **--ramp-up** if you want to
autosize at a different pace.

See all the options at http://molotov.readthedocs.io/en/stable/cli

This load testing technique is useful to determine what is the limiting
resource for a given application: RAM, CPU, I/O or Network.

Running Molotov against a single node that way can help decide what is the best
combination of RAM, CPU, Disk and Bandwidth per node to deploy a project. In
AWS that would mean helping chosing the size of the VM.

To perform this test you need to deploy the app on a dedicated node. Since most
of our web services projects at Mozilla are now available as Docker images, it
becomes easy to automate that deployment when we want to test the service.

I have created a small script on the top of Molotov that does exactly that, by
using Amazon SSM (Systems Manager). See
http://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html

Amazon SSM
----------

SSM is a client-server tool that simplifies working with EC2 nodes. For
instance, instead of writing a low-level script using Paramiko that drives EC2
instances through SSH, you can send batch commands through SSM to any number of
EC2 instances, and get back the results asynchronously.

SSM integrates with S3 so you can get back your commands results as artifacts
once they are finished.

Building a client around SSM is quite easy with Boto3. The only tricky part is
waiting for the results to be ready.

This is my SSM client:
https://github.com/tarekziade/sizer/blob/master/sizer/ssm.py


Deploying and running
---------------------


Based on this SSM client, my script is doing the following operations on AWS:

- Deploy (or reuse) an EC2 Instance that has an SSM agent and a Docker agent
  running
- Run the Docker container of the service on that EC2 instance
- Run a Docker container that runs **Glances** (more on this later)

Once the EC2 instance has the service up and running, it's ready to be used via
Molotov.

The script takes a github repo and run it, using **moloslave**
http://molotov.readthedocs.io/en/stable/slave Once the test is over, metrics
are grabbed via SSM and the results are presented in a fancy HTML 5 page where
you can find out what is the bottleneck of your service

Example with Kinto
------------------

Kinto is a Python service that provides a rest-ish API to read write schemaless
JSON documents. Running a load test on it using Molotov is pretty
straightforward. The test script adds data, browses it and verifies that the
Kinto service returns things correctly. And Kinto has a docker image published
on Docker hub.

I've run the sizing script using that image on a t2.micro instance. Here are
the results: https://ziade.org/sizer_tested.html

You can see that the memory is growing throughout the test, because the Docker
image uses a memory database and the test keeps on adding data -- that is also
why the I/O is sticking to 0.

If you double-click on the CPU metrics, you can see that the CPU reaches almost
100% at the end of the test before things starts to break.

So, for a memory backend, the limiting factor for Kinto is the CPU, which makes
sense. If we had had a bottleneck on I/O, that would have been an indication
that something was wrong.

Another interesting test would be to run it against a Postgres RDS deployment
instead of a memory database.

Collecting Metrics with Glances
-------------------------------

The metrics are collected on the EC2 box using Glances
(http://glances.readthedocs.io/) which runs in its own Docker container and has
the ability to measure **other docker images** running on the same agent. see
http://glances.readthedocs.io/en/stable/aoa/docker.html?highlight=docker

In other words, you can follow the resource usage *per docker container*, and
in our case that's useful to track the container that runs the actual service.

My Glances docker container uses this image:
https://github.com/tarekziade/sizer/blob/master/Dockerfile which runs the tool
and spits out the metrics in a CSV file I can collect via SSM once the test is
over.


Vizualizing results
-------------------

I could have send the metrics to an Influxdb or Grafana system, but I wanted to
create a simple static page that could work locally and be passed around as a
test artifact.

That's where Plotly (https://plot.ly/) comes in handy. This tool can turn a CSV
file produced by Glances into a nice looking HTML5 page where you can toggle
between metrics and do other nice stuff.

I have used Pandas/Numpy to process the data, which is probably overkill given
the amount of processed lines, but their API are a natural fit to work with
Plotly.

See the small class I've built here:
https://github.com/tarekziade/sizer/blob/master/sizer/chart.py


Conclusion
----------

The new Molotov sizing feature is pretty handy as long as you can automate the
deployment of isolated nodes for the service you want to test -- and that's
quite easy with Docker and AWS.

Autosizing can give you a hint on how an application behaves under stress and
help you decide how you want to initially deploy it.

In an ideal world, each one of our services has a Molotov test already, and
running an autosizing test can be done with minimal work.

In a super ideal world, everything I've described is part of the continuous
deployement process :)



