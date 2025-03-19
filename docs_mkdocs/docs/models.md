# Models Documentation

## Protocol (Enum)  
Represents the different types of protocols available for virtual machines.  

- **RDP**: Remote Desktop Protocol  

- **SSH**: Secure Shell  

- **VNC**: Virtual Network Computing  

## Question Model  
Represents a question in a polling application.  

**Fields:**  

- `question_text` (CharField): The text of the question.  

- `pub_date` (DateTimeField): The date when the question was published.  

**Methods:**  

- `was_published_recently()`: Checks if the question was published within the last day.  

## Choice Model  
Represents a possible answer to a `Question`.  

**Fields:**  

- `question` (ForeignKey to `Question`): The related question.  

- `choice_text` (CharField): The text of the choice.  

- `votes` (IntegerField): The number of votes this choice has received.  

## Virtuals Model  
Represents a virtual machine configuration.  

**Fields:**  

- `id` (UUIDField): Primary key.  

- `hostname` (CharField): The hostname of the VM.  

- `protocol` (CharField): The protocol used for remote connection.  

- `user_id` (ForeignKey to `User`): The owner of the VM.  

- `address` (CharField): The IP address or domain.  

- `port` (IntegerField): Port for connection.  

- `user_vm` (CharField): Username for VM access.  

- `password_vm` (CharField): Password for VM access.  

- `ignore_cert` (BooleanField): Whether to ignore SSL certificates.  

## Monitoring Model  
Tracks system usage for virtual machines.  

**Fields:**  

- `monitoring_id` (UUIDField): Primary key.  

- `cpu_usage` (FloatField): CPU usage percentage.  

- `memory_usage` (FloatField): Memory usage percentage.  

- `network_traffic` (TimeField): Network traffic.  

- `monitoring_time` (DateTimeField): Timestamp of monitoring data.  

- `virtual_machines` (ForeignKey to `Virtuals`): Related virtual machine.  

## Product Model  
Represents a product with a name and price.  

**Fields:**  

- `name` (CharField): Name of the product.  

- `price` (DecimalField): Price of the product.  
