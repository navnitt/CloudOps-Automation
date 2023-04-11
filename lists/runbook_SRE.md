# RunBook Connectors:
 | | | | | | 
 | ---| ---| ---| ---| ---| 
 | [AWS](xRunBook_List.md#AWS) | [ElasticSearch](xRunBook_List.md#ElasticSearch) | [Jenkins](xRunBook_List.md#Jenkins) | [Kubernetes](xRunBook_List.md#Kubernetes) | [Postgresql](xRunBook_List.md#Postgresql) | 

 
# RunBook Categories:
 | | | | | | | | | 
 | ---| ---| ---| ---| ---| ---| ---| ---| 
 | [IAM](runbook_IAM.md) | [SECOPS](runbook_SECOPS.md) | [CLOUDOPS](runbook_CLOUDOPS.md) | [DEVOPS](runbook_DEVOPS.md) | [SRE](runbook_SRE.md) | [COST_OPT](runbook_COST_OPT.md) | [TROUBLESHOOTING](runbook_TROUBLESHOOTING.md) | [ES](runbook_ES.md) | 

 # Runbooks in SRE
* AWS [Copy AMI to All Given AWS Regions](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Copy_ami_to_all_given_AWS_regions.ipynb): This runbook can be used to copy AMI from one region to multiple AWS regions using unSkript legos with AWS CLI commands.We can get all the available regions by using AWS CLI Commands.
* AWS [Delete Unattached AWS EBS Volumes](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Delete_Unattached_EBS_Volume.ipynb): This runbook can be used to delete all unattached EBS Volumes within an AWS region. You can delete an Amazon EBS volume that you no longer need. After deletion, its data is gone and the volume can't be attached to any instance. So before deletion, you can store a snapshot of the volume, which you can use to re-create the volume later.
* AWS [Detach EC2 Instance from ASG](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Detach_Instance_from_ASG.ipynb): This runbook can be used to detach an instance from Auto Scaling Group. You can remove (detach) an instance that is in the Service state from an Auto Scaling group. After the instance is detached, you can manage it independently from the rest of the Auto Scaling group. By detaching an instance, you can move an instance out of one Auto Scaling group and attach it to a different group. For more information, see Attach EC2 instances to your Auto Scaling group.
* AWS [Detach EC2 Instance from ASG and Load balancer](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Detach_ec2_Instance_from_ASG.ipynb): This runbook can be used to detach an instance from Auto Scaling Group and Load Balancer. You can remove (detach) an instance that is in the InService state from an Auto Scaling group. After the instance is detached, you can manage it independently from the rest of the Auto Scaling group. By detaching an instance, you can move an instance out of one Auto Scaling group and attach it to a different group. For more information, see Attach EC2 instances to your Auto Scaling group.
* AWS [Detect ECS failed deployment](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Detect_ECS_failed_deployment.ipynb): This runbook check if there is a failed deployment in progress for a service in an ECS cluster. If it finds one, it sends the list of stopped task associated with this deployment and their stopped reason to slack.
* AWS [AWS EC2 Disk Cleanup](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/EC2_Disk_Cleanup.ipynb): This runbook locates large files in an EC2 instance and backs them up into a given S3 bucket. Afterwards, it deletes the files backed up and send a message on a specified Slack channel. It uses SSH and linux commands to perform the functions it needs.
* AWS [Enforce Mandatory Tags Across All AWS Resources](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Enforce_Mandatory_Tags_Across_All_AWS_Resources.ipynb): This runbook can be used to Enforce Mandatory Tags Across All AWS Resources.We can get all the  untag resources of the given region,discovers tag keys of the given region and attaches mandatory tags to all the untagged resource.
* AWS [Handle AWS EC2 Instance Scheduled to retire](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Find_EC2_Instances_Scheduled_to_retire.ipynb): To avoid unexpected interruptions, it's a good practice to check to see if there are any EC2 instances scheduled to retire. This runbook can be used to List the EC2 instances that are scheduled to retire. To handle the instance retirement, user can stop and restart it before the retirement date. That action moves the instance over to a more stable host.
* AWS [Get unhealthy EC2 instances from ELB](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Get_Aws_Elb_Unhealthy_Instances.ipynb): This runbook can be used to list unhealthy EC2 instance from an ELB. Sometimes it difficult to determine why Amazon EC2 Auto Scaling didn't terminate an unhealthy instance from Activity History alone. You can find further details about an unhealthy instance's state, and how to terminate that instance, by checking the a few extra things.
* AWS [Monitor AWS DynamoDB provision capacity](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Monitor_AWS_DynamoDB_provision_capacity.ipynb): This runbook can be used to collect the data from cloudwatch related to AWS DynamoDB for provision capacity.
* AWS [List unused Amazon EC2 key pairs](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Notify_about_unused_keypairs.ipynb): This runbook finds all EC2 key pairs that are not used by an EC2 instance and notifies a slack channel about them. Optionally it can delete the key pairs based on user configuration.
* AWS [Resize EBS Volume](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Resize_EBS_Volume.ipynb): This run resizes the EBS volume to a specified amount. This runbook can be attached to Disk usage related Cloudwatch alarms to do the appropriate resizing. It also extends the filesystem to use the new volume size.
* AWS [Resize list of pvcs.](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Resize_List_Of_Pvcs.ipynb): This runbook can be used to resize list of pvcs in a namespace. By default, it uses all pvcs to be resized.
* AWS [Resize PVC](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Resize_PVC.ipynb): This runbook resizes the PVC to input size.
* AWS [Restart AWS EC2 Instances](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Restart_AWS_EC2_Instances_By_Tag.ipynb): This runbook can be used to Restart AWS EC2 Instances
* AWS [Restart AWS Instances with a given tag](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Restart_Aws_Instance_given_Tag.ipynb): This runbook will discover all AWS EC2 instances matching a tag and then restart them. It will notify status through slack after its done. There is also a dry run mode that will just display the instances that match the query.
* AWS [Restart unhealthy services in a Target Group](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Restart_Unhealthy_Services_Target_Group.ipynb): This runbook restarts unhealthy services in a target group. The restart command is provided via a tag attached to the instance.
* AWS [Launch AWS EC2 from AMI](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Run_EC2_from_AMI.ipynb): This lego can be used to launch an AWS EC2 instance from AMI in the given region.
* AWS [Troubleshooting Your EC2 Configuration in a Private Subnet](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Troubleshooting_Your_EC2_Configuration_in_Private_Subnet.ipynb): This runbook can be used to troubleshoot EC2 instance configuration in a private subnet by capturing the VPC ID for a given instance ID. Using VPC ID to get Internet Gateway details then try to SSH and connect to internet.
* Jenkins [Fetch Jenkins Build Logs](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Jenkins/Fetch_Jenkins_Build_Logs.ipynb): This runbook fetches the logs for a given Jenkins job and posts to a slack channel
* Kubernetes [k8s: Delete Evicted Pods From All Namespaces](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/Delete_Evicted_Pods_From_Namespaces.ipynb): This runbook shows and deletes the evicted pods for given namespace. If the user provides the namespace input, then it only collects pods for the given namespace; otherwise, it will select all pods from all the namespaces.
* Kubernetes [k8s: Get kube system config map](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/Get_Kube_System_Config_Map.ipynb): This runbook fetches the kube system config map for a k8s cluster and publishes the information on a Slack channel.
* Kubernetes [k8s: Get candidate nodes for given configuration](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/K8S_Get_Candidate_Nodes_Given_Config.ipynb): This runbook get the matching nodes for a given configuration (storage, cpu, memory, pod_limit) from a k8s cluster
* Kubernetes [Kubernetes Log Healthcheck](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/K8S_Log_Healthcheck.ipynb): This RunBook checks the logs of every pod in a namespace for warning messages.
* Kubernetes [k8s: Pod Stuck in CrashLoopBackoff State](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/K8S_Pod_Stuck_In_CrashLoopBack_State.ipynb): This runbook checks if any Pod(s) in CrashLoopBackoff state in a given k8s namespace. If it finds, it tries to find out the reason why the Pod(s) is in that state.
* Kubernetes [k8s: Pod Stuck in ImagePullBackOff State](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/K8S_Pod_Stuck_In_ImagePullBackOff_State.ipynb): This runbook checks if any Pod(s) in ImagePullBackOff state in a given k8s namespace. If it finds, it tries to find out the reason why the Pod(s) is in that state.
* Kubernetes [k8s: Pod Stuck in Terminating State](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/K8S_Pod_Stuck_In_Terminating_State.ipynb): This runbook checks any Pods are in terminating state in a given k8s namespace. If it finds, it tries to recover it by resetting finalizers of the pod.
* Kubernetes [k8s: Resize List of PVCs](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/Resize_List_of_PVCs.ipynb): This runbook resizes a list of Kubernetes PVCs.
* Kubernetes [k8s: Resize PVC](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/Resize_PVC.ipynb): This runbook resizes a Kubernetes PVC.
* Kubernetes [Rollback Kubernetes Deployment](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/Rollback_k8s_Deployment_and_Update_Jira.ipynb): This runbook can be used to rollback Kubernetes Deployment
* Postgresql [Display long running queries in a PostgreSQL database](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Postgresql/Display_Postgresql_Long_Running.ipynb): This runbook displays collects the long running queries from a database and sends a message to the specified slack channel. Poorly optimized queries and excessive connections can cause problems in PostgreSQL, impacting upstream services.