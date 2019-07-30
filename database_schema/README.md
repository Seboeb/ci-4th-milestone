# Database model

## User
| Column | Data Type |
| ------ | --------- |
| id  | int NOT NULL AUTO_INCREMENT; PRIMARY KEY |
| first_name  | CharField max_length 30; DEFAULT NULL |
| last_name  | CharField max_length 30; DEFAULT NULL |
| password  | Standard Django User Password |
| email  | EmailField NOT NULL; UNIQUE |
| profile_picture  | CharField max_length 20; DEFAULT 'img/non-user.png' |
| role  | FOREIGN KEY; REFERENCES UserRole; ON DELETE CASCADE |
| watchlist  | ManyToManyField; REFERENCES Tickets; BLANK TRUE |
| created_tickets  | ManyToManyField; REFERENCES Tickets; BLANK TRUE |
| upvotes  | ManyToManyField; REFERENCES Tickets; BLANK TRUE |

## UserRole
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY |
| label_name  | CharField max_length 20; NULL FALSE |

## Donation
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY |
| amount | DecimalField; max_digits 6; decimal_places 2; DEFAULT 0 |
| date | DateTimeField; auto_now_add TRUE |
| user  | FOREIGN KEY; REFERENCES User; ON DELETE CASCADE |
| ticket  | FOREIGN KEY; REFERENCES Ticket; ON DELETE CASCADE |

## Comment
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY |
| comment | TextField; NOT NULL |
| date_created | DateTimeField; auto_now_add TRUE |
| user  | FOREIGN KEY; REFERENCES User; ON DELETE CASCADE |
| ticket  | FOREIGN KEY; REFERENCES Ticket; ON DELETE CASCADE |

## Ticket
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY |
| ticket_id  | CharField max_length 10; DEFAULT NULL |
| title  | CharField max_length 75; DEFAULT NULL |
| description  | TextField; DEFAULT NULL |
| search_field  | CharField max_lenght 200; DEFAULT NULL |
| finder_app | BooleanField; BLANK FALSE; DEFAULT FALSE |
| recipe_community | BooleanField; BLANK FALSE; DEFAULT FALSE |
| estimate_devtime  | CharField max_length 75; DEFAULT 'unkown at this moment' |
| target_amount | DecimalField; max_digits 6; decimal_places 2; DEFAULT 0 |
| donated_amount | DecimalField; max_digits 6; decimal_places 2; DEFAULT 0 |
| date_created | DateTimeField; auto_now_add TRUE |
| upvotes | IntegerField; DEFAULT 0 | 
| nr_comments | IntegerField; DEFAULT 0 |  
| user  | FOREIGN KEY; REFERENCES User; ON DELETE CASCADE |
| status  | FOREIGN KEY; REFERENCES TicketProgressLabel; ON DELETE CASCADE |
| priority  | FOREIGN KEY; REFERENCES TicketPriorityLabel; ON DELETE CASCADE |
| ticket_type  | FOREIGN KEY; REFERENCES TicketType; ON DELETE CASCADE |

## TicketProgressLabel
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY|
| label_name  | CharField max_length 20; NULL FALSE |

## TicketPriorityLabel
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY|
| label_name  | CharField max_length 20; NULL FALSE |

## TicketType
| Column | Data Type |
| ------ | --------- |
| id | int NOT NULL AUTO_INCREMENT; PRIMARY KEY|
| name  | CharField max_length 20; NULL FALSE |

