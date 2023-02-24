# ETL_SpreadSheetToMySql

## A simple solution to provision a database and ETL data automatically from a spreadsheet

## Highlevel illustration

![image](https://user-images.githubusercontent.com/125423433/220273625-42d830ad-6708-473a-95aa-2e7bf493e5b6.png)

### Design
1) The design makes use of docker and dockercompose frameworks
2) It involves provisioning MySql database in one container and hosting the python ETL script in another container
3) Dockercompose establishes the network between both the containers to communicate seemlessly

## Usage

1) Download or clone the repo
2) Open a terminal and navigate to the root 
3) Run the following command

```
 docker-compose up
```
4) The above command will build both containers, provision the database with a database and the python script ETLs the spreadsheet data.
5) Once the ETL completion message is displayed in the terminal, you can exit by hitting ctl + c.


