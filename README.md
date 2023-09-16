# HAProxy on AWS Infrastructure Automation using Ansible

This project showcases the power of Ansible for automating AWS infrastructure provisioning, configuring HAProxy for reverse proxy functionality, and managing Apache web servers. It leverages Ansible's capabilities for infrastructure automation and orchestration.

## Project Overview

The project achieves the following objectives:

1. **AWS EC2 Instance Provisioning**:
   - Launches AWS EC2 instances for a load balancer (HAProxy) and backend web servers.
   - Utilizes Ansible's `ec2` module for dynamic instance provisioning.

2. **Passwordless Authentication**:
   - Establishes passwordless authentication between the Ansible control node and EC2 instances for enhanced security and automation. (See [Setup Passwordless Authentication](#setup-passwordless-authentication))

3. **HAProxy Configuration**:
   - Configures HAProxy on the load balancer instance to provide reverse proxy functionality.
   - Automates the process of updating the HAProxy configuration whenever new managed nodes (Apache web servers) are added to the inventory.

4. **Backend Web Server Configuration**:
   - Configures Apache (`httpd`) on the backend web servers.
   - Copies a sample HTML page with dynamic content to differentiate between servers.
   
## Project Structure

The project is organized into the following components:

- `instance.yml`: Ansible playbook for provisioning EC2 instances.
- `webserver.yml`: Ansible playbook for configuring Apache web servers.
- `haproxy.cfg`: Template file for HAProxy configuration.
- Other Ansible inventory and configuration files as needed.

## Getting Started

To use this project, follow these steps:

1. **Prerequisites**:
   - Install Ansible on your control node.
   - Configure AWS CLI with access and secret keys.

2. **Setup Passwordless Authentication**:
   - Before running playbooks, set up passwordless authentication by copying the master node's public key into worker nodes. (See [Setup Passwordless Authentication](#setup-passwordless-authentication))

3. **AWS EC2 Instances**:
   - Customize `instance.yml` to match your AWS settings.
   - Run the playbook to provision EC2 instances: `ansible-playbook -i aws_ec2.yml instance.yml`.

4. **Web Servers**:
   - Customize `webserver.yml` as needed.
   - Run the playbook to configure Apache web servers: `ansible-playbook -i aws_ec2.yml webserver.yml`.

5. **HAProxy**:
   - Customize `haproxy.cfg` to define HAProxy configuration rules.
   - Run the playbook to configure HAProxy.

6. **Access Web Application**:
   - Access the web application via the load balancer's public IP or DNS.

## Setup Passwordless Authentication

Before running any playbooks, set up passwordless authentication between the Ansible control node (master) and the EC2 instances (worker nodes). Follow these steps:

1. **Generate SSH Key Pair**:
   - On the Ansible control node, generate an SSH key pair using `ssh-keygen`. Keep the default location for the keys.

   ```bash
   ssh-keygen -t rsa -b 2048
   ```

2. **Copy the Public Key**:
   - Copy the public key to the worker nodes using Ansible's `authorized_key` module or manually. Replace `USER` with the appropriate SSH user and `WORKER_IP` with the IP address of each worker node.

   ```bash
   ansible -i aws_ec2.yml all -m authorized_key -a "user=USER key=$(cat ~/.ssh/id_rsa.pub)" --private-key=/path/to/your/key.pem
   ```

   - Or, manually copy the public key to `~/.ssh/authorized_keys` on each worker node.

3. **Test SSH Access**:
   - Verify that passwordless authentication works by SSHing into the worker nodes without a password:

   ```bash
   ssh -i /path/to/your/key.pem USER@WORKER_IP
   ```

   You should be able to log in without being prompted for a password.

## Contributing

Contributions to this project are welcome. If you find issues or have enhancements, please open a GitHub issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Ansible](https://www.ansible.com/) for automation capabilities.
- [AWS](https://aws.amazon.com/) for cloud infrastructure.
- [HAProxy](http://www.haproxy.org/) for load balancing.

## Author

Saurabh Rohankar

[GitHub Profile](https://github.com/SaurabhRohankar)
