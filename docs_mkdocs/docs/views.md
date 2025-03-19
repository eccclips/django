# Views Documentation  

## Index View  
Handles the main page of the polls app.  

- **URL:** `/`  

- **Method:** `GET`  

- **Response:** Plain text "Hello, world. You're at the polls index."  

## MonitoringListView  
Handles listing and creating monitoring records.  

- **URL:** `/monitoring/`  

- **Methods:**  

  - `GET`: Returns a list of all monitoring records.  

  - `POST`: Creates a new monitoring record.  

## MonitoringDetailView  
Handles retrieving and deleting a specific monitoring record.  

- **URL:** `/monitoring/<monitoring_id>/`  

- **Methods:**  

  - `GET`: Returns details of a monitoring record.  

  - `DELETE`: Deletes the specified monitoring record.  

## VirtualsListView  
Handles listing and creating virtual machine records.  

- **URL:** `/virtuals/`  

- **Methods:**  

  - `GET`: Returns a list of all virtual machines.  

  - `POST`: Creates a new virtual machine record.  

## VirtualsDetailView  
Handles retrieving and deleting a specific virtual machine record.  

- **URL:** `/virtuals/<vm_id>/`  

- **Methods:**  

  - `GET`: Returns details of a virtual machine.  

  - `DELETE`: Deletes the specified virtual machine.  
