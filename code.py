import os
import getpass
import pyttsx3 as p
import webbrowser as wb

engine = p.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate
#"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print()
print("welcome to my menu !!!".center(125))
print("----------------------".center(125))
p.speak("welcome to my menu !!!")

p.speak("enter your password")
print()
passwd = getpass.getpass("Enter your Password : ".center(125))

if passwd != "integration":
  print("password incorrect ...")
  exit()

print()

p.speak("enter yes to continue")
r = input("Enter yes to Continue : ".center(125))

print("""
  \n
  Press 1  : to create key-pair. 
  Press 2  : to create Secutiy Group.
  Press 3  : to create EC-2 Instances.
  Press 4  : to create s3 Bucket and Put objects into it.
  Press 5  : to create Cloud Front Distribution
  Press 6  : to copy hadoop and jdk software to EC-2 Instances.
  Press 7  : to setup and configure namenode and datanode on the top of EC-2 Instances.
  Press 8  : to create two EBS Volumes and mount them to Datanode EC-2 Instance.
  Press 9  : to create LVM Partition.
  Press 10 : to start hadoop Cluster.
  Press 11 : to increase Datanode Storage on the fly.
  Press 12 : to configure docker on the top of EC-2 Instance.
  Press 13 : to pull CentOS Image and Run Centos Container.
  Press 14 : to configure webserver on the top of Centos Container which is running on the top of AWS Cloud. 
  Press 15 : to setup Python Interpreter on the top of EC-2 Instance.
  Press 16 : to run Salary Predictor Code on the top of EC-2 Instance.
  Press 17 : to configure Ansible on the top of EC-2 Instance.
  Press 18 : to setup gedit , httpd , mysql ,and tcpdump  using Ansible on the top of EC-2 Instance.
  Press 19 : to show the network configuration of your EC-2 Instance.
  Press 20 : to exit.
  """.center(125))
#p.speak("on press one i will create key pair , on press two i will create Security Group  , on press three i will create ec2 instances , on press four i will create key s3 bucket and put objects into it , on press five i will create cloud front distribution , on press six i will copy hadoop and jdk software to ec2 instances , on press seven i will setup and configure namenode and datanode on the top of ec2 instances , on press eight i will create two EBS volumes and mount them to datanode EC-2 instance , on press nine i will create LVM partition , on press ten i will start hadoop cluster , on press eleven i will increase datanode storage on the fly , on press twelve i will configure docker on the top of EC-2 Instance , on press thirteen i will pull centos image and run centos container , on press fourteen i will configure webserver on the top of Centos Container which is running on the top of AWS Cloud , on press fifteen i will setup Python Interpreter on the top of EC-2 Instance , on press sixteen i will run Salary Predictor Code on the top of EC-2 Instance , on press seventeen i will configure Ansible on the top of EC-2 Instance , on press eighteen i will setup gedit , httpd , mysql , and tcpdump using Ansible on the top of EC-2 Instance ,on press nineteen i will show network configurations and on press twenty i will exit the program .. now you can proceed further thankyou...!!!")
input()

