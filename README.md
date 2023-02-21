# ETL_SpreadSheetToMySql

## A simple solution to provision a database and data from a spreadsheet

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


## Design Considerations

1) I added a 10 second wait after the container with the database is instanciated. This is to ensure that the datatabase is fully ready to take connections.
2) Currently the spreadhseet is added to the same project structure. This solution can be extended by making the script more generic by looking at a pre-configured path
for available data that needs to be ETLed. This is a common business use case.
3) The python script is hosted in a flask development server. So this solution cannot be used as is in production. The solution need to be updated with a production grade webserver. 
4) There are no sanity checks and unit tests. 

