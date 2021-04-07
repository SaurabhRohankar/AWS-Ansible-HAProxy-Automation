# haproxy_on_aws_ansible
Automating setup of load balancer (HAProxy) on AWS using ansible playbooks

Configure the folowing setup over AWS using instance over there.

Use Ansible playbook to Configure Reverse Proxy i.e. Haproxy and update it's configuration 
file automatically on each time new Managed node (Configured With Apache Webserver) join the inventory.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 1) Launching 3 instances over aws using ansible playbook
webservers :- 2 instances
load balancer:- 1 instance


Step 2) Configuring webservers in 2 instances
To launch instance we will use dynamic inventory and you need to setup environment varibles for access and secret key.


Step 3) Retrieving webserver's IPs and adding it to haproxy config file dynamically 
We will use jinja templates for doing this


Step 4) Configuring HAProxy in one instance