while True:
  os.system("cls")
  print("""
  \n
  Press 1  : to create key-pair. 
  Press 2  : to create Security group.
  Press 3  : to create EC-2 Instances.
  Press 4  : to create s3 Bucket and Put objects into it.
  Press 5  : to create Cloud Front Distribution.
  Press 6  : to copy hadoop and jdk software to EC-2 Instances.
  Press 7  : to setup and configure namenode and datanode on the top of EC-2 Instances.
  Press 8  : to create two EBS Volumes and mount them to Datanode EC2-Instance.
  Press 9  : to create LVM Partition.
  Press 10 : to start hadoop Cluster.
  Press 11 : to increase Datanode Storage on the fly.
  Press 12 : to configure docker on the top of EC-2 Instance.
  Press 13 : to pull CentOS Image and Run Centos Container.
  Press 14 : to configure webserver on the top of Centos Container which is running on the top of AWS Cloud. 
  Press 15 : to setup Python Interpreter on the top of EC-2 Instance.
  Press 16 : to run Salary Predictor Code on the top of EC-2 Instance.
  Press 17 : to configure Ansible on the top of EC-2 Instance.
  Press 18 : to setup gedit , httpd , mysql , and tcpdump using Ansible on the top of EC-2 Instance.
  Press 19 : to show the network configuration of your EC-2 Instance.
  Press 20 : to exit.
  """)


  choice = input(" Enter Your Choice : ")
  print()
  
  
  if r == "yes":
    
    if int(choice) == 1:
      p.speak("Enter Key name")
      kn = input("Enter Key Name : ")
      os.system("aws ec2 create-key-pair --key-name {}".format(kn))
      p.speak("Key Pair is Successfully Created")
    elif int(choice) == 2:
      p.speak("Enter Security Group Name")
      sg = input("Enter Security Group Name : ")
      os.system("aws ec2 create-security-group --group-name {}  --description my-group".format(sg))
      os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol all --port all --cidr 0.0.0.0/0".format(sg))
      p.speak("Security Group is Successfully Created")
    elif int(choice) == 3:
      p.speak("Enter Security Group id")
      sg = input("Enter Security Group id : ")
      os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --count 2 --instance-type t2.micro --key-name {} --security-group-ids {} --subnet-id subnet-43073d2b".format(kn,sg))
      p.speak("ec2 instances are successfully provisioned")
    elif int(choice) == 4:
      p.speak(" \n Enter Bucket Name")
      bn = input("Enter Bucket Name : ")
      os.system(" \n aws s3 mb s3://{}".format(bn))
      os.system(" \n aws s3 cp pic1.gif s3://{} --acl public-read".format(bn))
      os.system(" \n aws s3 cp pic2.jpg s3://{} --acl public-read".format(bn))
      p.speak("s3 Bucket created successfully and object are uploaded")
    elif int(choice) == 5:
      os.system(" \n aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object pic1.gif".format(bn))
      os.system(" \n aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object pic2.jpg".format(bn))
      p.speak("Cloud front Distribution created successfully")
      input()
      p.speak("Enter First CloudFront Domain Name")   
      url1 = input("Enter First CloudFront Domain Name : ")
      wb.open("{}".format(url1))
      input()
      p.speak("Enter Second CloudFront Domain Name")   
      url2 = input("Enter Second CloudFront Domain Name : ")
      wb.open("{}".format(url2))
    elif int(choice) == 6:
      p.speak("Enter namenode ip")
      ip1 = input("Enter Namenode IP : ")
      os.system("scp hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm root@{}:".format(ip1))
      print()
      p.speak("Enter datanode ip")
      ip2 = input("Enter Datenode IP : ")
      os.system("scp hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm root@{}:".format(ip2))
      p.speak("Packages are successfully Copied")
    elif int(choice) == 7:
      os.system("ssh root@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm --force".format(ip1))
      p.speak("enter namenode directory")
      nn = input("Enter Namenode Directory : ")
      os.system("ssh root@{} mkdir /{} ; yum install git -y ; git clone https://github.com/aaditya2801/bash-script.git".format(ip1,nn))
      p.speak("enter shell script for namenode")
      bs = input("Enter Shell Script : ")
      os.system("ssh root@{} source bash-script/{} ; hadoop namenode -format".format(ip1,bs))
      print()
      os.system("ssh root@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm --force".format(ip2))
      p.speak("enter datanode directory")
      nn = input("Enter Datanode Directory : ")
      os.system("ssh root@{} mkdir /{} ; yum install git -y ; git clone https://github.com/aaditya2801/bash-script.git".format(ip2,nn))
      p.speak("enter Shell script for datanode")
      bs = input("Enter shell Script : ")
      os.system("ssh root@{} source bash-script/{}".format(ip2,bs))
      p.speak("setup and configure of namenode and datanode on the top of EC-2 Instances are done")
    elif int(choice) == 8:
      os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
      os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
      p.speak("volumes are successfully created")
      p.speak("Enter Datanode instance id : ")
      id = input("Enter Datanode Instance id : ")
      p.speak("Enter First Volume id")
      volid1 = input("Enter First Volume id : ")
      os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid1,id))
      p.speak("Enter Second Volume id")
      volid2 = input("Enter Second Volume id : ")
      os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdj".format(volid2,id))
      p.speak("Volumes are successfully attached to the datanode instance")
    elif int(choice) == 9:
      os.system("ssh root@{} fdisk -l".format(ip2))
      p.speak("These are the drives present in datanode instance")
      input()
      p.speak("Enter first Drive Name")
      print()
      dn1 = input("Enter First Drive Name : ")
      p.speak("Enter second Drive Name")
      print()
      dn2 = input("Enter Second Drive Name : ")
      os.system("ssh root@{} pvcreate {} ; pvcreate {} ; pvdisplay".format(ip2,dn1,dn2))
      p.speak("Physical volumes are created successfully")
      input()
      p.speak("enter volume group name")
      print()
      gn = input("Enter Group Name : ")
      print()
      pv1 = input("Enter First PV Name : ")
      p.speak("Enter second PV Name")
      print()
      pv2 = input("Enter Second Drive Name : ")
      os.system("ssh root@{} vgcreate {} {} {} ; vgdisplay {}".format(ip2,gn,pv1,pv2,gn))
      p.speak("volume group is successfully created")
      input()
      p.speak("enter size of partition")
      print()
      sz = input("Enter Size of Partition : ")
      print()
      p.speak("enter logical partition name")
      print()
      lp = input("Enter Logical Partition Name : ")
      print()
      os.system("ssh root@{} lvcreate --size {}G --name {} {} ; lvdisplay {}/{} ; mkfs.ext4 /dev/{}/{}".format(ip2,sz,lp,gn,gn,lp,gn,lp))
      p.speak("partition is successfully created")
      print()
      p.speak("enter mount point name")
      print()
      mp = input("Enter Mount Point Name : ")
      print()
      os.system("ssh root@{} mount /dev/{}/{} /{} ; df -h ".format(ip2,gn,lp,mp))
      p.speak("Partition is successfully mounted on datanode directory")
    elif int(choice) == 10:
      os.system("ssh root@{} hadoop-daemon.sh start namenode".format(ip1))
      p.speak("namenode started")
      print()
      os.system("ssh root@{} hadoop-daemon.sh start datanode ; hadoop dfsadmin -report".format(ip2))
      p.speak("datanode started and providing limited storage to the cluster")
    elif int(choice) == 11:
      p.speak("enter incremental size of datanode storage in MB")
      print()
      sz = input("Enter Incremental size of Datanode Storage in MB : ")
      print()
      os.system("ssh root@{} lvextend --size +{}M /dev/{}/{} ; resize2fs /dev/{}/{} ; hadoop dfsadmin -report".format(ip2,sz,gn,lp,gn,lp))
      p.speak("storage extended")
    elif int(choice) == 12:
      p.speak("Enter Instance IP where you want to configure docker")
      ip = input("Enter Instance IP : ")
      os.system("ssh root@{} amazon-linux-extras install docker -y ; systemctl start docker ; systemctl status docker".format(ip))
      p.speak("docker is successfully configured")
    elif int(choice) == 13:
      p.speak("Enter Image name")
      print()
      img = input("Enter Image Name : ")
      p.speak("Enter Container name")
      cnt = input("Enter Container Name : ")
      os.system("ssh root@{} docker pull {} ; docker images ; docker run -dit -p 8080:80 --name {} centos ; docker ps".format(ip,img,cnt))
      p.speak("CentOS Image is successfully pulled and Centos Container is also running")
    elif int(choice) == 14:
      os.system("ssh root@{}".format(ip))
      p.speak("webserver is successfully configured and webpage is deploying")
      wb.open("{}:8080".format(ip))
    elif int(choice) == 15:
      os.system("ssh root@{} yum install python3 -y ; rpm -q python3".format(ip))
      p.speak("python interpreter setup is done")
    elif int(choice) == 16:
      p.speak("Enter python file name :")
      py = input("Enter python file name : ")
      os.system("ssh root@{} pip3 install joblib sklearn ; python3 bash-script/{} ".format(ip,py))
      p.speak("This is all about Salary Predictor Code") 
    elif int(choice) == 17:
      os.system("ssh root@{} pip3 install ansible ; mkdir /etc/ansible/ ; touch /etc/ansible/ansible.cfg ; ansible --version".format(ip))
      p.speak("Ansible is successfully configured")   
    elif int(choice) == 18:
      ip = input("Enter Instance IP : ")
      os.system("ssh root@{} ansible-playbook bash-script/code.yml ; rpm -q gedit ; rpm -q httpd ; rpm -q mariadb ; rpm -q tcpdump".format(ip))
      p.speak("Ansible Playbook successfully deployed and packages are installed successfully")
    elif int(choice) == 19:
      os.system("ssh root@{} ifconfig".format(ip))
      p.speak("These are the network Configurations")      
    elif int(choice) == 20:  
      p.speak("see you soon , have a nice day")
      exit()
    else: 
      print("not supported")
  
  input("\n Press Enter to continue....")
  
	








 
  